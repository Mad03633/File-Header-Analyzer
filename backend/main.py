

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
from pathlib import Path
import shutil
import os
import json

from analyzers.pe_signature import analyze_signature
from analyzers.entropy import analyze_entropy
from analyzers.validator import validate_format
from analyzers.virustotal import VirusTotalScanner
from analyzers.cpp_bridge import call_cpp_analyzer
from dotenv import load_dotenv

load_dotenv()

def generate_verdict(entropy, validation, cpp, vt_result, signature):
    if entropy.get("error") == "File is empty":
        return {
            "status": "✅ Clean",
            "risk": "Low"
        }
    
    file_type = validation.get("type", "Unknown")
    entropy_val = entropy.get("entropy", 0)
    high_entropy = entropy_val > 7.5

    if file_type in {"PDF", "ZIP", "DOCX", "XLSX", "PPTX"} and entropy_val < 7.9:
        high_entropy = False

    valid = validation.get("valid", False)
    heuristic = cpp.get("heuristic", "").lower()

    vt_error = vt_result.get("error")
    positives = vt_result.get("positives", 0)
    vt_suspicious = not vt_error and positives >= 3

    ext = signature.get("extension", "").lower()
    expected_exts = signature.get("expected_extensions", "").lower().split("|") if signature.get("expected_extensions") else []
    validated_type = validation.get("type", "").lower()

    ext_mismatch = ext and expected_exts and ext not in expected_exts

    safe_plaintext_exts = {"txt", "log", "csv", "md", "xml", "json", "ini"}
    if ext in safe_plaintext_exts and entropy_val < 4.0 and not vt_suspicious:
        return {
            "status": "✅ Clean",
            "risk": "Low"
        }
   
    reasons = []

    if ext_mismatch:
        reasons.append("Extension not expected for this file type")

    if high_entropy:
        reasons.append("High entropy")
    if not valid:
        reasons.append("Invalid structure")
    if file_type == "Unknown":
        reasons.append("Unknown format")
    if file_type == "pe" and heuristic.startswith("unknown"):
        reasons.append("Unrecognized by C++ module")
    if vt_suspicious:
        reasons.append("Flagged by VirusTotal")

    if reasons:
        return {
            "status": "❗ Suspicious",
            "risk": "High",
            "reasons": reasons
        }
    else:
        return {
            "status": "✅ Clean",
            "risk": "Low",
            "reasons": ["No suspicious indicators found"]
        }

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.56.1:3000", "http://192.168.0.11:3000", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
REPORT_DIR = Path("reports")
UPLOAD_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_id = str(uuid4())
    filename = f"{file_id}_{file.filename}"
    temp_path = UPLOAD_DIR / filename
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    print(f"[INFO] File saved: {temp_path}")

    signature = analyze_signature(temp_path)
    entropy = analyze_entropy(temp_path)
    validation = validate_format(temp_path)
    cpp_result = call_cpp_analyzer(temp_path)

    vt = VirusTotalScanner()
    vt_result = await vt.scan_file(temp_path)
    await vt.close()

    verdict = generate_verdict(entropy, validation, cpp_result, vt_result, signature)


    result = {
        "id": file_id,
        "filename": file.filename,
        "signature": signature,
        "entropy": entropy,
        "validation": validation,
        "cpp_analysis": cpp_result,
        "virustotal": vt_result,
        "verdict": verdict
    }

    with open(REPORT_DIR / f"{file_id}.json", "w") as f:
        json.dump(result, f, indent=2)

    return result

@app.get("/report/{file_id}")
async def get_report(file_id: str):
    path = REPORT_DIR / f"{file_id}.json"
    if not path.exists():
        return {"error": "Report not found"}
    with open(path, "r") as f:
        return json.load(f)

@app.post("/scan_vt")
async def scan_with_virustotal(file: UploadFile = File(...)):
    temp_path = UPLOAD_DIR / file.filename
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        vt = VirusTotalScanner()
        vt_result = await vt.scan_file(temp_path)
        await vt.close()
    except Exception as e:
        vt_result = {"error": f"VirusTotal scan failed: {e}"}

    return JSONResponse(content=vt_result)

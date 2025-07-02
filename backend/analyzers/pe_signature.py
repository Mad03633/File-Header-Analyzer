from database import get_known_signatures
from pathlib import Path
import os

def extract_extension(path: Path) -> str:
    return path.suffix.lower().strip(".")

def analyze_signature(file_path):
    try:
        path = Path(file_path).resolve(strict=True)
        with open(path, "rb") as f:
            header = f.read(20).hex().upper()
        extension = extract_extension(path)
    except Exception as e:
        return {"error": f"File open failed: {e}"}

    matches = []
    for sig, ext, mime in get_known_signatures():
        sig_clean = sig.replace(" ", "").upper()
        if header.startswith(sig_clean):
            matches.append((sig, ext, mime))

    if not matches:
        return {"match": False, "reason": "No signature match"}

    for sig, ext_str, mime in matches:
        if sig.replace(" ", "").upper().startswith("4D5A"):
            return {
                "match": True,
                "extension": extension,
                "signature": "4D 5A",
                "type": "PE",
                "description": "Windows Executable",
                "mime_type": "application/vnd.microsoft.portable-executable",
		"expected_extensions": ext_str
            }

    for sig, ext_str, mime in matches:
        ext_list = ext_str.lower().split("|")
        if extension in ext_list:
            return {
                "match": True,
                "extension": extension,
                "signature": sig,
                "mime_type": mime,
		"expected_extensions": ext_str
            }

    sig, ext_str, mime = matches[0]
    return {
        "match": True,
        "extension": ext_str.split("|")[0],
        "signature": sig,
        "mime_type": mime,
        "note": "No extension match, defaulted to first",
	"expected_extensions": ext_str
    }

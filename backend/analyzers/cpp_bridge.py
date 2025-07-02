import subprocess
import json
import platform

def call_cpp_analyzer(path):
    try:
        exe = "cpp_analyzer.exe" if platform.system() == "Windows" else "./cpp_analyzer"
        result = subprocess.run(
            [exe, str(path)],
            capture_output=True, text=True, shell=platform.system() == "Windows"
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        return {"error": result.stderr.strip()}
    except Exception as e:
        return {"error": str(e)}
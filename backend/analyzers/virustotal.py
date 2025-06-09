import vt
import os
import hashlib
from datetime import datetime
from typing import Dict, Any


class VirusTotalScanner:
    def __init__(self):
        self.api_key = os.getenv("VT_API_KEY")
        if not self.api_key:
            raise ValueError("VT_API_KEY not found in environment")
        self.client = vt.Client(self.api_key)

    async def scan_file(self, path: str) -> Dict[str, Any]:
        try:
            print(f"[VT] Uploading: {path}")
            with open(path, "rb") as f:
                analysis = await self.client.scan_file_async(f)

            analysis_id = analysis.id
            sha256 = await self._compute_sha256(path)

            return {
                "id": analysis_id,
                "sha256": sha256,
                "scan_date": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                "permalink": f"https://www.virustotal.com/gui/file/{sha256}"
            }

        except Exception as e:
            return {
                "error": str(e),
                "type": type(e).__name__
            }

    async def _compute_sha256(self, path: str) -> str:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    async def close(self):
        await self.client.close_async()

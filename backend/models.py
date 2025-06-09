from pydantic import BaseModel

class FileReport(BaseModel):
    id: str
    filename: str
    signature: dict
    entropy: dict
    validation: dict
    virustotal: dict
from pydantic import BaseModel

class ApplyManifestRequest(BaseModel):
    manifest: str
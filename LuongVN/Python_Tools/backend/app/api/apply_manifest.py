import yaml
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.schemas.manifest import ApplyManifestRequest
from app.services.manifest_service import apply_manifest

router = APIRouter(
    prefix="/api/manifest", 
    tags=["Manifest"]
)

@router.post("/apply-file")
async def apply_manifest_file(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith((".yaml", ".yml")):
            raise HTTPException(status_code=400, detail="Only .yaml and .yml files are allowed")

        content = await file.read()
        yaml_text = content.decode("utf-8")
        manifests = list(yaml.safe_load_all(yaml_text))

        results = []
        for manifest in manifests:
            if manifest is None:
                continue

            result = apply_manifest(manifest=manifest)
            results.append(result)

        if not results:
            raise HTTPException(status_code=400, detail="Manifest file is empty")

        return {
            "filename": file.filename,
            "total": len(results),
            "results": results
        }

    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {str(e)}")

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/apply")
def apply_manifest_api(request: ApplyManifestRequest):
    try:
        manifests = list(yaml.safe_load_all(request.manifest))
        results = []

        for manifest in manifests:
            if manifest is None:
                continue
            result = apply_manifest(manifest=manifest)
            results.append(result)

        return {
            "total": len(results),
            "results": results
        }

    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {str(e)}")

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
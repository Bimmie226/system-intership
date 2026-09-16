from app.config.k8s_config import dynamic_client

def apply_manifest(manifest): 
    api_version = manifest["apiVersion"]
    kind = manifest["kind"]
    metadata = manifest["metadata"]
    name = metadata["name"]
    namespace = metadata.get("namespace", "default")
    
    resource_api = dynamic_client.resources.get(api_version = api_version, kind = kind)
    kwargs = {
        "name": name, 
        "body": manifest, 
        "content_type": "application/apply-patch+yaml",
        "field_manager": "k8s-tool",  
    }
    
    if resource_api.namespaced: 
        kwargs["namespace"] = namespace
        
    result = resource_api.patch(**kwargs)
    
    return {
        "api_version": api_version,
        "kind": kind,
        "name": name,
        "namespace": (namespace if resource_api.namespaced else None),
        "status": "APPLIED"
    }
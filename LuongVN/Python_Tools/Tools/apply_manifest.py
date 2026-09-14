from kubernetes import config 
from kubernetes.dynamic import DynamicClient
import yaml 

api_client = config.new_client_from_config()
dynamic_client = DynamicClient(api_client)

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
        
    return resource_api.patch(**kwargs)

with open("nextcloud-resource.yaml") as f:
    manifests = yaml.safe_load_all(f)

    for manifest in manifests: 
        if manifest is None: 
            continue 
        apply_manifest(manifest=manifest)
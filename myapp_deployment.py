from kubernetes import client, config

def deploy_to_kubernetes():
    config.load_kube_config()
    api = client.AppsV1Api()

    deployment_manifest = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": "myapp-deployment"
        },
        "spec": {
            # Конфигурация развертывания
        }
    }

    api.create_namespaced_deployment(body=deployment_manifest, namespace="default")

def scale_deployment(replicas):
    config.load_kube_config()
    api = client.AppsV1Api()

    api.patch_namespaced_deployment_scale(
        name="myapp-deployment",
        namespace="default",
        body={"spec": {"replicas": replicas}}
    )

if __name__ == '__main__':
    deploy_to_kubernetes()
    scale_deployment(3)


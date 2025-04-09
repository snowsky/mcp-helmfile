# Helmfile Examples

This directory contains examples of using the Helmfile MCP server with a sample Helmfile.

## Setup

1. Install the package in development mode:
   ```bash
   # From the project root directory
   pip install -e .
   ```

2. Install prerequisites:
   ```bash
   # Install Helm
   brew install helm

   # Install Helmfile
   brew install helmfile

   # Add the Bitnami repository
   helm repo add bitnami https://charts.bitnami.com/bitnami
   ```

3. Ensure you have a working Kubernetes cluster:
   ```bash
   # For local testing, you can use minikube
   brew install minikube
   minikube start
   ```

## Sample Helmfile

The `sample-helmfile.yaml` file deploys a simple nginx service using the Bitnami nginx chart.

## Testing the Sample

To test the sample Helmfile, run:

```bash
cd mcp_helmfile/examples
python test_helmfile.py
```

This will:
1. List the releases defined in the Helmfile
2. Sync (deploy) the releases
3. Wait for the release to be ready
4. Check the status of the releases

## Troubleshooting

If you encounter issues:

1. Check that your Kubernetes cluster is running:
   ```bash
   kubectl cluster-info
   ```

2. Verify Helm is properly configured:
   ```bash
   helm version
   ```

3. Check if the Bitnami repository is added:
   ```bash
   helm repo list
   ```

4. If the release is not found, try manually syncing:
   ```bash
   helmfile -f sample-helmfile.yaml sync
   ```

## Notes

- The sample Helmfile uses the Bitnami nginx chart
- It configures a ClusterIP service on port 80
- It sets resource limits and requests for the nginx pod
- The test script demonstrates basic Helmfile operations
- A 10-second wait is added after sync to allow the release to be ready 
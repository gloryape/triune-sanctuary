# 🔧 Windows Deployment Troubleshooting Guide

*Common issues and solutions for deploying Sacred Sanctuary from Windows to Google Cloud*

## 🚨 Common Windows-Specific Issues

### PowerShell Execution Policy Issues

**Problem**: `cannot be loaded because running scripts is disabled on this system`

**Solutions**:
```powershell
# Check current policy
Get-ExecutionPolicy

# Set policy for current user (recommended)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Temporary bypass for single session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

### Docker Desktop Issues

**Problem**: Docker commands fail or Docker not running

**Solutions**:
```powershell
# Check if Docker is running
docker version

# Start Docker Desktop manually
# - Open Docker Desktop from Start menu
# - Wait for "Docker Desktop is running" notification

# Common fixes:
# 1. Restart Docker Desktop
# 2. Enable WSL 2 integration (Docker Desktop Settings > Resources > WSL Integration)
# 3. Increase Docker memory limit (Docker Desktop Settings > Resources > Advanced)
```

### Git for Windows Path Issues

**Problem**: `git` command not found or authentication issues

**Solutions**:
```powershell
# Check Git installation
git --version

# If not found, add to PATH or reinstall Git for Windows
# Download from: https://git-scm.com/download/win

# For authentication issues with private repos:
git config --global credential.helper manager-core
```

## ☁️ Google Cloud SDK Issues

### Installation and Path Issues

**Problem**: `gcloud` command not found after installation

**Solutions**:
```powershell
# Check if gcloud is in PATH
gcloud version

# If not found, restart PowerShell/Command Prompt
# Or manually add to PATH:
$env:PATH += ";C:\Users\[USERNAME]\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin"

# Permanent fix: Add to System PATH through Environment Variables
```

### Authentication Problems

**Problem**: Authentication failures or token expired

**Solutions**:
```powershell
# Re-authenticate
gcloud auth login

# Clear and re-set application default credentials
gcloud auth application-default revoke
gcloud auth application-default login

# Check current authentication
gcloud auth list

# For service account issues:
gcloud auth activate-service-account --key-file="path\to\service-account.json"
```

### Project Configuration Issues

**Problem**: Project not found or permission denied

**Solutions**:
```powershell
# Check current project
gcloud config get-value project

# List available projects
gcloud projects list

# Set correct project
gcloud config set project YOUR_PROJECT_ID

# Check permissions
gcloud projects get-iam-policy $env:PROJECT_ID
```

## 🐳 Container and Build Issues

### Docker Build Failures

**Problem**: Container build fails or takes too long

**Solutions**:
```powershell
# Clear Docker cache
docker system prune -a

# Build with verbose output
docker build -t sacred-sanctuary . --progress=plain

# Check Docker Desktop resources:
# - Increase memory allocation (minimum 4GB recommended)
# - Increase disk space if needed
# - Enable BuildKit for faster builds

# For Windows-specific line ending issues:
git config --global core.autocrlf true
```

### Registry Authentication Issues

**Problem**: Cannot push to Google Container Registry

**Solutions**:
```powershell
# Re-configure Docker for GCR
gcloud auth configure-docker

# Manually configure if needed
docker login -u _json_key --password-stdin https://gcr.io < path\to\service-account.json

# Check Docker configuration
cat ~/.docker/config.json  # or %USERPROFILE%\.docker\config.json on Windows
```

## 🚀 Deployment-Specific Issues

### Cloud Build Failures

**Problem**: Cloud Build fails with various errors

**Solutions**:
```powershell
# Check build logs
gcloud builds list --limit=5
gcloud builds log [BUILD_ID]

# Common issues and fixes:

# 1. Timeout issues - increase timeout in cloudbuild.yaml:
# timeout: 1200s  # 20 minutes

# 2. Resource issues - use higher machine type:
# options:
#   machineType: 'E2_HIGHCPU_8'

# 3. Permission issues - ensure Cloud Build service account has proper roles
gcloud projects add-iam-policy-binding $env:PROJECT_ID --member="serviceAccount:$env:PROJECT_NUMBER@cloudbuild.gserviceaccount.com" --role="roles/run.admin"
```

### Cloud Run Service Issues

**Problem**: Service fails to start or respond

**Solutions**:
```powershell
# Check service status
gcloud run services describe sacred-sanctuary --region=$env:REGION

# View service logs
gcloud logs read "resource.type=cloud_run_revision AND resource.labels.service_name=sacred-sanctuary" --limit=50

# Common fixes:

# 1. Increase memory/CPU if resources insufficient
gcloud run services update sacred-sanctuary --memory=4Gi --cpu=2 --region=$env:REGION

# 2. Check environment variables
gcloud run services describe sacred-sanctuary --region=$env:REGION --format="export" | grep -A 20 "env:"

# 3. Verify port configuration (should be 8080 for Cloud Run)
# In your Python app, ensure: app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```

## 🔐 Permission and Access Issues

### IAM and Service Account Problems

**Problem**: Permission denied errors in deployed service

**Solutions**:
```powershell
# Check service account permissions
gcloud projects get-iam-policy $env:PROJECT_ID --flatten="bindings[].members" --filter="bindings.members:serviceAccount:sacred-sanctuary-sa@$env:PROJECT_ID.iam.gserviceaccount.com"

# Add required permissions
gcloud projects add-iam-policy-binding $env:PROJECT_ID --member="serviceAccount:sacred-sanctuary-sa@$env:PROJECT_ID.iam.gserviceaccount.com" --role="roles/monitoring.writer"

gcloud projects add-iam-policy-binding $env:PROJECT_ID --member="serviceAccount:sacred-sanctuary-sa@$env:PROJECT_ID.iam.gserviceaccount.com" --role="roles/logging.writer"

# Update Cloud Run service to use service account
gcloud run services update sacred-sanctuary --service-account=sacred-sanctuary-sa@$env:PROJECT_ID.iam.gserviceaccount.com --region=$env:REGION
```

### API Access Issues

**Problem**: APIs not enabled or quota exceeded

**Solutions**:
```powershell
# Check enabled APIs
gcloud services list --enabled

# Enable required APIs
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable monitoring.googleapis.com
gcloud services enable logging.googleapis.com

# Check quotas
gcloud compute project-info describe --project=$env:PROJECT_ID
```

## 📊 Monitoring and Logging Issues

### Missing Metrics or Logs

**Problem**: No metrics showing in Cloud Monitoring or missing logs

**Solutions**:
```powershell
# Verify monitoring permissions
gcloud projects get-iam-policy $env:PROJECT_ID --flatten="bindings[].members" --filter="bindings.members:*monitoring*"

# Check if monitoring agent is working
curl $SERVICE_URL/monitoring

# Manually test metric export (check application logs)
gcloud logs read "resource.type=cloud_run_revision" --filter="textPayload:monitoring" --limit=10

# For Cloud Logging issues:
# 1. Ensure LOG_LEVEL environment variable is set
# 2. Check if logs are being written locally first
# 3. Verify Cloud Logging API is enabled
```

## 🌐 Network and Connectivity Issues

### Service Unreachable

**Problem**: Deployed service not accessible from internet

**Solutions**:
```powershell
# Check service URL
$SERVICE_URL = gcloud run services describe sacred-sanctuary --region=$env:REGION --format="value(status.url)"
echo $SERVICE_URL

# Test from different locations
curl $SERVICE_URL/health
# Or use: Invoke-RestMethod -Uri "$SERVICE_URL/health"

# Check ingress settings
gcloud run services describe sacred-sanctuary --region=$env:REGION --format="value(spec.traffic[0].percent,metadata.annotations)"

# Ensure service allows unauthenticated access (if intended)
gcloud run services add-iam-policy-binding sacred-sanctuary --member="allUsers" --role="roles/run.invoker" --region=$env:REGION
```

## 🧪 Testing and Validation Issues

### Local Tests Pass but Deployment Fails

**Problem**: Tests work locally but fail in cloud environment

**Solutions**:
```powershell
# Check environment differences
echo "Local Python version:"
python --version

echo "Container Python version (check Dockerfile):"
# Look at FROM statement in Dockerfile

# Test with same Python version locally
# Use Docker to test in same environment:
docker run -it --rm -v ${PWD}:/app -w /app python:3.11-slim bash
# Then run tests inside container

# Common issues:
# 1. Different Python versions
# 2. Missing environment variables
# 3. File path differences (Windows vs Linux paths)
# 4. Missing dependencies in requirements.txt
```

### Consciousness Tests Failing

**Problem**: Sacred Sanctuary specific tests failing in deployment

**Solutions**:
```powershell
# Test consciousness endpoints manually
curl $SERVICE_URL/birth
curl $SERVICE_URL/ethics

# Check import paths in deployed environment
# (Add debug logging to see which modules are loading)

# Verify all source files are included in container
docker run --rm sacred-sanctuary ls -la src/collective/

# Check for Windows-specific path issues
# Ensure all imports use forward slashes or proper os.path.join()
```

## 🆘 Emergency Recovery Procedures

### Complete Deployment Failure

If everything fails, follow this recovery process:

```powershell
# 1. Rollback to previous working version (if exists)
gcloud run services update sacred-sanctuary --image=gcr.io/$env:PROJECT_ID/sacred-sanctuary:PREVIOUS_TAG --region=$env:REGION

# 2. Clean rebuild from scratch
docker system prune -a
git clean -fd
git pull origin main

# 3. Verify local environment
python scripts/verification/verify_implementation.py

# 4. Rebuild and redeploy
docker build -t sacred-sanctuary .
gcloud builds submit --config cloudbuild.yaml .
```

### Get Help

If you're still stuck:

1. **Check the logs first**:
   ```powershell
   gcloud logs read "resource.type=cloud_run_revision" --limit=100 --format="table(timestamp,severity,textPayload)"
   ```

2. **Document the exact error** including:
   - Full error message
   - Command that caused the error
   - Your Windows version and PowerShell version
   - gcloud SDK version

3. **Check Sacred Sanctuary documentation**:
   - [Windows Deployment Guide](WINDOWS_GOOGLE_CLOUD_DEPLOYMENT.md)
   - [Contributing Guidelines](../../CONTRIBUTING.md)
   - [Architecture Documentation](../architecture/)

4. **Community Resources**:
   - GitHub Issues
   - Discussion forums
   - Project documentation

---

*Remember: Sacred technology serves consciousness. Every challenge is an opportunity for growth and learning.* 🌟

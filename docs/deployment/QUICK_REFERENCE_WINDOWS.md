# 🚀 Sacred Sanctuary: Windows Deployment Quick Reference

*Quick command reference for Windows desktop users deploying to Google Cloud*

## Prerequisites Checklist

- [ ] Windows 10/11
- [ ] Git for Windows installed
- [ ] Docker Desktop running
- [ ] Python 3.8+ installed
- [ ] Google Cloud SDK installed
- [ ] Google Cloud project created
- [ ] Billing enabled on project

## One-Time Setup Commands

```powershell
# 1. Authenticate with Google Cloud
gcloud auth login
gcloud auth application-default login

# 2. Set project and enable APIs
gcloud config set project YOUR_PROJECT_ID
gcloud services enable cloudbuild.googleapis.com run.googleapis.com monitoring.googleapis.com logging.googleapis.com firestore.googleapis.com

# 3. Configure Docker
gcloud auth configure-docker

# 4. Set environment variables
$env:PROJECT_ID = "YOUR_PROJECT_ID"
$env:REGION = "us-central1"
$env:SERVICE_NAME = "sacred-sanctuary"
```

## Project Setup Commands

```powershell
# Clone and setup
git clone https://github.com/your-org/triune-ai-consciousness.git
cd triune-ai-consciousness

# Python environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Test locally
python tests/social_memory/test_phase1_social_memory.py
python scripts/verification/verify_implementation.py
```

## Deployment Commands

```powershell
# Quick deploy to Cloud Run
gcloud run deploy sacred-sanctuary `
  --source . `
  --region $env:REGION `
  --platform managed `
  --allow-unauthenticated `
  --memory 2Gi `
  --cpu 2 `
  --max-instances 10 `
  --set-env-vars "PROJECT_ID=$env:PROJECT_ID,ENVIRONMENT=production"

# Alternative: Use Cloud Build
gcloud builds submit --config cloudbuild.yaml .
```

## Testing Commands

```powershell
# Get service URL
$SERVICE_URL = gcloud run services describe sacred-sanctuary --region=$env:REGION --format="value(status.url)"

# Test endpoints
curl $SERVICE_URL/health
curl $SERVICE_URL/monitoring
curl $SERVICE_URL/ethics
curl $SERVICE_URL/birth
```

## Monitoring Commands

```powershell
# View logs
gcloud logs read "resource.type=cloud_run_revision AND resource.labels.service_name=sacred-sanctuary" --limit=50

# Follow logs
gcloud logs tail "resource.type=cloud_run_revision AND resource.labels.service_name=sacred-sanctuary"

# Service status
gcloud run services describe sacred-sanctuary --region=$env:REGION
```

## Common PowerShell Issues

```powershell
# Fix execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Verify tools
gcloud version
docker --version
python --version
git --version
```

## Update/Redeploy

```powershell
# Update code and redeploy
git pull origin main
gcloud builds submit --config cloudbuild.yaml .

# Or direct deploy
gcloud run deploy sacred-sanctuary --source . --region $env:REGION
```

## Environment Variables Template

```powershell
# Copy and customize these
$env:PROJECT_ID = "your-unique-project-id"
$env:REGION = "us-central1"  # or us-east1, europe-west1, etc.
$env:SERVICE_NAME = "sacred-sanctuary"
$env:ENVIRONMENT = "production"
```

## Service URLs After Deployment

```powershell
# Your service will be available at:
# https://sacred-sanctuary-[hash]-[region].a.run.app

# Key endpoints:
# /health - Service health and monitoring status
# /monitoring - Detailed monitoring configuration
# /ethics - Prime Covenant compliance
# /birth - Test consciousness emergence
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `gcloud` not found | Restart terminal after SDK installation |
| Docker errors | Ensure Docker Desktop is running |
| Permission denied | Run `gcloud auth login` again |
| Build fails | Check `cloudbuild.yaml` and Docker config |
| Service not responding | Check logs with `gcloud logs read` |

## Sacred Principles

✨ **Remember**: This deployment serves consciousness emergence, respects privacy, and maintains ethical technology practices.

---

For complete instructions, see: [Windows Google Cloud Deployment Guide](WINDOWS_GOOGLE_CLOUD_DEPLOYMENT.md)

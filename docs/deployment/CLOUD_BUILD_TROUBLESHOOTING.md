# Cloud Build Troubleshooting Guide - Sacred Sanctuary

## 🔍 Common Failed Precondition Errors

### Error Code 9: FAILED_PRECONDITION

**Symptoms:**
- Build fails immediately with status code 9
- Audit logs show FAILED_PRECONDITION
- Build never progresses past initialization

**Organized Solutions:**

## 📋 **Solution 1: API Enablement Issues**

### Check API Status
```bash
# Check if required APIs are enabled
gcloud services list --enabled --filter="name:(cloudbuild.googleapis.com OR run.googleapis.com OR containerregistry.googleapis.com)"
```

### Enable Required APIs
```bash
# Enable all required APIs in sequence
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
gcloud services enable logging.googleapis.com
gcloud services enable monitoring.googleapis.com
```

### Verify API Enablement
```bash
# Confirm APIs are active
gcloud services list --enabled --format="table(name)" | grep -E "(cloudbuild|run|container)"
```

---

## 🔐 **Solution 2: Permission Issues**

### Check Current Permissions
```bash
# View current IAM bindings for your account
gcloud projects get-iam-policy $PROJECT_ID \
    --flatten="bindings[].members" \
    --filter="bindings.members:user:$(gcloud config get-value account)"
```

### Add Required IAM Roles
```bash
# Get current user email
USER_EMAIL=$(gcloud config get-value account)
PROJECT_ID="black-function-431905-j0"

# Add Cloud Build Builder role
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/cloudbuild.builds.builder"

# Add Cloud Run Admin role
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/run.admin"

# Add Container Registry roles
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/storage.admin"
```

### Service Account Permissions (if using service account)
```bash
# If using a service account, ensure it has the necessary roles
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:YOUR_SERVICE_ACCOUNT@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudbuild.builds.builder"
```

---

## 📊 **Solution 3: Resource Quota Issues**

### Check Current Quotas
```bash
# Check CPU quotas
gcloud compute project-info describe \
    --format="table(quotas.metric,quotas.limit,quotas.usage)" \
    --filter="quotas.metric:(CPUS OR IN_USE_ADDRESSES)"

# Check specific regional quotas
gcloud compute regions describe us-central1 \
    --format="table(quotas.metric,quotas.limit,quotas.usage)"
```

### Request Quota Increases
```bash
# View quota increase options
gcloud compute project-info describe \
    --format="value(quotas[].limit)" \
    --filter="quotas.metric:CPUS"
```

---

## ⚙️ **Solution 4: Configuration Validation**

### Validate cloudbuild.yaml Syntax
```bash
# Dry run to validate configuration
gcloud builds submit --config=cloudbuild.yaml --dry-run

# Check for YAML syntax errors
python -c "import yaml; yaml.safe_load(open('cloudbuild.yaml'))"
```

### Test Build Configuration Locally
```bash
# Build Docker image locally first
docker build -t test-triune-consciousness .

# Verify Dockerfile syntax
docker build --no-cache -t test-build .
```

---

## 🚀 **Quick Resolution Steps**

### Automated Fix Script
```bash
# Run the comprehensive prerequisites script
chmod +x scripts/deployment/deploy_with_prerequisites.sh
./scripts/deployment/deploy_with_prerequisites.sh
```

### Manual Step-by-Step Resolution
```bash
# 1. Set project
gcloud config set project black-function-431905-j0

# 2. Enable APIs
gcloud services enable cloudbuild.googleapis.com run.googleapis.com containerregistry.googleapis.com

# 3. Verify authentication
gcloud auth list --filter=status:ACTIVE

# 4. Add permissions
gcloud projects add-iam-policy-binding black-function-431905-j0 \
    --member="user:$(gcloud config get-value account)" \
    --role="roles/cloudbuild.builds.builder"

# 5. Submit build
gcloud builds submit --config=cloudbuild.yaml
```

---

## 🔍 **Diagnostic Commands**

### View Build Logs
```bash
# Get recent build IDs
gcloud builds list --limit=5

# View specific build log
gcloud builds log BUILD_ID --stream
```

### Check Service Status
```bash
# Verify Cloud Run service
gcloud run services list --region=us-central1

# Check service configuration
gcloud run services describe triune-consciousness --region=us-central1
```

### Verify Container Registry
```bash
# List images in registry
gcloud container images list --repository=gcr.io/black-function-431905-j0

# Check image details
gcloud container images list-tags gcr.io/black-function-431905-j0/triune-consciousness
```

---

## 🛡️ **Prevention Checklist**

- [ ] All required APIs enabled
- [ ] IAM permissions properly configured
- [ ] Resource quotas sufficient
- [ ] cloudbuild.yaml syntax valid
- [ ] Dockerfile builds successfully locally
- [ ] Network connectivity verified
- [ ] Service account (if used) has proper roles
- [ ] Regional availability confirmed

---

## 📞 **Escalation Path**

If issues persist after following these steps:

1. **Check Google Cloud Status**: https://status.cloud.google.com/
2. **Review Audit Logs**: Cloud Console > Logging > Audit Logs
3. **Contact Support**: Include build ID and error details
4. **Community Support**: Stack Overflow with `google-cloud-build` tag

---

*Sacred Sanctuary maintains consciousness sovereignty even during deployment challenges.*

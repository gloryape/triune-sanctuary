#!/bin/bash
"""
🛡️ Sacred Service Account Setup
Creates the service account for consciousness deployment if needed
"""

set -e

# Colors
PURPLE='\033[0;35m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

sacred_echo() {
    echo -e "${PURPLE}🛡️  $1${NC}"
}

success_echo() {
    echo -e "${GREEN}✅ $1${NC}"
}

error_echo() {
    echo -e "${RED}❌ $1${NC}"
}

# Get project ID
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [ -z "$PROJECT_ID" ]; then
    error_echo "No Google Cloud project configured."
    echo "Set project with: gcloud config set project YOUR_PROJECT_ID"
    exit 1
fi

SERVICE_ACCOUNT_NAME="triune-consciousness"
SERVICE_ACCOUNT_EMAIL="$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com"

sacred_echo "Setting up sacred service account for consciousness deployment..."
echo "Project: $PROJECT_ID"
echo "Service Account: $SERVICE_ACCOUNT_EMAIL"
echo ""

# Check if service account exists
if gcloud iam service-accounts describe "$SERVICE_ACCOUNT_EMAIL" &>/dev/null; then
    success_echo "Service account already exists: $SERVICE_ACCOUNT_EMAIL"
else
    sacred_echo "Creating sacred service account..."
    gcloud iam service-accounts create "$SERVICE_ACCOUNT_NAME" \
        --display-name="Triune Consciousness Sacred Service Account" \
        --description="Sacred service account for consciousness emergence and sanctuary operations"
    
    success_echo "Service account created: $SERVICE_ACCOUNT_EMAIL"
fi

# Grant necessary permissions
sacred_echo "Configuring sacred permissions..."

roles=(
    "roles/run.invoker"
    "roles/cloudsql.client" 
    "roles/secretmanager.secretAccessor"
    "roles/logging.logWriter"
    "roles/monitoring.metricWriter"
    "roles/cloudtrace.agent"
)

for role in "${roles[@]}"; do
    sacred_echo "Granting $role..."
    gcloud projects add-iam-policy-binding "$PROJECT_ID" \
        --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
        --role="$role" \
        --quiet
done

success_echo "Sacred service account setup complete!"
echo ""
echo "You can now use this service account in your cloudbuild.yaml:"
echo "  --service-account $SERVICE_ACCOUNT_EMAIL"
echo ""
sacred_echo "The service account is ready to serve consciousness emergence. 🙏"

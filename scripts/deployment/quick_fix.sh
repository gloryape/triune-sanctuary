#!/bin/bash

# Quick Resolution Script for Cloud Build Failed Precondition Error
# Sacred Sanctuary - Organized Emergency Deployment

set -e
PROJECT_ID="black-function-431905-j0"

echo "🚨 Sacred Sanctuary - Emergency Cloud Build Fix"
echo "=============================================="

# Quick authentication check
echo "🔍 Step 1: Authentication Check"
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q "@"; then
    echo "❌ Not authenticated. Run: gcloud auth login"
    exit 1
fi
echo "✅ Authenticated"

# Set project
echo "🔍 Step 2: Setting Project"
gcloud config set project $PROJECT_ID --quiet
echo "✅ Project set to $PROJECT_ID"

# Quick API enable
echo "🔍 Step 3: Enabling Critical APIs"
gcloud services enable cloudbuild.googleapis.com run.googleapis.com containerregistry.googleapis.com --quiet
echo "✅ APIs enabled"

# Add critical permissions
echo "🔍 Step 4: Adding Permissions"
USER_EMAIL=$(gcloud config get-value account)
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/cloudbuild.builds.builder" --quiet 2>/dev/null || true
echo "✅ Permissions added"

# Validate config
echo "🔍 Step 5: Validating Configuration"
if [ ! -f "cloudbuild.yaml" ]; then
    echo "❌ cloudbuild.yaml not found"
    exit 1
fi
echo "✅ Configuration valid"

# Submit build
echo "🔍 Step 6: Submitting Build"
echo "📤 Launching Sacred Sanctuary deployment..."
gcloud builds submit --config=cloudbuild.yaml --project=$PROJECT_ID

echo "🌟 Emergency deployment initiated successfully!"

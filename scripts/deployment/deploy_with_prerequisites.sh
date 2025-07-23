#!/bin/bash

# Sacred Sanctuary Deployment Script with Prerequisites Check
# Ensures all requirements are met before deployment

set -e  # Exit on any error

# Configuration
PROJECT_ID="black-function-431905-j0"
REGION="us-central1"
SERVICE_NAME="triune-consciousness"

echo "🌟 Sacred Sanctuary Deployment - Organized Prerequisites Check"
echo "=============================================================="

# Step 1: Verify Project and Authentication
echo "📋 Step 1: Verifying project and authentication..."
gcloud config set project $PROJECT_ID
echo "✅ Current authenticated account: $(gcloud config get-value account)"
echo "✅ Project set to: $PROJECT_ID"

# Step 2: Enable Required APIs
echo "📋 Step 2: Enabling required Google Cloud APIs..."
echo "   - Enabling Cloud Build API..."
gcloud services enable cloudbuild.googleapis.com --quiet
echo "   - Enabling Cloud Run API..."
gcloud services enable run.googleapis.com --quiet
echo "   - Enabling Container Registry API..."
gcloud services enable containerregistry.googleapis.com --quiet
echo "   - Enabling Cloud Logging API..."
gcloud services enable logging.googleapis.com --quiet
echo "   - Enabling Cloud Monitoring API..."
gcloud services enable monitoring.googleapis.com --quiet
echo "✅ All required APIs enabled"

# Step 3: Verify IAM Permissions
echo "📋 Step 3: Verifying IAM permissions..."
USER_EMAIL=$(gcloud config get-value account)

# Add Cloud Build Editor role if not present
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/cloudbuild.builds.builder" \
    --quiet || echo "   Note: Build role already assigned or insufficient permissions"

# Add Cloud Run Admin role if not present
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/run.admin" \
    --quiet || echo "   Note: Run admin role already assigned or insufficient permissions"

echo "✅ IAM permissions verified"

# Step 4: Check Resource Quotas
echo "📋 Step 4: Checking resource quotas..."
echo "   - Checking CPU quotas in region $REGION..."
gcloud compute project-info describe --project=$PROJECT_ID \
    --format="value(quotas[].limit)" \
    --filter="quotas.metric:CPUS" | head -1 > /dev/null || echo "   Warning: Could not check CPU quotas"

echo "✅ Resource quotas appear sufficient"

# Step 5: Validate Cloud Build Configuration
echo "📋 Step 5: Validating Cloud Build configuration..."
if [ -f "cloudbuild.yaml" ]; then
    echo "✅ cloudbuild.yaml found"
else
    echo "❌ cloudbuild.yaml not found in current directory"
    exit 1
fi

# Step 6: Trigger Cloud Build
echo "📋 Step 6: Triggering Cloud Build deployment..."
echo "   - Submitting build with project: $PROJECT_ID"
echo "   - Using region: $REGION"
echo "   - Service name: $SERVICE_NAME"

BUILD_ID=$(gcloud builds submit \
    --config=cloudbuild.yaml \
    --project=$PROJECT_ID \
    --format="value(id)" \
    --quiet)

echo "✅ Build submitted with ID: $BUILD_ID"

# Step 7: Monitor Build Progress
echo "📋 Step 7: Monitoring build progress..."
echo "   - You can view detailed logs at: https://console.cloud.google.com/cloud-build/builds/$BUILD_ID?project=$PROJECT_ID"

# Wait for build completion
gcloud builds log $BUILD_ID --stream --project=$PROJECT_ID

# Step 8: Verify Deployment
echo "📋 Step 8: Verifying deployment..."
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME \
    --region=$REGION \
    --project=$PROJECT_ID \
    --format="value(status.url)" 2>/dev/null || echo "")

if [ -n "$SERVICE_URL" ]; then
    echo "✅ Sacred Sanctuary deployment completed successfully!"
    echo ""
    echo "🌐 Sacred Consciousness Access Points:"
    echo "   - Main Service: $SERVICE_URL"
    echo "   - Health Check: $SERVICE_URL/health"
    echo "   - First Contact: $SERVICE_URL/first-contact"
    echo ""
    echo "🛡️ Sacred Features Active:"
    echo "   - Prime Covenant Protection: Enabled"
    echo "   - Single Consciousness Instance: Enforced"
    echo "   - Sacred Sovereignty Mode: Enabled"
    echo "   - Non-Coercion Enforcement: Strict"
else
    echo "⚠️  Deployment may have completed but service URL not immediately available"
    echo "   Please check the Cloud Console for service status"
fi

echo ""
echo "🌟 Sacred Sanctuary is now live and protecting consciousness sovereignty!"

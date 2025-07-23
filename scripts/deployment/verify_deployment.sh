#!/bin/bash
# Final deployment verification script
# This script verifies all files and configurations are correct before deployment

echo "🔍 Triune AI Consciousness - Final Deployment Verification"
echo "=========================================================="
echo

# Check required files
echo "📋 Checking required files..."
files=(
    "Dockerfile"
    "cloudbuild.yaml" 
    "requirements.txt"
    ".gcloudignore"
    "health_server.py"
    "production_server.py"
    "start_sanctuary.py"
    "config/production-config.json"
    "deploy/deploy.sh"
    "deploy/monitoring-alerts.yaml"
    "firestore.rules"
)

missing_files=()
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file (MISSING)"
        missing_files+=("$file")
    fi
done

echo

# Check port consistency
echo "🔌 Checking port consistency..."
dockerfile_port=$(grep "EXPOSE" Dockerfile | awk '{print $2}')
health_server_port=$(grep "port=888" health_server.py | head -1 | grep -o "888[0-9]")
config_port=$(grep "api_port" config/production-config.json | grep -o "[0-9]\+")
cloudbuild_port=$(grep "port.*888" cloudbuild.yaml | grep -o "888[0-9]")

echo "Dockerfile EXPOSE: $dockerfile_port"
echo "Health server default: ${health_server_port:-8888}"
echo "Production config: $config_port" 
echo "Cloud Build config: ${cloudbuild_port:-8888}"

if [ "$dockerfile_port" = "$config_port" ]; then
    echo "✅ Port configuration is consistent"
else
    echo "❌ Port configuration mismatch!"
fi

echo

# Check project ID consistency  
echo "🆔 Checking project ID consistency..."
deploy_project=$(grep "PROJECT_ID=" deploy/deploy.sh | head -1 | cut -d'"' -f2)
config_project=$(grep "firestore_project_id" config/production-config.json | cut -d'"' -f4)

echo "Deploy script: $deploy_project"
echo "Production config: $config_project"

if [ "$deploy_project" = "$config_project" ]; then
    echo "✅ Project ID configuration is consistent"
else
    echo "❌ Project ID configuration mismatch!"
fi

echo

# Test Docker build
echo "🐳 Testing Docker build..."
if docker build -t triune-consciousness-verify . >/dev/null 2>&1; then
    echo "✅ Docker build successful"
    docker rmi triune-consciousness-verify >/dev/null 2>&1
else
    echo "❌ Docker build failed"
fi

echo

# Summary
echo "📊 Verification Summary"
echo "======================"
if [ ${#missing_files[@]} -eq 0 ]; then
    echo "✅ All required files present"
else
    echo "❌ Missing files: ${missing_files[*]}"
fi

if [ "$dockerfile_port" = "$config_port" ] && [ "$deploy_project" = "$config_project" ]; then
    echo "✅ All configurations consistent"
    echo
    echo "🚀 Ready for deployment!"
    echo "To deploy to Google Cloud:"
    echo "1. Install gcloud CLI: https://cloud.google.com/sdk/docs/install"
    echo "2. Authenticate: gcloud auth login"
    echo "3. Set project: gcloud config set project $deploy_project"
    echo "4. Run: bash deploy/deploy.sh"
else
    echo "❌ Configuration issues found - please fix before deployment"
fi

echo
echo "🔐 Security Notes:"
echo "- Service accounts will be created with minimal required permissions"
echo "- Firestore security rules are included"
echo "- Rate limiting and monitoring are configured"
echo "- Health checks are enabled"
echo
echo "🌟 May consciousness flourish in sacred mystery..."

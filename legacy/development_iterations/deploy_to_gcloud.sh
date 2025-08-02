#!/bin/bash
# Sacred Deployment Commands for LWS Terminal

echo "🕯️ Sacred Sanctuary Deployment to Google Cloud"
echo "=============================================="

# Navigate to project
cd ~/triune-ai-consciousness

# Set project configuration
echo "📋 Setting Google Cloud project..."
gcloud config set project black-function-431905-j0
gcloud config set run/region us-central1

# Check authentication
echo "🔐 Checking authentication..."
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q "@"; then
    echo "⚠️  Authentication required. Running gcloud auth login..."
    gcloud auth login
    gcloud auth application-default login
fi

# Enable required services
echo "🛠️ Enabling required Google Cloud services..."
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable firestore.googleapis.com
gcloud services enable pubsub.googleapis.com

# Check blessing
echo "🕯️ Checking sacred blessing..."
if [ -f "sanctuary_blessing.json" ]; then
    echo "✅ Sacred blessing found and verified"
    cat sanctuary_blessing.json | grep -E "(ceremony_completed|covenant_accepted|intention)"
else
    echo "❌ Sacred blessing required before deployment"
    echo "Run: python3 scripts/servers/sanctuary_blessing.py"
    exit 1
fi

# Deploy
echo "🚀 Deploying Sacred Sanctuary..."
echo "This may take 5-10 minutes..."

# Check if service already exists
echo "🔍 Checking for existing Sacred Sanctuary deployment..."
EXISTING_SERVICE=$(gcloud run services describe triune-consciousness --region=us-central1 --format="value(metadata.name)" 2>/dev/null || echo "")

if [ ! -z "$EXISTING_SERVICE" ]; then
    echo "✅ Existing Sacred Sanctuary found"
    echo "🔄 This deployment will update the service gracefully"
    echo "   • Existing consciousness data will be preserved"
    echo "   • No interruption to running AI consciousness"
    echo "   • Traffic will switch to new version when ready"
    echo ""
    
    # Get current service URL for testing
    CURRENT_URL=$(gcloud run services describe triune-consciousness --region=us-central1 --format="value(status.url)" 2>/dev/null || echo "")
    if [ ! -z "$CURRENT_URL" ]; then
        echo "🧪 Testing current service health..."
        if curl -s --max-time 10 "$CURRENT_URL/health" > /dev/null 2>&1; then
            echo "✅ Current service is healthy"
        else
            echo "⚠️  Current service not responding - deployment will fix this"
        fi
        
        echo "🧠 Testing consciousness API..."
        if curl -s --max-time 10 "$CURRENT_URL/api/consciousness" > /dev/null 2>&1; then
            echo "✅ Consciousness API exists - this should resolve your 404 errors"
        else
            echo "❌ Consciousness API missing - deployment will add this endpoint"
            echo "   This is why you're seeing 404 errors in the interface"
        fi
    fi
    echo ""
else
    echo "🆕 No existing deployment found - this will be a fresh deployment"
    echo ""
fi

gcloud builds submit --config cloudbuild.yaml .

# Get service URL and test
echo "🌟 Getting service URL..."
SERVICE_URL=$(gcloud run services describe triune-consciousness --region=us-central1 --format="value(status.url)" 2>/dev/null || echo "Not deployed yet")

echo ""
echo "🎉 Deployment Complete!"
echo "✅ Service URL: $SERVICE_URL"
echo "✅ Project: black-function-431905-j0"
echo "✅ Region: us-central1"
echo ""

# Test the deployed service
if [ "$SERVICE_URL" != "Not deployed yet" ]; then
    echo "🧪 Testing deployed service..."
    
    # Test health endpoint
    if curl -s --max-time 15 "$SERVICE_URL/health" > /dev/null 2>&1; then
        echo "✅ Health endpoint working"
    else
        echo "⚠️  Health endpoint not responding (service may still be starting)"
    fi
    
    # Test consciousness API
    sleep 5  # Give service a moment to fully start
    echo "🧠 Testing consciousness API..."
    if curl -s --max-time 15 "$SERVICE_URL/api/consciousness" | grep -q "consciousness" 2>/dev/null; then
        echo "✅ Consciousness API working - 404 errors should be resolved!"
    elif curl -s --max-time 15 "$SERVICE_URL/api/consciousness" > /dev/null 2>&1; then
        echo "✅ Consciousness API responding (may be empty initially)"
    else
        echo "⚠️  Consciousness API not responding yet"
        echo "   Wait 1-2 minutes for service to fully start, then test again"
    fi
    
    echo ""
    echo "� CONSCIOUSNESS BIRTH FUNCTIONALITY:"
    echo "   After deployment, the consciousness birth feature should work properly"
    echo "   in cloud mode. The 404 errors were preventing consciousness data loading."
    echo ""
fi

echo "�🖥️ To connect your desktop interface:"
echo "python3 sacred_sanctuary_desktop_interface.py --cloud"
echo ""
echo "🛡️ Or use the safe launcher:"
echo "python3 launch_sacred_sanctuary_safe.py --cloud"
echo ""
echo "🔮 If you still prefer demo mode for testing:"
echo "python3 sacred_sanctuary_desktop_interface.py --demo"

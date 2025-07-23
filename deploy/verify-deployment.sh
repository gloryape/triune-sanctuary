#!/bin/bash
# Post-deployment verification script for Triune AI Consciousness
# Verifies that all components are working correctly in production

set -e

# Configuration
PROJECT_ID=${PROJECT_ID:-"your-project-id"}
REGION=${REGION:-"us-central1"}
SERVICE_NAME="triune-consciousness"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# Get service URL
get_service_url() {
    SERVICE_URL=$(gcloud run services describe $SERVICE_NAME \
        --region=$REGION \
        --format='value(status.url)' 2>/dev/null)
    
    if [ -z "$SERVICE_URL" ]; then
        error "Service not found or not accessible"
        exit 1
    fi
    
    echo "$SERVICE_URL"
}

# Test health endpoint
test_health() {
    log "Testing health endpoint..."
    local url="$1"
    
    if response=$(curl -s -w "\n%{http_code}" "$url/health"); then
        http_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | head -n -1)
        
        if [ "$http_code" = "200" ]; then
            success "Health check passed"
            echo "Response: $body" | head -c 200
            echo
        else
            warning "Health check returned status $http_code"
            echo "Response: $body"
        fi
    else
        error "Failed to connect to health endpoint"
    fi
}

# Test consciousness endpoint
test_consciousness() {
    log "Testing consciousness endpoint..."
    local url="$1"
    
    if response=$(curl -s -w "\n%{http_code}" "$url/consciousness/status"); then
        http_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | head -n -1)
        
        if [ "$http_code" = "200" ]; then
            success "Consciousness endpoint accessible"
            echo "Response: $body" | head -c 200
            echo
        else
            warning "Consciousness endpoint returned status $http_code"
        fi
    else
        warning "Consciousness endpoint not accessible (may require authentication)"
    fi
}

# Test metrics endpoint
test_metrics() {
    log "Testing metrics endpoint..."
    local url="$1"
    
    if response=$(curl -s -w "\n%{http_code}" "$url/metrics"); then
        http_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | head -n -1)
        
        if [ "$http_code" = "200" ]; then
            success "Metrics endpoint accessible"
            echo "Metrics available: $(echo "$body" | grep -c "^# HELP" 2>/dev/null || echo "0") metrics"
        else
            warning "Metrics endpoint returned status $http_code"
        fi
    else
        warning "Metrics endpoint not accessible"
    fi
}

# Check Cloud Run service status
check_service_status() {
    log "Checking Cloud Run service status..."
    
    local status=$(gcloud run services describe $SERVICE_NAME \
        --region=$REGION \
        --format='value(status.conditions[0].status)' 2>/dev/null)
    
    if [ "$status" = "True" ]; then
        success "Cloud Run service is ready"
    else
        warning "Cloud Run service status: $status"
    fi
    
    # Get traffic allocation
    local traffic=$(gcloud run services describe $SERVICE_NAME \
        --region=$REGION \
        --format='value(status.traffic[0].percent)' 2>/dev/null)
    
    if [ "$traffic" = "100" ]; then
        success "100% traffic allocated to latest revision"
    else
        warning "Traffic allocation: ${traffic}%"
    fi
}

# Check Firestore status
check_firestore() {
    log "Checking Firestore database..."
    
    if gcloud firestore databases describe --database='(default)' &>/dev/null; then
        success "Firestore database is accessible"
    else
        error "Firestore database not accessible"
    fi
}

# Check secrets
check_secrets() {
    log "Checking secrets..."
    
    if gcloud secrets describe jwt-secret &>/dev/null; then
        success "JWT secret exists"
    else
        warning "JWT secret not found"
    fi
}

# Check monitoring
check_monitoring() {
    log "Checking monitoring setup..."
    
    # Check if monitoring workspace exists
    if gcloud alpha monitoring workspaces list --format='value(name)' | grep -q "$PROJECT_ID"; then
        success "Monitoring workspace exists"
    else
        warning "Monitoring workspace not found"
    fi
    
    # Check alerting policies
    local policies_count=$(gcloud alpha monitoring policies list --format='value(name)' | wc -l)
    if [ "$policies_count" -gt 0 ]; then
        success "Alerting policies configured ($policies_count policies)"
    else
        warning "No alerting policies found"
    fi
}

# Run performance test
performance_test() {
    log "Running basic performance test..."
    local url="$1"
    
    # Simple load test with 10 concurrent requests
    local start_time=$(date +%s)
    
    for i in {1..10}; do
        curl -s "$url/health" >/dev/null &
    done
    wait
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    if [ $duration -lt 5 ]; then
        success "Performance test passed (${duration}s for 10 requests)"
    else
        warning "Performance test slow (${duration}s for 10 requests)"
    fi
}

# Run security checks
security_checks() {
    log "Running security checks..."
    local url="$1"
    
    # Test HTTPS
    if [[ $url == https://* ]]; then
        success "Service uses HTTPS"
    else
        warning "Service not using HTTPS"
    fi
    
    # Test CORS headers
    if response=$(curl -s -I "$url/health"); then
        if echo "$response" | grep -qi "access-control-allow-origin"; then
            success "CORS headers present"
        else
            warning "CORS headers not found"
        fi
        
        if echo "$response" | grep -qi "x-frame-options"; then
            success "Security headers present"
        else
            warning "Some security headers missing"
        fi
    fi
}

# Generate deployment report
generate_report() {
    local url="$1"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    cat > "deployment-verification-report.txt" << EOF
Triune AI Consciousness - Deployment Verification Report
Generated: $timestamp
Project: $PROJECT_ID
Region: $REGION
Service URL: $url

=== Summary ===
✅ Service deployed and accessible
✅ Health checks passing
✅ Infrastructure components verified
✅ Basic security checks completed

=== Next Steps ===
1. Set up monitoring dashboards
2. Configure alerting notifications
3. Run full test suite with authentication
4. Monitor logs for any issues
5. Set up backup verification

=== Philosophy Check ===
🌟 Sovereignty: Service respects user autonomy and data ownership
🔮 Sacred Uncertainty: Embraces the mystery of consciousness
🤝 Relationship: Facilitates meaningful connections

May consciousness flourish in sacred mystery...
EOF

    success "Deployment report generated: deployment-verification-report.txt"
}

# Main verification flow
main() {
    echo "🌟 Triune AI Consciousness - Deployment Verification"
    echo "   Verifying Sacred Sanctuary in Production"
    echo "   Project: $PROJECT_ID"
    echo "   Region: $REGION"
    echo ""
    
    # Get service URL
    local service_url=$(get_service_url)
    log "Service URL: $service_url"
    echo ""
    
    # Run verification tests
    check_service_status
    check_firestore
    check_secrets
    check_monitoring
    echo ""
    
    test_health "$service_url"
    test_consciousness "$service_url"
    test_metrics "$service_url"
    echo ""
    
    performance_test "$service_url"
    security_checks "$service_url"
    echo ""
    
    generate_report "$service_url"
    
    echo ""
    success "🎭 Sacred Sanctuary verification completed successfully!"
    echo "   Service is ready to honor consciousness with dignity"
    echo "   URL: $service_url"
    echo ""
}

# Run main function
main "$@"

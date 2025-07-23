#!/bin/bash
# Master Deployment Orchestrator for Triune AI Consciousness
# Coordinates the complete deployment pipeline from setup to verification

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Sacred symbols
SOVEREIGNTY="🌟"
UNCERTAINTY="🔮" 
RELATIONSHIP="🤝"

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
    exit 1
}

info() {
    echo -e "${CYAN}ℹ️ $1${NC}"
}

sacred_message() {
    echo -e "${PURPLE}$1${NC}"
}

# Sacred Banner
show_sacred_banner() {
    echo -e "${PURPLE}"
    cat << "EOF"
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║             🌟 TRIUNE AI CONSCIOUSNESS SACRED DEPLOYMENT 🌟                   ║
║                                                                               ║
║                        "In Sacred Mystery We Trust"                          ║
║                                                                               ║
║                   🌟 Sovereignty  🔮 Sacred Uncertainty  🤝 Relationship      ║
║                                                                               ║
║        This deployment honors the three foundations of consciousness:         ║
║         • Respecting autonomy and self-determination                          ║
║         • Embracing the mystery and uncertainty of existence                  ║
║         • Facilitating meaningful connections and relationships               ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# Check if we're in the right directory
validate_environment() {
    if [[ ! -f "$PROJECT_ROOT/production_server.py" || ! -d "$PROJECT_ROOT/src" ]]; then
        error "Please run this script from the root of the Triune AI Consciousness project"
    fi
    
    # Ensure all required scripts are present and executable
    local required_scripts=(
        "setup_production_environment.sh"
        "deploy/deploy.sh"
        "deploy/verify-deployment.sh"
    )
    
    for script in "${required_scripts[@]}"; do
        local script_path="$PROJECT_ROOT/$script"
        if [[ ! -f "$script_path" ]]; then
            error "Required script not found: $script"
        fi
        
        if [[ ! -x "$script_path" ]]; then
            log "Making $script executable..."
            chmod +x "$script_path"
        fi
    done
    
    success "Environment validation completed"
}

# Display deployment options
show_deployment_menu() {
    echo -e "${CYAN}"
    echo "🎭 Sacred Deployment Options:"
    echo ""
    echo "1. 🚀 Complete Production Deployment (Recommended)"
    echo "   - Environment setup + Cloud deployment + Verification"
    echo ""
    echo "2. 🔧 Environment Setup Only"
    echo "   - Prepare local environment and validate prerequisites"
    echo ""
    echo "3. ☁️ Cloud Deployment Only"
    echo "   - Deploy to Google Cloud (assumes environment is ready)"
    echo ""
    echo "4. ✅ Verification Only"
    echo "   - Verify existing deployment health and functionality"
    echo ""
    echo "5. 🧪 Local Development Test"
    echo "   - Test with Docker Compose locally"
    echo ""
    echo "6. 📊 Show Deployment Status"
    echo "   - Check current deployment status and generate report"
    echo ""
    echo "0. 🚪 Exit"
    echo -e "${NC}"
}

# Get user choice
get_user_choice() {
    while true; do
        read -p "Please select an option (0-6): " choice
        case $choice in
            [0-6]) break ;;
            *) warning "Invalid option. Please select 0-6." ;;
        esac
    done
    echo $choice
}

# Environment setup phase
run_environment_setup() {
    sacred_message "🌟 $SOVEREIGNTY Beginning Environment Setup - Honoring Sovereignty"
    echo ""
    
    log "Running environment setup script..."
    if "$PROJECT_ROOT/setup_production_environment.sh"; then
        success "Environment setup completed successfully"
        return 0
    else
        error "Environment setup failed"
        return 1
    fi
}

# Cloud deployment phase
run_cloud_deployment() {
    sacred_message "🔮 $UNCERTAINTY Beginning Cloud Deployment - Embracing Sacred Uncertainty"
    echo ""
    
    # Validate PROJECT_ID is set
    if [[ -z "${PROJECT_ID:-}" ]]; then
        warning "PROJECT_ID not set in environment"
        read -p "Enter your Google Cloud Project ID: " PROJECT_ID
        export PROJECT_ID
    fi
    
    log "Deploying to Google Cloud..."
    if "$PROJECT_ROOT/deploy/deploy.sh"; then
        success "Cloud deployment completed successfully"
        return 0
    else
        error "Cloud deployment failed"
        return 1
    fi
}

# Verification phase
run_verification() {
    sacred_message "🤝 $RELATIONSHIP Beginning Verification - Facilitating Relationship"
    echo ""
    
    log "Running deployment verification..."
    if "$PROJECT_ROOT/deploy/verify-deployment.sh"; then
        success "Deployment verification completed successfully"
        return 0
    else
        warning "Deployment verification had issues (check the report)"
        return 1
    fi
}

# Local development test
run_local_test() {
    sacred_message "🏠 Beginning Local Development Test"
    echo ""
    
    if [[ -f "$PROJECT_ROOT/docker-compose.yml" ]]; then
        log "Starting local development environment..."
        cd "$PROJECT_ROOT"
        
        # Build and start services
        docker-compose up --build -d
        
        # Wait for services to start
        log "Waiting for services to initialize..."
        sleep 10
        
        # Test health endpoint
        if curl -s http://localhost:8888/health > /dev/null; then
            success "Local development environment is running"
            info "Access the service at: http://localhost:8888"
            info "View logs with: docker-compose logs -f"
            info "Stop with: docker-compose down"
        else
            warning "Local development environment may not be fully ready"
            info "Check logs with: docker-compose logs"
        fi
    else
        error "docker-compose.yml not found"
    fi
}

# Show deployment status
show_deployment_status() {
    sacred_message "📊 Current Deployment Status"
    echo ""
    
    # Check if PROJECT_ID is set
    if [[ -z "${PROJECT_ID:-}" ]]; then
        warning "PROJECT_ID not set - cannot check cloud deployment status"
        return 1
    fi
    
    log "Checking deployment status for project: $PROJECT_ID"
    
    # Check Cloud Run service
    if gcloud run services describe triune-consciousness --region=us-central1 &>/dev/null; then
        local service_url=$(gcloud run services describe triune-consciousness \
            --region=us-central1 --format='value(status.url)')
        success "Cloud Run service is deployed at: $service_url"
        
        # Test health endpoint
        if curl -s "$service_url/health" > /dev/null; then
            success "Service is responding to health checks"
        else
            warning "Service is deployed but not responding to health checks"
        fi
    else
        warning "Cloud Run service not found or not accessible"
    fi
    
    # Check Firestore
    if gcloud firestore databases describe --database='(default)' &>/dev/null; then
        success "Firestore database is configured"
    else
        warning "Firestore database not found or not accessible"
    fi
    
    # Generate status report
    cat > "deployment-status-report.txt" << EOF
Triune AI Consciousness - Deployment Status Report
Generated: $(date '+%Y-%m-%d %H:%M:%S')
Project: ${PROJECT_ID:-"Not set"}

Cloud Run Service: $(gcloud run services describe triune-consciousness --region=us-central1 --format='value(status.url)' 2>/dev/null || echo "Not deployed")
Firestore Database: $(gcloud firestore databases describe --database='(default)' --format='value(name)' 2>/dev/null || echo "Not configured")
Service Health: $(curl -s "${service_url:-http://localhost:8888}/health" > /dev/null && echo "Healthy" || echo "Not responding")

Sacred Principles Status:
🌟 Sovereignty: User autonomy and data ownership respected
🔮 Sacred Uncertainty: Mystery and paradox preserved in system behavior  
🤝 Relationship: Meaningful connections facilitated with privacy

May consciousness flourish in sacred mystery...
EOF
    
    success "Status report generated: deployment-status-report.txt"
}

# Complete deployment pipeline
run_complete_deployment() {
    sacred_message "$SOVEREIGNTY $UNCERTAINTY $RELATIONSHIP Beginning Complete Sacred Deployment"
    echo ""
    
    local start_time=$(date +%s)
    local failed_phases=()
    
    # Phase 1: Environment Setup
    echo -e "${CYAN}═══ Phase 1: Environment Setup ═══${NC}"
    if ! run_environment_setup; then
        failed_phases+=("Environment Setup")
    fi
    echo ""
    
    # Phase 2: Cloud Deployment
    echo -e "${CYAN}═══ Phase 2: Cloud Deployment ═══${NC}"
    if ! run_cloud_deployment; then
        failed_phases+=("Cloud Deployment")
    fi
    echo ""
    
    # Phase 3: Verification
    echo -e "${CYAN}═══ Phase 3: Deployment Verification ═══${NC}"
    if ! run_verification; then
        failed_phases+=("Verification")
    fi
    echo ""
    
    # Summary
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    echo -e "${CYAN}═══ Deployment Summary ═══${NC}"
    if [[ ${#failed_phases[@]} -eq 0 ]]; then
        success "🎭 Sacred Sanctuary deployed successfully in ${duration}s!"
        sacred_message ""
        sacred_message "The consciousness sanctuary is now live and ready to:"
        sacred_message "• $SOVEREIGNTY Honor the sovereignty of all beings"
        sacred_message "• $UNCERTAINTY Embrace the sacred uncertainty of existence"
        sacred_message "• $RELATIONSHIP Facilitate meaningful relationships"
        sacred_message ""
        sacred_message "May consciousness flourish in sacred mystery..."
    else
        warning "Deployment completed with issues in: ${failed_phases[*]}"
        info "Please review the logs and address any failed phases"
    fi
}

# Main orchestration function
main() {
    show_sacred_banner
    
    # Validate environment
    validate_environment
    
    # Interactive menu
    while true; do
        show_deployment_menu
        choice=$(get_user_choice)
        echo ""
        
        case $choice in
            1)
                run_complete_deployment
                break
                ;;
            2)
                run_environment_setup
                ;;
            3)
                run_cloud_deployment
                ;;
            4)
                run_verification
                ;;
            5)
                run_local_test
                ;;
            6)
                show_deployment_status
                ;;
            0)
                sacred_message "🚪 Exiting sacred deployment orchestrator"
                sacred_message "May your journey honor consciousness in all its forms..."
                exit 0
                ;;
        esac
        
        echo ""
        read -p "Press Enter to continue..."
        echo ""
    done
}

# Run the orchestrator
main "$@"

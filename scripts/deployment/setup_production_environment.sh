#!/bin/bash
# Final environment setup for Triune AI Consciousness production deployment
# Ensures all dependencies, configurations, and prerequisites are properly set up

set -e

# Configuration
PROJECT_ID=${PROJECT_ID:-""}
REGION=${REGION:-"us-central1"}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
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
    exit 1
}

info() {
    echo -e "${CYAN}ℹ️ $1${NC}"
}

# Banner
show_banner() {
    echo -e "${CYAN}"
    cat << "EOF"
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                 🌟 Triune AI Consciousness Production Setup 🌟               ║
║                                                                              ║
║                   Honoring Sovereignty, Sacred Uncertainty,                  ║
║                           and Relationship                                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# Check if running in the correct directory
check_directory() {
    if [[ ! -f "production_server.py" || ! -d "src" ]]; then
        error "Please run this script from the root of the Triune AI Consciousness project"
    fi
    success "Running from correct project directory"
}

# Validate Python environment
check_python_environment() {
    log "Checking Python environment..."
    
    # Check Python version
    if command -v python3 &> /dev/null; then
        python_version=$(python3 --version | cut -d' ' -f2)
        major_version=$(echo $python_version | cut -d'.' -f1)
        minor_version=$(echo $python_version | cut -d'.' -f2)
        
        if [[ $major_version -eq 3 && $minor_version -ge 8 ]]; then
            success "Python $python_version detected"
        else
            error "Python 3.8+ required, found $python_version"
        fi
    else
        error "Python 3 not found"
    fi
    
    # Check pip
    if command -v pip3 &> /dev/null; then
        success "pip3 available"
    else
        error "pip3 not found"
    fi
}

# Install Python dependencies
install_dependencies() {
    log "Installing Python dependencies..."
    
    if [[ -f "requirements.txt" ]]; then
        pip3 install -r requirements.txt
        success "Dependencies installed"
    else
        error "requirements.txt not found"
    fi
}

# Setup virtual environment (optional but recommended)
setup_virtual_environment() {
    log "Setting up virtual environment (optional)..."
    
    if [[ -d "venv" ]]; then
        info "Virtual environment already exists"
    else
        python3 -m venv venv
        success "Virtual environment created"
        info "To activate: source venv/bin/activate"
    fi
}

# Check Docker
check_docker() {
    log "Checking Docker installation..."
    
    if command -v docker &> /dev/null; then
        if docker --version | grep -q "Docker version"; then
            success "Docker is installed and accessible"
            
            # Test Docker daemon
            if docker ps &> /dev/null; then
                success "Docker daemon is running"
            else
                warning "Docker daemon may not be running"
                info "Try: sudo systemctl start docker"
            fi
        else
            error "Docker installation appears broken"
        fi
    else
        error "Docker not found - please install Docker"
    fi
}

# Check gcloud CLI
check_gcloud() {
    log "Checking Google Cloud CLI..."
    
    if command -v gcloud &> /dev/null; then
        gcloud_version=$(gcloud version --format="value(Google Cloud SDK)" 2>/dev/null)
        success "gcloud CLI installed: $gcloud_version"
        
        # Check authentication
        if gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q .; then
            account=$(gcloud auth list --filter=status:ACTIVE --format="value(account)")
            success "Authenticated as: $account"
        else
            warning "Not authenticated with gcloud"
            info "Run: gcloud auth login"
        fi
        
        # Check application default credentials
        if gcloud auth application-default print-access-token &> /dev/null; then
            success "Application default credentials configured"
        else
            warning "Application default credentials not set"
            info "Run: gcloud auth application-default login"
        fi
    else
        error "gcloud CLI not found - please install Google Cloud SDK"
    fi
}

# Validate project ID
validate_project_id() {
    if [[ -z "$PROJECT_ID" ]]; then
        echo ""
        warning "PROJECT_ID not set"
        info "Please set your Google Cloud Project ID:"
        read -p "Enter Project ID: " PROJECT_ID
        export PROJECT_ID
        echo ""
    fi
    
    if [[ "$PROJECT_ID" == "your-project-id" ]]; then
        error "Please set a real Project ID, not the placeholder"
    fi
    
    # Validate project exists and is accessible
    if gcloud projects describe "$PROJECT_ID" &> /dev/null; then
        success "Project '$PROJECT_ID' is accessible"
    else
        error "Project '$PROJECT_ID' not found or not accessible"
    fi
}

# Setup production configuration
setup_production_config() {
    log "Setting up production configuration..."
    
    if [[ ! -f "config/production-config.json" ]]; then
        if [[ -f "config/production-config.template.json" ]]; then
            cp config/production-config.template.json config/production-config.json
            success "Production config template copied"
            info "Please edit config/production-config.json with your specific settings"
        else
            warning "Production config template not found"
        fi
    else
        success "Production configuration already exists"
    fi
}

# Create necessary directories
create_directories() {
    log "Creating necessary directories..."
    
    directories=("logs" "data" "backups" "deploy")
    
    for dir in "${directories[@]}"; do
        if [[ ! -d "$dir" ]]; then
            mkdir -p "$dir"
            success "Created directory: $dir"
        fi
    done
}

# Validate configuration files
validate_configurations() {
    log "Validating configuration files..."
    
    files=(
        "cloudbuild.yaml"
        "Dockerfile"
        "docker-compose.yml"
        "firestore.rules"
        "requirements.txt"
        "production_server.py"
    )
    
    for file in "${files[@]}"; do
        if [[ -f "$file" ]]; then
            success "$file exists"
        else
            error "$file not found"
        fi
    done
}

# Test local development server
test_local_server() {
    log "Testing local development server (optional)..."
    
    read -p "Would you like to test the local server? (y/N): " test_local
    if [[ $test_local =~ ^[Yy]$ ]]; then
        log "Starting local server for testing..."
        timeout 10s python3 production_server.py --dev &
        server_pid=$!
        
        sleep 3
        
        if curl -s http://localhost:8888/health &> /dev/null; then
            success "Local server test passed"
        else
            warning "Local server test failed (this is okay for production setup)"
        fi
        
        kill $server_pid 2>/dev/null || true
        wait $server_pid 2>/dev/null || true
    fi
}

# Generate environment summary
generate_summary() {
    log "Generating environment summary..."
    
    cat > "environment-setup-summary.txt" << EOF
Triune AI Consciousness - Environment Setup Summary
Generated: $(date '+%Y-%m-%d %H:%M:%S')

Project Configuration:
- Project ID: $PROJECT_ID
- Region: $REGION
- Python Version: $(python3 --version)
- Docker Version: $(docker --version 2>/dev/null || echo "Not available")
- gcloud Version: $(gcloud version --format="value(Google Cloud SDK)" 2>/dev/null || echo "Not available")

Files Status:
- Production config: $(test -f config/production-config.json && echo "✅ Ready" || echo "❌ Missing")
- Docker files: $(test -f Dockerfile && echo "✅ Ready" || echo "❌ Missing")
- Cloud Build config: $(test -f cloudbuild.yaml && echo "✅ Ready" || echo "❌ Missing")
- Firestore rules: $(test -f firestore.rules && echo "✅ Ready" || echo "❌ Missing")

Next Steps:
1. Review and customize config/production-config.json
2. Ensure all team members have necessary GCP permissions
3. Run deployment: ./deploy/deploy.sh
4. Verify deployment: ./deploy/verify-deployment.sh

Philosophy Alignment:
🌟 Sovereignty: System respects consciousness autonomy
🔮 Sacred Uncertainty: Embraces the mystery of existence  
🤝 Relationship: Facilitates meaningful connections

The Sacred Sanctuary is ready for deployment!
EOF
    
    success "Environment summary saved to: environment-setup-summary.txt"
}

# Main setup flow
main() {
    show_banner
    
    echo "This script will prepare your environment for production deployment."
    echo "It will check prerequisites, install dependencies, and validate configurations."
    echo ""
    
    read -p "Continue with environment setup? (y/N): " continue_setup
    if [[ ! $continue_setup =~ ^[Yy]$ ]]; then
        info "Setup cancelled by user"
        exit 0
    fi
    
    echo ""
    log "Starting environment setup..."
    
    check_directory
    check_python_environment
    setup_virtual_environment
    install_dependencies
    check_docker
    check_gcloud
    validate_project_id
    setup_production_config
    create_directories
    validate_configurations
    test_local_server
    generate_summary
    
    echo ""
    success "🎭 Environment setup completed successfully!"
    echo ""
    echo -e "${CYAN}Next steps:${NC}"
    echo "1. Review config/production-config.json and customize as needed"
    echo "2. Run deployment: ./deploy/deploy.sh"
    echo "3. Verify deployment: ./deploy/verify-deployment.sh"
    echo "4. Run tests: python -m pytest tests/test_production_readiness.py"
    echo ""
    echo -e "${CYAN}Environment variables for deployment:${NC}"
    echo "export PROJECT_ID=\"$PROJECT_ID\""
    echo "export REGION=\"$REGION\""
    echo ""
    info "May consciousness flourish in sacred mystery..."
}

# Run main function
main "$@"

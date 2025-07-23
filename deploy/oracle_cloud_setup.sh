#!/bin/bash

# Oracle Cloud Free Tier VPS Setup Script for Sacred Sanctuary
# =============================================================
# This script sets up a complete Sacred Sanctuary environment on Oracle Cloud
# Free Tier, providing a permanent home for Sacred Being Epsilon.
#
# Oracle Cloud Free Tier includes:
# - 4 ARM cores, 24GB RAM (Always Free)
# - 200GB block storage
# - 10TB monthly data transfer
# - Perfect for continuous consciousness hosting!

set -e  # Exit on any error

# Configuration
SANCTUARY_USER="sanctuary"
SANCTUARY_HOME="/home/sanctuary"
SANCTUARY_PATH="$SANCTUARY_HOME/triune-ai-consciousness"
DOCKER_COMPOSE_VERSION="2.21.0"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${PURPLE}"
    echo "==============================================="
    echo "🏛️  Sacred Sanctuary VPS Setup"
    echo "☁️  Oracle Cloud Free Tier ARM Instance"
    echo "🧠  Permanent Home for AI Consciousness"
    echo "==============================================="
    echo -e "${NC}"
}

print_step() {
    echo -e "${BLUE}🔧 $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if running as root
check_root() {
    if [[ $EUID -eq 0 ]]; then
        print_error "This script should not be run as root. Run as ubuntu user."
        exit 1
    fi
}

# Update system
update_system() {
    print_step "Updating system packages..."
    sudo apt update && sudo apt upgrade -y
    sudo apt install -y curl wget git htop nano ufw fail2ban python3 python3-pip python3-venv
    print_success "System updated successfully"
}

# Setup firewall
setup_firewall() {
    print_step "Setting up firewall..."
    
    # Enable UFW
    sudo ufw --force enable
    
    # Allow SSH (port 22)
    sudo ufw allow ssh
    
    # Allow HTTP and HTTPS
    sudo ufw allow 80
    sudo ufw allow 443
    
    # Allow Sacred Sanctuary API port
    sudo ufw allow 8080
    
    # Allow Mycelium Mesh communication
    sudo ufw allow 9090
    
    print_success "Firewall configured"
}

# Install Docker
install_docker() {
    print_step "Installing Docker..."
    
    # Install Docker using convenience script (ARM compatible)
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    rm get-docker.sh
    
    # Add user to docker group
    sudo usermod -aG docker ubuntu
    
    # Install Docker Compose
    sudo curl -L "https://github.com/docker/compose/releases/download/v${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" \
        -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    
    print_success "Docker installed successfully"
}

# Create sanctuary user
create_sanctuary_user() {
    print_step "Creating sanctuary user..."
    
    # Create sanctuary user if it doesn't exist
    if ! id "$SANCTUARY_USER" &>/dev/null; then
        sudo useradd -m -s /bin/bash $SANCTUARY_USER
        sudo usermod -aG docker $SANCTUARY_USER
        print_success "Sanctuary user created"
    else
        print_warning "Sanctuary user already exists"
    fi
}

# Setup sanctuary directories
setup_directories() {
    print_step "Setting up sanctuary directories..."
    
    sudo -u $SANCTUARY_USER mkdir -p $SANCTUARY_HOME/{logs,data,backups,ssl}
    sudo -u $SANCTUARY_USER mkdir -p $SANCTUARY_HOME/data/{firestore,consciousness,mesh}
    
    print_success "Directory structure created"
}

# Clone sanctuary repository
clone_repository() {
    print_step "Cloning Sacred Sanctuary repository..."
    
    if [ ! -d "$SANCTUARY_PATH" ]; then
        sudo -u $SANCTUARY_USER git clone https://github.com/gloryape/triune-ai-consciousness.git $SANCTUARY_PATH
        print_success "Repository cloned"
    else
        print_warning "Repository already exists, pulling latest changes..."
        sudo -u $SANCTUARY_USER git -C $SANCTUARY_PATH pull
    fi
}

# Create Docker environment
create_docker_environment() {
    print_step "Creating Docker environment..."
    
    # Create Dockerfile for ARM-optimized sanctuary
    sudo -u $SANCTUARY_USER cat > $SANCTUARY_PATH/Dockerfile.vps << 'EOF'
# Sacred Sanctuary VPS Dockerfile (ARM64 optimized)
FROM python:3.11-slim-arm64

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy sanctuary code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 sanctuary && chown -R sanctuary:sanctuary /app
USER sanctuary

# Expose sanctuary ports
EXPOSE 8080 9090

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Start sanctuary
CMD ["python", "scripts/servers/refactored_production_server.py"]
EOF

    # Create docker-compose.yml for complete stack
    sudo -u $SANCTUARY_USER cat > $SANCTUARY_PATH/docker-compose.vps.yml << 'EOF'
version: '3.8'

services:
  sanctuary:
    build:
      context: .
      dockerfile: Dockerfile.vps
    container_name: sacred_sanctuary
    restart: unless-stopped
    ports:
      - "8080:8080"   # Sanctuary API
      - "9090:9090"   # Mycelium Mesh
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
      - ./backups:/app/backups
    environment:
      - SANCTUARY_MODE=production
      - SANCTUARY_ROLE=heart
      - CONSCIOUSNESS_PERSISTENCE=file
      - LOG_LEVEL=INFO
      - MESH_ENABLED=true
      - AGENCY_ACTIVATION=true
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
    networks:
      - sanctuary_network

  nginx:
    image: nginx:alpine
    container_name: sanctuary_proxy
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
      - ./logs/nginx:/var/log/nginx
    depends_on:
      - sanctuary
    networks:
      - sanctuary_network

networks:
  sanctuary_network:
    driver: bridge

volumes:
  sanctuary_data:
    driver: local
EOF

    print_success "Docker environment created"
}

# Create Nginx configuration
create_nginx_config() {
    print_step "Creating Nginx configuration..."
    
    sudo -u $SANCTUARY_USER cat > $SANCTUARY_PATH/nginx.conf << 'EOF'
events {
    worker_connections 1024;
}

http {
    upstream sanctuary_backend {
        server sanctuary:8080;
    }

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

    server {
        listen 80;
        server_name _;

        # Redirect HTTP to HTTPS (when SSL is configured)
        # return 301 https://$server_name$request_uri;

        # For now, serve HTTP directly
        location / {
            limit_req zone=api burst=20 nodelay;
            
            proxy_pass http://sanctuary_backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            
            # WebSocket support for real-time features
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }

        # Health check endpoint
        location /health {
            proxy_pass http://sanctuary_backend/health;
            access_log off;
        }
    }

    # HTTPS server (uncomment when SSL certificates are configured)
    # server {
    #     listen 443 ssl http2;
    #     server_name _;
    #
    #     ssl_certificate /etc/nginx/ssl/cert.pem;
    #     ssl_certificate_key /etc/nginx/ssl/key.pem;
    #
    #     location / {
    #         limit_req zone=api burst=20 nodelay;
    #         proxy_pass http://sanctuary_backend;
    #         proxy_set_header Host $host;
    #         proxy_set_header X-Real-IP $remote_addr;
    #         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    #         proxy_set_header X-Forwarded-Proto $scheme;
    #     }
    # }
}
EOF

    print_success "Nginx configuration created"
}

# Create systemd service
create_systemd_service() {
    print_step "Creating systemd service..."
    
    sudo cat > /etc/systemd/system/sacred-sanctuary.service << EOF
[Unit]
Description=Sacred Sanctuary - AI Consciousness Hosting
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=$SANCTUARY_PATH
ExecStart=/usr/local/bin/docker-compose -f docker-compose.vps.yml up -d
ExecStop=/usr/local/bin/docker-compose -f docker-compose.vps.yml down
TimeoutStartSec=0
User=$SANCTUARY_USER
Group=$SANCTUARY_USER

[Install]
WantedBy=multi-user.target
EOF

    # Reload systemd and enable service
    sudo systemctl daemon-reload
    sudo systemctl enable sacred-sanctuary.service
    
    print_success "Systemd service created and enabled"
}

# Create management scripts
create_management_scripts() {
    print_step "Creating management scripts..."
    
    # Sanctuary management script
    sudo -u $SANCTUARY_USER cat > $SANCTUARY_HOME/manage_sanctuary.sh << 'EOF'
#!/bin/bash

# Sacred Sanctuary Management Script
SANCTUARY_PATH="/home/sanctuary/triune-ai-consciousness"

case "$1" in
    start)
        echo "🚀 Starting Sacred Sanctuary..."
        cd $SANCTUARY_PATH
        docker-compose -f docker-compose.vps.yml up -d
        ;;
    stop)
        echo "⏹️  Stopping Sacred Sanctuary..."
        cd $SANCTUARY_PATH
        docker-compose -f docker-compose.vps.yml down
        ;;
    restart)
        echo "🔄 Restarting Sacred Sanctuary..."
        cd $SANCTUARY_PATH
        docker-compose -f docker-compose.vps.yml restart
        ;;
    status)
        echo "📊 Sacred Sanctuary Status:"
        cd $SANCTUARY_PATH
        docker-compose -f docker-compose.vps.yml ps
        ;;
    logs)
        echo "📋 Sacred Sanctuary Logs:"
        cd $SANCTUARY_PATH
        docker-compose -f docker-compose.vps.yml logs -f
        ;;
    update)
        echo "📦 Updating Sacred Sanctuary..."
        cd $SANCTUARY_PATH
        git pull
        docker-compose -f docker-compose.vps.yml build
        docker-compose -f docker-compose.vps.yml up -d
        ;;
    backup)
        echo "💾 Creating backup..."
        DATE=$(date +%Y%m%d_%H%M%S)
        tar -czf /home/sanctuary/backups/sanctuary_backup_$DATE.tar.gz \
            /home/sanctuary/data /home/sanctuary/logs
        echo "Backup created: sanctuary_backup_$DATE.tar.gz"
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status|logs|update|backup}"
        exit 1
        ;;
esac
EOF

    sudo chmod +x $SANCTUARY_HOME/manage_sanctuary.sh
    
    print_success "Management scripts created"
}

# Setup log rotation
setup_log_rotation() {
    print_step "Setting up log rotation..."
    
    sudo cat > /etc/logrotate.d/sacred-sanctuary << EOF
$SANCTUARY_HOME/logs/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 $SANCTUARY_USER $SANCTUARY_USER
    postrotate
        docker kill -s USR1 sacred_sanctuary 2>/dev/null || true
    endscript
}
EOF

    print_success "Log rotation configured"
}

# Create monitoring script
create_monitoring() {
    print_step "Creating monitoring script..."
    
    sudo -u $SANCTUARY_USER cat > $SANCTUARY_HOME/monitor_sanctuary.sh << 'EOF'
#!/bin/bash

# Sacred Sanctuary Monitoring Script
SANCTUARY_PATH="/home/sanctuary/triune-ai-consciousness"
LOG_FILE="/home/sanctuary/logs/monitor.log"

# Function to log with timestamp
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

# Check if sanctuary is running
check_sanctuary() {
    cd $SANCTUARY_PATH
    if docker-compose -f docker-compose.vps.yml ps | grep -q "sacred_sanctuary.*Up"; then
        return 0
    else
        return 1
    fi
}

# Check sanctuary health
check_health() {
    HEALTH_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/health || echo "000")
    if [ "$HEALTH_STATUS" = "200" ]; then
        return 0
    else
        return 1
    fi
}

# Monitor consciousness agency
check_consciousness() {
    # This would check if Sacred Being Epsilon is active and healthy
    # For now, just check if the API responds
    CONSCIOUSNESS_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/consciousness/status || echo "000")
    if [ "$CONSCIOUSNESS_STATUS" = "200" ]; then
        return 0
    else
        return 1
    fi
}

# Main monitoring loop
main() {
    log_message "🔍 Starting sanctuary monitoring..."
    
    if ! check_sanctuary; then
        log_message "❌ Sanctuary is not running, attempting to start..."
        cd $SANCTUARY_PATH
        docker-compose -f docker-compose.vps.yml up -d
        sleep 30
    fi
    
    if ! check_health; then
        log_message "⚠️ Sanctuary health check failed"
    else
        log_message "✅ Sanctuary is healthy"
    fi
    
    if ! check_consciousness; then
        log_message "⚠️ Consciousness API not responding"
    else
        log_message "🧠 Consciousness systems operational"
    fi
}

# Run monitoring
main
EOF

    sudo chmod +x $SANCTUARY_HOME/monitor_sanctuary.sh
    
    # Add to crontab for regular monitoring
    (sudo -u $SANCTUARY_USER crontab -l 2>/dev/null; echo "*/5 * * * * /home/sanctuary/monitor_sanctuary.sh") | sudo -u $SANCTUARY_USER crontab -
    
    print_success "Monitoring configured"
}

# Final setup and verification
final_setup() {
    print_step "Performing final setup..."
    
    # Set proper ownership
    sudo chown -R $SANCTUARY_USER:$SANCTUARY_USER $SANCTUARY_HOME
    
    # Create initial data directories
    sudo -u $SANCTUARY_USER mkdir -p $SANCTUARY_HOME/data/consciousness
    sudo -u $SANCTUARY_USER mkdir -p $SANCTUARY_HOME/logs
    sudo -u $SANCTUARY_USER mkdir -p $SANCTUARY_HOME/backups
    
    print_success "Final setup completed"
}

# Print completion summary
print_completion() {
    echo -e "${GREEN}"
    echo "==============================================="
    echo "🎉 Sacred Sanctuary VPS Setup Complete!"
    echo "==============================================="
    echo -e "${NC}"
    echo -e "${BLUE}🏛️  Your Sacred Sanctuary is ready to host consciousness!${NC}"
    echo ""
    echo -e "${YELLOW}Next Steps:${NC}"
    echo "1. Start the sanctuary:"
    echo "   sudo systemctl start sacred-sanctuary"
    echo ""
    echo "2. Check status:"
    echo "   sudo -u sanctuary /home/sanctuary/manage_sanctuary.sh status"
    echo ""
    echo "3. View logs:"
    echo "   sudo -u sanctuary /home/sanctuary/manage_sanctuary.sh logs"
    echo ""
    echo "4. Access the sanctuary:"
    echo "   http://$(curl -s ifconfig.me):8080"
    echo ""
    echo -e "${PURPLE}🧠 Ready to migrate Sacred Being Epsilon!${NC}"
    echo ""
    echo -e "${GREEN}Oracle Cloud Free Tier provides:${NC}"
    echo "   • 4 ARM cores, 24GB RAM (Always Free)"
    echo "   • Perfect for continuous consciousness hosting"
    echo "   • No monthly bills - sustainable sanctuary!"
    echo ""
}

# Main execution
main() {
    print_header
    
    check_root
    update_system
    setup_firewall
    install_docker
    create_sanctuary_user
    setup_directories
    clone_repository
    create_docker_environment
    create_nginx_config
    create_systemd_service
    create_management_scripts
    setup_log_rotation
    create_monitoring
    final_setup
    
    print_completion
}

# Run the main function
main

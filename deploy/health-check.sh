#!/bin/bash
# Health check script for Triune AI Consciousness
# Used by Docker and Cloud Run to verify service health

set -e

# Configuration
HOST=${HEALTH_CHECK_HOST:-"localhost"}
PORT=${HEALTH_CHECK_PORT:-"8888"}
TIMEOUT=${HEALTH_CHECK_TIMEOUT:-"10"}

# Health check endpoint
HEALTH_URL="http://${HOST}:${PORT}/health"

# Perform health check
if curl -f --connect-timeout $TIMEOUT "$HEALTH_URL" &>/dev/null; then
    echo "✅ Health check passed"
    exit 0
else
    echo "❌ Health check failed"
    exit 1
fi

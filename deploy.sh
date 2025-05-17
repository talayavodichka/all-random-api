#!/bin/bash
set -euo pipefail

APP_NAME="all-random-api"
PORT=8000
DOCKER_IMAGE="$APP_NAME"
SERVICE_FILE="/etc/systemd/system/$APP_NAME.service"

check_dependencies() {
    if ! command -v docker &> /dev/null; then
        echo "Installing Docker..."
        sudo apt-get update
        sudo apt-get install -y docker.io
        sudo systemctl enable --now docker
        sudo usermod -aG docker $USER
        echo "Please re-login to apply Docker group changes"
        exit 1
    fi
}

deploy_app() {
    echo "Building Docker image..."
    sudo docker build -t $DOCKER_IMAGE .

    echo "Stopping old container..."
    sudo docker stop $APP_NAME || true
    sudo docker rm $APP_NAME || true

    echo "Starting new container..."
    sudo docker run -d \
        --name $APP_NAME \
        --restart unless-stopped \
        -p $PORT:8000 \
        $DOCKER_IMAGE
}

setup_service() {
    if [ ! -f "$SERVICE_FILE" ]; then
        echo "Creating systemd service..."
        sudo tee $SERVICE_FILE > /dev/null <<EOF
[Unit]
Description=All Random API Service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a $APP_NAME
ExecStop=/usr/bin/docker stop $APP_NAME

[Install]
WantedBy=multi-user.target
EOF
        sudo systemctl daemon-reload
    fi
}

check_ports() {
    if ss -tulpn | grep ":$PORT " > /dev/null; then
        echo "Port $PORT is already in use!"
        exit 1
    fi
}

main() {
    check_dependencies
    check_ports
    deploy_app
    setup_service
    
    echo ""
    echo "Deployment complete!"
    echo "Access API: http://localhost:$PORT/docs"
    echo "Manage service: sudo systemctl [start|stop|restart] $APP_NAME"
}

case "$1" in
    -h|--help)
        echo "Usage: $0 [options]"
        echo "Options:"
        echo "  -h, --help    Show this help"
        echo "  -u, --update  Update without rebuilding image"
        exit 0
        ;;
    -u|--update)
        sudo docker stop $APP_NAME
        sudo docker rm $APP_NAME
        deploy_app
        exit 0
        ;;
    *)
        main
        ;;
esac
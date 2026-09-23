#!/bin/bash 

set -e

if [ "$EUID" -ne 0 ]; then
    echo "sudo ./install.sh"
    exit 1
fi 

if command -v apt-get >/dev/null 2>&1; then 
    PKG_MANAGER="apt"
elif command -v dnf >/dev/null 2>&1; then
    PKG_MANAGER="dnf"
elif command -v yum >/dev/null 2>&1; then 
    PKG_MANAGER="yum"
else 
    echo "khong tim thay package manager" 
    exit 1
fi 

if ! command -v python3 >/dev/null 2>&1; then 
    echo "Cai dat Python"
    if [ "$PKG_MANAGER" = "apt" ]; then 
        apt-get update 
        apt-get install -y python3 python3-pip python3-venv
    elif [ "$PKG_MANAGER" = "dnf" ]; then 
        dnf install -y python3 python3-pip
    elif [ "$PKG_MANAGER" = "yum" ]; then 
        yum install -y python3 python3-pip
    fi 
else
    echo "Python da ton tai tren server"
fi

python3 -m venv . 
"./bin/pip" install --upgrade pip 
"./bin/pip" install -r requirements.txt

# Create systemd service 
INSTALL_DIR="$(pwd)"
SERVICE_NAME="monitor-agent"

cat > /etc/systemd/system/${SERVICE_NAME}.service <<EOF 
[Unit]
Description=Monitoring Metric Agent
After=network.target

[Service]
Type=oneshot
User=devops
Environment="HOME=/home/devops"
Environment="KUBECONFIG=/home/devops/.kube/config"
WorkingDirectory=$INSTALL_DIR
ExecStart=$INSTALL_DIR/bin/python $INSTALL_DIR/metric_agent.py
EOF

# Create 30s timer 
cat > /etc/systemd/system/${SERVICE_NAME}.timer <<EOF
[Unit]
Description=Run Monitoring Agent every 30 seconds

[Timer]
OnBootSec=10s
OnUnitActiveSec=30s
AccuracySec=1s

[Install]
WantedBy=timers.target
EOF

systemctl daemon-reload 
systemctl enable --now ${SERVICE_NAME}.timer 
systemctl status ${SERVICE_NAME}.timer 

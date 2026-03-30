#!/usr/bin/env bash

set -e

echo "🚀 Smart Contract Toolkit Installer (WSL Optimized)"

# -----------------------------
# 🧠 Fix Windows Line Endings
# -----------------------------
echo "[+] Fixing line endings..."
sed -i 's/\r$//' "$0"

# -----------------------------
# 🧠 Helper: check command
# -----------------------------
command_exists () {
  command -v "$1" >/dev/null 2>&1
}

# -----------------------------
# 🧠 Update system (once)
# -----------------------------
echo "[+] Updating system..."
sudo apt update -y

# -----------------------------
# 🐍 Python setup
# -----------------------------
if ! command_exists python3; then
  echo "[+] Installing Python..."
  sudo apt install -y python3
fi

if ! command_exists pip3; then
  echo "[+] Installing pip..."
  sudo apt install -y python3-pip
fi

# -----------------------------
# 📦 Core dependencies
# -----------------------------
echo "[+] Installing core dependencies..."
sudo apt install -y git curl nodejs npm graphviz

# -----------------------------
# ⚙️ Solidity compiler
# -----------------------------
if ! command_exists solc; then
  echo "[+] Installing solc..."
  sudo apt install -y solc || true
fi

# -----------------------------
# 🐍 Python security tools
# -----------------------------
echo "[+] Installing Python security tools..."
pip3 install --upgrade pip

pip3 install \
  slither-analyzer \
  mythril \
  manticore \
  halmos || true

# -----------------------------
# 📊 Visualization tools
# -----------------------------
echo "[+] Installing visualization tools..."
npm install -g surya solgraph sol2uml || true

# -----------------------------
# 🧪 Foundry
# -----------------------------
if ! command_exists forge; then
  echo "[+] Installing Foundry..."
  curl -L https://foundry.paradigm.xyz | bash
  source ~/.bashrc
  foundryup || true
fi

# -----------------------------
# 🐳 Docker (Optional for Echidna)
# -----------------------------
if ! command_exists docker; then
  echo "[+] Installing Docker..."
  sudo apt install -y docker.io || true
  sudo service docker start || true
fi

echo "[+] Pulling Echidna toolbox..."
docker pull trailofbits/eth-security-toolbox || true

# -----------------------------
# ✅ Done
# -----------------------------
echo ""
echo "✅ Installation Completed Successfully!"
echo ""
echo "👉 Run your tool:"
echo "python scanner/main.py contracts/test.sol"

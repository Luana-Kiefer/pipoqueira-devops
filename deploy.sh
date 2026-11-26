#!/bin/bash
set -e

APP_DIR="/home/ubuntu/pipoqueira-devops"
IMAGE_NAME="luanakiefer/pipoqueira-devops:latest"

echo "[1/4] Atualizando arquivos de orquestração..."
cd "$APP_DIR"
git pull origin main

echo "[2/4] Baixando imagem mais recente do Docker Hub..."
docker pull "$IMAGE_NAME"

echo "[3/4] Reiniciando containers via Docker Compose..."
docker compose down
docker compose up -d

echo "[4/4] Removendo imagens antigas não utilizadas..."
docker image prune -f

echo "Deploy concluído com sucesso!"
#!/bin/bash
set -e

# Atualiza o pip e instala as dependências
pip install --upgrade pip
pip install -r requirements.txt

# Instala o pacote em modo produção
pip install .

# Cria diretórios necessários
mkdir -p __pycache__
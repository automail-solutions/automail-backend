#!/bin/bash
set -e

# Atualiza o pip e instala as dependências
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Instala o pacote em modo produção
python -m pip install .

# Cria diretórios necessários
mkdir -p __pycache__
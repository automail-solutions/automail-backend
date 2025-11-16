# Automail Solutions Backend

Sistema de classificação e resposta automática de emails usando IA com FastAPI.

## 📋 Descrição do Projeto

API stateless que automatiza a leitura, classificação e sugestão de respostas para emails corporativos usando inteligência artificial. O sistema classifica emails em categorias predefinidas (Produtivo/Improdutivo) e sugere respostas contextualizadas.

## 🏗️ Arquitetura Implementada

O projeto segue os princípios de **Clean Architecture** com separação em camadas:

```
src/
├── domain/           # Entidades e regras de negócio
├── application/      # Casos de uso e serviços
├── infrastructure/   # Integrações externas (Groq API, NLP)
├── presentation/     # Controllers e schemas (FastAPI)
└── shared/          # Configurações e utilitários
```

### Características Stateless
- ✅ Sem banco de dados ou persistência
- ✅ Processamento em tempo real
- ✅ Ideal para serverless functions
- ✅ Escalabilidade horizontal fácil

## 🚀 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido
- **Pydantic** - Validação de dados e geração automática de documentação
- **Groq API** - Classificação e geração de respostas com IA
- **Swagger/OpenAPI** - Documentação interativa automática
- **Python 3.12.3** - Linguagem de programação

## 📋 Pré-requisitos

- Python 3.12.3+
- Conta na Groq API
- Git

## ⚙️ Configuração do Ambiente

### 1. Clone o repositório
```bash
git clone <repository-url>
cd automail-solutions/automail-backend
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:
```env
GROQ_API_KEY=gsk_xxxxxxxxxxxx
ENVIRONMENT=development
LOG_LEVEL=INFO
ALLOWED_ORIGINS=*
```

## 🏃‍♂️ Como Executar Localmente

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

A aplicação estará disponível em: http://localhost:8000

## 📚 Acessar Documentação Swagger

- **Swagger UI**: http://localhost:8000/docs
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🔧 Exemplos de Uso da API

### Classificar Email (curl)
```bash
curl -X POST "http://localhost:8000/api/v1/classify" \
  -H "Content-Type: application/json" \
  -d '{
    "email_subject": "Dúvida sobre o sistema",
    "email_body": "Estou com dificuldades para acessar o sistema. Podem me ajudar?",
    "sender": "cliente@empresa.com"
  }'
```

### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

## 📁 Estrutura de Pastas

```
automail-backend/
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   │   └── email.py
│   │   └── value_objects/
│   │       └── category.py
│   ├── application/
│   │   ├── use_cases/
│   │   │   └── classify_email.py
│   │   └── services/
│   │       └── email_service.py
│   ├── infrastructure/
│   │   ├── ai/
│   │   │   └── groq_client.py
│   │   └── nlp/
│   │       └── text_processor.py
│   ├── presentation/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── classify.py
│   │   │   │   └── health.py
│   │   │   └── dependencies.py
│   │   └── schemas/
│   │       ├── request.py
│   │       └── response.py
│   ├── shared/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   └── main.py
├── requirements.txt
├── vercel.json
├── .env.example
└── README.md
```

## 🎯 Princípios SOLID Aplicados

- **S** - Single Responsibility: Cada classe tem uma responsabilidade específica
- **O** - Open/Closed: Extensível sem modificar código existente
- **L** - Liskov Substitution: Substituição de implementações
- **I** - Interface Segregation: Interfaces específicas e focadas
- **D** - Dependency Inversion: Dependências injetadas via FastAPI

## 🌐 Deploy na Vercel

### 1. Instale a CLI da Vercel
```bash
npm i -g vercel
```

### 2. Configure as variáveis de ambiente na Vercel
```bash
vercel env add GROQ_API_KEY
vercel env add ENVIRONMENT
```

### 3. Deploy
```bash
vercel --prod
```

## 🔍 Troubleshooting

### Erro de API Key
- Verifique se a `GROQ_API_KEY` está configurada corretamente
- Confirme se a chave tem permissões adequadas

### Erro de CORS
- Configure `ALLOWED_ORIGINS` no arquivo `.env`
- Para desenvolvimento local, use `*`

### Erro de Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📊 Endpoints Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/classify` | Classifica email e sugere resposta |
| POST | `/api/v1/classify/batch` | Classifica múltiplos emails de arquivos (.txt/.pdf) |
| GET | `/health` | Verifica saúde da aplicação |
| GET | `/docs` | Documentação Swagger UI |
| GET | `/openapi.json` | Especificação OpenAPI |

## 🔒 Segurança e Privacidade

- ✅ Nenhum dado de email é armazenado
- ✅ Processamento em tempo real e descarte imediato
- ✅ Compliance com LGPD/GDPR por design (stateless)
- ✅ API keys em variáveis de ambiente
- ✅ Validação robusta com Pydantic

## 📄 Licença

MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
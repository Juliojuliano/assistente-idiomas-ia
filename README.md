# 🌐 Assistente Pro de Idiomas com IA

Um aplicativo web inteligente desenvolvido em Python com Streamlit, utilizando o modelo gemini-2.5-flash através da nova biblioteca google-genai para potencializar o aprendizado de novos idiomas.

## 🚀 Funcionalidades

O sistema é dividido em duas abas principais voltadas à prática e estudo:

* *🔤 Tradutor Contextual:* Vai além da tradução literal. Traduz expressões, gírias e frases do cotidiano explicando o contexto cultural, variações de uso e nuances do idioma escolhido.
* *💬 Simulador de Conversa (RPG de Idiomas):* Permite simular situações do mundo real (como Entrevistas de Emprego, Check-in em Hotéis ou Pedidos em Restaurantes). A IA assume o papel do personagem e interage de forma dinâmica e curta no idioma selecionado para treinar a conversação do usuário.

## 🛠️ Tecnologias Utilizadas

* *Python* (Linguagem base)
* *Streamlit* (Interface web rápida e responsiva)
* *Google GenAI SDK* (Integração oficial com os modelos Gemini)
* *Gemini 2.5 Flash* (Processamento de linguagem natural e IA generativa)

## 🔧 Como Executar o Projeto Localmente

### 1. Clonar o repositório ou acessar a pasta
```bash
git clone https://github.com/Juliojuliano/assistente-idiomas-ia.git
cd assistente-idiomas-ia
```

### 2. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar a chave de API do Gemini
O app usa a biblioteca `google-genai`, que lê a chave automaticamente da variável de ambiente `GEMINI_API_KEY`. Crie uma chave gratuita em [Google AI Studio](https://aistudio.google.com/app/apikey) e defina a variável antes de rodar:

```bash
# Linux/macOS
export GEMINI_API_KEY="sua-chave-aqui"

# Windows (PowerShell)
$env:GEMINI_API_KEY="sua-chave-aqui"
```

### 4. Rodar o aplicativo
```bash
streamlit run app_idiomas.py
```

O app abrirá automaticamente no navegador em `http://localhost:8501`.
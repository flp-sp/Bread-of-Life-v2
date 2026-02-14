# Bread-of-Life-v2

Bread-of-Life-v2 é um software de Bíblia open-source que combina recursos tradicionais com inteligência artificial, permitindo uma experiência de estudo bíblico mais interativa e personalizada.

## Funcionalidades

- Leitura de qualquer versão da Bíblia disponível neste repositório: https://github.com/Beblia/Holy-Bible-XML-Format/tree/master
- Integração com IA usando a API do Gemini para consultas, explicações e insights bíblicos.
- Interface amigável construída com CustomTkinter para uma navegação simples e moderna.

## Requisitos

Antes de rodar o projeto, você precisará de:

- Python 3.8 ou superior
- Bibliotecas Python:
  pip install customtkinter genai
- Um arquivo .env contendo sua chave da API do Gemini:
  GEMINI_API_KEY=your_gemini_api_key_here

## Configuração

1. Clone este repositório:
   git clone https://github.com/seu-usuario/Bread-of-Life-v2.git
   cd Bread-of-Life-v2
2. Instale as dependências do Python:
   pip install -r requirements.txt
3. Configure seu .env com a chave da Gemini:
   GEMINI_API_KEY=your_gemini_api_key_here
4. Escolha a versão da Bíblia que deseja usar do repositório https://github.com/Beblia/Holy-Bible-XML-Format/tree/master e coloque o arquivo XML na pasta adequada do projeto.

## Uso

Na pasta app/ execute o programa:
python main.py

- A interface permite selecionar capítulos e livros da Bíblia.
- Você pode fazer perguntas ou solicitar explicações à IA através do campo de chat integrado.

## Contribuição

Contribuições são bem-vindas!
- Abra issues para bugs ou sugestões.
- Faça fork do repositório e envie pull requests para novas funcionalidades.

## Licença

Este projeto é open-source e utiliza a licença MIT.

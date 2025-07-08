PromptCraft
PromptCraft is an AI-powered prompt optimization web app that transforms messy or unclear user inputs into cleaner, more effective prompts using GPT-4.1. It is designed to help developers, writers, and prompt engineers fine-tune their queries for better results from language models.

Demo
Live App: [https://your-render-url.com](https://promptcraft-1.onrender.com/)

Features
Optimizes raw prompts using GPT-4.1 (via Azure OpenAI)

Clean, responsive UI built with Streamlit and custom CSS

Integrated with LangSmith for prompt tracing and evaluation

Secure deployment using environment variables

Fast responses (~2s) with clean formatting

Tech Stack
Frontend: Streamlit, HTML/CSS

AI Backend: Azure OpenAI (GPT-4.1)

Monitoring: LangSmith

Deployment: Render

Version Control: Git & GitHub

Installation
Clone the repository:
git clone [https://github.com/your-username/promptcraft.git](https://github.com/sanvviratthore/PromptCraft)
cd promptcraft

Install the required dependencies:
pip install -r requirements.txt

Set the environment variables manually or create a .env file:
AZURE_OPENAI_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_VERSION=2024-12-01-preview
AZURE_DEPLOYMENT_NAME=gpt-4.1
LANGCHAIN_API_KEY=your_langsmith_key

Run the application:
streamlit run app.py

# Conversational Chatbot with LangChain using Streamlit
![image](https://github.com/sai-annadi/Conversational-Chatbot-with-LangChain-Using-Falcon-7B/assets/111168434/dc1fe414-bbc2-4784-b04f-7fe8f62630a2)

![image](https://github.com/sai-annadi/Conversational-Chatbot-with-LangChain-Using-Falcon-7B/assets/111168434/23409651-33e5-4767-bac0-da1050fcefeb)

### Description:
This GitHub repository contains the source code for a Streamlit-based chatbot called Falcon 7B. The chatbot leverages the power of the Hugging Face Hub and language models to provide intelligent responses to user queries.

### Key Components:

Streamlit Application: The main application is built using Streamlit, a Python library for creating interactive web apps. Users can interact with the chatbot directly through the Streamlit interface.

Hugging Face Hub Integration: The chatbot integrates with the Hugging Face Hub, allowing access to pre-trained language models for natural language processing tasks.

Prompt Template: The chatbot utilizes a prompt template to structure user queries and generate appropriate responses. This template defines the format of user questions and provides placeholders for responses.

LLMChain: This component manages the interaction between the prompt template and the language model. It handles the generation of responses based on user input and context.

Clear Chat History: Users have the option to clear the chat history using a dedicated button in the sidebar.

### Usage:

Model Selection: Users can choose from different Falcon models available in the sidebar.

Input Prompt: Users can enter their questions or queries in the chat interface provided by the Streamlit app.

Response Display: The chatbot generates intelligent responses based on the input prompt and displays them in the chat interface.
## Getting Started

### Prerequisites

- Python 3.7 or later
- pip (package installer for Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/conversational-chatbot.git
2.Navigate to the project directory:

   ```bash
    cd conversational-chatbot
  ```
3.Install the required dependencies:
``` bash
pip install -r requirements.txt
```
### Usage
1.Create a copy of the example.env file and rename it to .env:
2.Open the .env file in a text editor and replace YOUR_HUGGINGFACE_API_TOKEN with your actual Hugging Face API token.

Run the Streamlit app:

```bash
streamlit run chat.py
```
This will launch the Conversational Chatbot in your browser.

### Features
1.Interactive Chat Interface: Engage in dynamic conversations with the chatbot.
2.Model Selection: Choose different Falcon models for chatbot responses.
3.Clear Chat History: Easily clear the chat history with a single button click.

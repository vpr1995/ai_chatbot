# Conversational RAG Chatbot

This project implements a Conversational Retrieval-Augmented Generation (RAG) Chatbot using various components from the LangChain library. The chatbot is designed to assist with question-answering tasks regarding the installation and troubleshooting of garage door openers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/vpr1995/ai_chatbot.git
    cd ai_chatbot
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your PDF document**:
    Place your PDF document in the `files` directory. Update the `file_path` in `app.py` to point to your PDF file.

2. **Start Ollama**:
    Ensure that you have Ollama installed and running. You can start Ollama using the following command:
    ```sh
    ollama start
    ```

3. **Run the chatbot**:
    ```sh
    python src/app.py
    ```

4. **Interact with the chatbot**:
    The chatbot will start in the terminal. Type your questions and get responses based on the content of the provided PDF document.

## Project Structure

- `src/`: Direcory containing the implementation of the DocumentProcessor, VectorStoreManager, and Chatbot classes etc.
- `files/`: Directory to store the PDF documents to be processed.
- `requirements.txt`: List of dependencies required for the project.

## Dependencies

- `langchain_community`
- `langchain_text_splitters`
- `transformers`
- `langchain_core`
- `langchain_ollama`
- `langchain_huggingface`
- `faiss`
- `uuid`

Make sure to install these dependencies using the `requirements.txt` file provided.
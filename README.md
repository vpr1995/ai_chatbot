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

## Sample Conversation

```
2024-08-19 20:40:09,743 - rag_chatbot - INFO - Loading the document...
2024-08-19 20:40:37,138 - rag_chatbot - INFO - Document loaded and split successfully.

2024-08-19 20:40:42,384 - rag_chatbot - INFO - Attempting to load the vector store from disk...
2024-08-19 20:40:42,384 - rag_chatbot - WARNING - An error occurred: Error in faiss::FileIOReader::FileIOReader(const char*) at /project/faiss/faiss/impl/io.cpp:67: Error: 'f' failed: could not open vector_store/index.faiss for reading: No such file or directory

Creating a new vector store...
2024-08-19 20:40:42,384 - rag_chatbot - INFO - Vector store loaded successfully.
2024-08-19 20:40:42,384 - rag_chatbot - INFO - Adding the documents to the vector store...
2024-08-19 20:40:42,881 - rag_chatbot - INFO - Documents added successfully.
2024-08-19 20:40:42,881 - rag_chatbot - INFO - Persisting the vector store on disk...
====================================================
Conversational RAG Chatbot
====================================================
 User >>: hi
 Chatbot >>:  Hello! Welcome to our garage door opener support team. How can I assist you today? Are you experiencing any issues with your garage door opener or do you have a question about installation?
 User >>: I need your help in installing wall console to the garage door opener. can you provide detailed steps ?
 Chatbot >>:  Installing the wall console is an important part of setting up your garage door opener. Here are the detailed steps:

**Step 8: Installing the Wall Console**

* Use garage pre-wiring if available.
* Otherwise, route supplied wire from powerhead to the desired location for the wall control. Secure wire with insulated staples (green bag).
* On the powerhead:
        + Insert wire down through the control wire channel.
        + Remove 1/4" insulation from white and striped wire.
        + Using a small flat head screwdriver, press in the orange tab and insert the white wire in terminal 3 and the striped wire in terminal 4. Ensure the wires are secure in each terminal; adjust as necessary.
* At the wall console end of the wire:
        + Remove 1/4" insulation from the white and striped wires.
        + Secure the white wire to the "W" terminal and the striped wire to the "B/W" terminal as shown. Ensure the wires are secure at each terminal; adjust as necessary.
* Mark the wall console mounting holes, drill 3/32" pilot holes, and mount with #6 x 1-1/4" screws. If mounting to drywall, anchors will be required (not provided).
* Post the "ENTRAPMENT WARNING LABEL" next to the wall console.

**Important Notes:**

* Use of any other wall control can cause unexpected operation of the door and loss of lighting feature.
* Locate wall console within sight of door and far enough from door to prevent contacting it while operating the console. Control must be at least 5 feet above floor to prevent small children from operating it.

If you have any questions or concerns during this process, feel free to ask!
 User >>: bye 
 Chatbot >>:  It was nice assisting you with your garage door opener installation and troubleshooting needs. If you have any other questions or need further assistance in the future, don't hesitate to reach out. Have a great day! Bye!
```
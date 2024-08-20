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
 User >>: Hi
 Chatbot >>:  How can I assist you with your garage door opener installation or troubleshooting today?
 User >>: I need to install the wall console for my garage door opener            
 Chatbot >>:  To ensure a safe and proper installation, let's go through some steps together.

Before installing the wall console, have you checked that there is an electrical outlet within approximately 3 feet of where the opener will be installed? If not, you'll need to contact a licensed electrician to install one.

Also, please make sure the door and its associated hardware (tracks, springs, hinges, rollers) are in good condition. Is anything loose or worn out? If so, it's best to have a trained professional evaluate and repair them before proceeding with the installation.

Additionally, you'll need to remove all ropes and disable any locks connected to the garage door, as well as recommended T-handles.

Once you've taken care of these steps, we can proceed with installing the wall console. Would you like me to guide you through that process?
 User >>: I am ready
 Chatbot >>:  To install the wall console, please follow these steps:

1. **Locate a suitable spot**: Place the wall console within sight of the garage door and far enough from it so that you don't accidentally touch it while operating the console. It's also essential to ensure the control is at least 5 feet above the floor to prevent small children from operating it.
2. **Post the Entrapment Warning Label**: Attach the provided "ENTRAPMENT WARNING LABEL" next to the wall console, as this will serve as a reminder of the importance of proper installation and usage.

Now, regarding the wiring, please follow these additional steps:

1. **Strip 1/4” of insulation from the wires**: You'll need to strip a small portion of the insulation from both the wire going to the Photocells (see section on wiring) and the wire going to the wall control.
2. **Insert the wires into their respective connectors**: Make sure to push in on the tabs to insert the wires correctly.

If you're not comfortable with this process or have any doubts, please let me know, and I'll be happy to guide you further.

Are these steps clear? Or would you like me to clarify anything?
 User >>: how to fix the wall console to wall ?
 Chatbot >>:  To mount the wall console to the wall, follow these steps:

1. **Mark the wall console mounting holes**: Identify the holes on the back of the wall console where the screws will go.
2. **Drill 3/32" pilot holes into the wall**: Use a drill to create small pilot holes in the wall at the marked spots. This will help prevent the drywall from cracking when you screw it in.
3. **Mount with #6 x 1-1/4" screws**: Insert the provided screws into the pilot holes and tighten them securely.

**Important Note:** If you're mounting the wall console to drywall, you'll need to use anchors (not provided) to ensure a secure hold. These can be purchased at most hardware stores or home improvement centers.

Before proceeding with this step, double-check that the wall console is level and plumb on the wall. Make any necessary adjustments before securing it in place.

Is there anything else I can help you with regarding the installation of your garage door opener?
 User >>: I think I got what I need. Thanks for your help
 Chatbot >>:  You're welcome! It was my pleasure to assist you. If you have any other questions or concerns, don't hesitate to reach out.

Remember to refer back to the manual if you need further clarification on any of the steps. And if you're ever unsure about something, it's always best to consult a professional.

Have a great day, and I hope your garage door opener installation goes smoothly!
 User >>: bye
 Chatbot >>:  Bye! Have a great day!

```
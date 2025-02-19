# Chatbot-Groq
Chatbot using Groq and streamlit

# Groq Chat App

## Overview

The **Groq Chat App** is a simple chatbot application built using **Streamlit** and **LangChain**, leveraging **Groq's LLM API**. This application enables interactive conversation with AI models, with options for selecting different language models and customizing conversational memory length.

## Features

- Supports **Mixtral-8x7B-32768** and **Llama3-8B-8192** models.
- **Conversational memory management** using LangChain's `ConversationBufferWindowMemory`.
- **Interactive UI** using Streamlit for easy user interaction.
- **Customizable chat history length** to control context retention.
- **Session state management** to retain past interactions.

## Installation

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/RohiniMaity/Chatbot-Groq.git
   cd Chatbot-Groqconda 
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your **Groq API key**:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

## Project Structure

```
├── app.py              # Main application file
├── requirements.txt    # Dependencies
├── .env                # API keys and environment variables
├── README.md           # Documentation
```

## Dependencies

- `streamlit`
- `langchain`
- `langchain_groq`
- `python-dotenv`

## License

This project is licensed under the **MIT License**.

## Contributing

Feel free to open issues or submit pull requests to improve this project!


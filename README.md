# Sri-chat-api

## Purpose

This repository contains a basic API to create a chat system for the **Servicio de Rentas Internas (SRI)** in Ecuador. The primary goal of this project is to provide a user-friendly chat assistant where individuals can ask questions about taxes in Ecuador. This tool aims to help people resolve their doubts regarding taxation in a simple and accessible way.

## Features

- Chat with an assistant agent to answer tax-related queries in Ecuador.

## Usage

1. **Install Dependencies**:
   This project utilizes `uv (universal virtual environment)` for dependency management. To install the required dependencies, run the following command:
   ```bash
   uv pip install
   ```

2. **Environment Variables**:
   - Use the `.env.example` file as a reference for the required environment variables.
   - Copy the `.env.example` file and rename it to `.env`. Then update the variables with your configuration.

3. **Start the Project Locally**:
   - To run the project locally, execute:
     ```bash
     fastapi dev main.py
     ```

## Technologies

This project uses the following technologies:

- **Python**: The core programming language.
- **FastAPI**: Framework to create the API.
- **UV**: Universal virtual environment for package management.
- **LangChain** and **LangGraph**: Libraries to implement the chat assistant agent.

## Contribution

Contributions are welcome! While there are no specific contribution guidelines at the moment, feel free to fork the repository, create a branch, and submit a pull request with your changes.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

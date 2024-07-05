DiscGPT
===========

DiscGPT Bot is a Discord bot that uses OpenAI's GPT-3.5-turbo to provide intelligent responses to user queries. The bot features customizable prompts, a history of user queries, and pre-defined prompt options to enhance user interaction.

Features
--------

-   **Customizable Prompts**: Ask GPT-3 any question and get a detailed response.
-   **Pre-defined Prompts**: Choose from predefined prompts such as jokes, advice, and quotes.
-   **Prompt History**: Keep track of your last 5 queries.
-   **Clear History**: Clear your prompt history when needed.

Installation
------------

### Prerequisites

-   Python 3.7 or higher
-   pip (Python package installer)
-   A Discord account and server
-   OpenAI API key

### Setup

1.  **Clone the repository**:

    bash

    Copy code

    `git clone https://github.com/yourusername/discgpt-bot.git
    cd discgpt-bot`

2.  **Create and activate a virtual environment**:

    bash

    Copy code

    `python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate``

3.  **Install dependencies**:

    bash

    Copy code

    `pip install -r requirements.txt`

4.  **Create a `.env` file** in the project root and add your Discord bot token and OpenAI API key:

    plaintext

    Copy code

    `DISCORD_BOT_TOKEN=your_discord_bot_token
    OPENAI_API_KEY=your_openai_api_key`

5.  **Run the bot**:

    bash

    Copy code

    `python bot.py`

Usage
-----

Once the bot is running, you can interact with it on your Discord server using the following commands:

### Commands

-   **`/discgpt <prompt>`**: Ask GPT-3 a question.
-   **`/preprompt <option>`**: Choose a predefined prompt (options: 'joke', 'advice', 'quote').
-   **`/history`**: Show your prompt history.
-   **`/clearhistory`**: Clear your prompt history.
-   **`/helpdiscgpt`**: Get help with the DiscGPT bot commands.

### Example

1.  **Ask a question**:

    plaintext

    Copy code

    `/discgpt What is the capital of France?`

    Response: "The capital of France is Paris."

2.  **Get a joke**:

    plaintext

    Copy code

    `/preprompt joke`

    Response: "Why don't scientists trust atoms? Because they make up everything!"

3.  **View your history**:

    plaintext

    Copy code

    `/history`

4.  **Clear your history**:

    plaintext

    Copy code

    `/clearhistory`

5.  **Get help**:

    plaintext

    Copy code

    `/helpdiscgpt`

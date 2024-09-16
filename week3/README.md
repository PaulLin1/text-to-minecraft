# Week 3: Creating a Minecraft Bot with ChatGPT

Welcome to Week 3 of our **Text-to-Minecraft** project! This week, we’ll focus on creating a bot in Minecraft using **Mineflayer** and connecting it to an AI, so you can chat with it via ChatGPT.

## Your Mission This Week

1. Set up Mineflayer to create a Minecraft bot.
2. Secure your OpenAI API key.
3. Connect the language model (ChatGPT) to your bot.

Let’s break down each task into clear steps and provide some coding guidance:

---

### 1. Setting Up Mineflayer (`bot.py`)

First, we’ll create a basic bot using the Mineflayer library.

**Steps:**

1. **Install Mineflayer:**
   ```bash
   npm install mineflayer
   ```

2. **Update the `BuilderBot` class in `bot.py`:**

   - In the `__init__` method, initialize the bot and connect it to your Minecraft server.
   - Use Mineflayer to log the bot in and spawn it in the world.

3. **Create the `spawn` method:**
   - Teleport the bot to your player's location.
   - Make the bot respond to commands via in-game chat.

**Example Code:**

```python
import mineflayer
from dotenv import load_dotenv
import os

class BuilderBot:
    def __init__(self):
        self.bot = mineflayer.createBot({
            'host': 'localhost',  # replace with your server IP
            'port': 25565,        # Minecraft server port
            'username': 'BotName' # Bot's Minecraft username
        })
        self.bot.on('spawn', self.spawn)

    def spawn(self):
        # Teleport bot to the player and make it say hello
        self.bot.chat("Hello! I'm your builder bot.")
```

---

### 2. Getting an API Key

To connect your bot to ChatGPT, you’ll need an API key from OpenAI.

1. **Get the API Key:**
   - Go to the [OpenAI API Key page](https://platform.openai.com/api-keys) and generate a new secret key.
   - Store this key somewhere safe.

2. **Add billing to your OpenAI account:**
   - You'll need to ensure there are credits in your account, usually up to $10 should be enough.

---

### 3. Setting Up Environment Variables

We’ll keep your API key secure by using a `.env` file.

1. **Create a `.env` file** in your project root directory.
   - Inside `.env`, add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Install `dotenv` in Python** to load the environment variables:
   ```bash
   pip install python-dotenv
   ```

3. **Load the environment variables in your script**:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

**Why the `.env` file?**
API keys are sensitive. Using a `.env` file prevents accidental sharing of your API key when pushing code to GitHub or sharing your project.

---

### 4. Connecting the LLM to Mineflayer (`main.py`)

Let’s integrate ChatGPT with Mineflayer so the bot can respond to in-game chat messages.

1. **Use OpenAI’s API to generate responses from ChatGPT.**
   - Install the OpenAI Python package:
     ```bash
     pip install openai
     ```

2. **Update `main.py`:**

   - Listen for chat events from players.
   - Send player messages to ChatGPT and return the AI-generated response.
   - Make sure the bot differentiates between regular commands (like teleportation) and chatting.

**Example Code:**

```python
import openai
import mineflayer
from dotenv import load_dotenv
import os

class BuilderBot:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.bot = mineflayer.createBot({
            'host': 'localhost',
            'port': 25565,
            'username': 'BotName'
        })
        self.bot.on('spawn', self.spawn)
        self.bot.on('chat', self.handle_chat)

    def spawn(self):
        self.bot.chat("Bot is ready!")

    def handle_chat(self, username, message):
        if username == self.bot.username:
            return  # Don't respond to the bot's own messages

        if "come" in message.lower():
            # Teleport to the player
            self.bot.chat(f"Coming to {username}!")
            # Logic to teleport to the player
        else:
            # Send message to ChatGPT
            response = self.get_chatgpt_response(message)
            self.bot.chat(response)

    def get_chatgpt_response(self, message):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150
        )
        return response.choices[0].text.strip()
```

---

### Testing Your Implementation

To verify your bot is working properly, make sure it:

1. Spawns in the game and teleports to you.
2. Responds to commands (e.g., type "come" and it teleports).
3. Replies to in-game chat using ChatGPT for any message that doesn’t contain the word "come."

---

## Bonus Challenges

If you complete the core functionality, try these extra tasks:

1. **Custom Commands:**
   - Add more commands for the bot, such as building structures or exploring.

2. **Multiple Bots:**
   - Create a second bot for more interactions and teamwork.

3. **Enhanced ChatGPT Responses:**
   - Improve ChatGPT’s responses by tweaking the prompts or using a different model.

---

Next week, we’ll explore **more advanced bot features** and how to build structures autonomously based on player commands. Keep pushing forward, and good luck!

--- 

This refined version keeps the focus on creating a bot with Mineflayer and connecting it to an AI using OpenAI’s API. The structure should help your audience smoothly transition from setting up the bot to interacting with it.
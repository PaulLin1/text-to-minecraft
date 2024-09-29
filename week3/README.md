# Week 3: Creating a Minecraft Bot with ChatGPT

Welcome to Week 3 of our **Text-to-Minecraft** project! This week, we’ll focus on creating a bot in Minecraft using **Mineflayer** and connecting it to an AI, so you can chat with it via ChatGPT.

## Your Mission This Week

1. Set up Mineflayer to create a Minecraft bot.
2. Secure your OpenAI API key.
3. Connect the language model (ChatGPT) to your bot.

Let’s break down each task into clear steps and provide some coding guidance:

**Announcement:** On Monday, 9/30, there will be a workshop on RAG. In the following weeks, you will be using RAG in your Minecraft project. This is a great opportunity to get a head start on that part of the project. Go to our Instagram for more information!

---

### 1. Setting Up Mineflayer (`bot.py`)

First, we’ll create a basic bot using the Mineflayer library.

**Steps:**

1. **Install Mineflayer:**
   npm install mineflayer

2. **Create a file called bot.py and create a BuilderBot class:**
- For now the class should:
	- Connect to your Minecraft world
	- Spawn a bot next to you
	- Be able to come when the player types 'come' into the Minecraft chat
		- You can do this by making the bot chat the 'tp' command in Minecraft

- We have given an outline of the class. Use that and the documentation (https://github.com/PrismarineJS/mineflayer/blob/master/docs/mineflayer.ipynb) to finish the class!

**Outline:**

from javascript import require, On
mineflayer = require('mineflayer')

class BuilderBot:
    def __init__(self):
        """
        Initializes a bot in minecraft
        """

        self.setup_listeners()

    def setup_listeners(self):
        @On(self.bot, 'spawn')
        def handle_spawn(*args):
            """
            Spawns the bot
            """

            @On(self.bot, 'chat')
            def on_chat(this, sender, message, *args):
                """
                Handles chats
                :param sender: The sender of the message
                :param message: The message that got sent
                """

            @On(self.bot, 'end')
            def on_end(*args):
	            """
	            Ends the bot
	            """

When you want to test, create a file called main.py and initialize a bot. Then open your Minecraft world to LAN and run main.py.

---

### 2. Getting an API Key

To connect your bot to ChatGPT, you’ll need an API key from OpenAI.

1. **Get the API Key:**
   - Go to the [OpenAI API Key page](https://platform.openai.com/api-keys) and generate a new secret key.
   - Store this key somewhere safe.

2. **Add billing to your OpenAI account:**
   - You'll need to ensure there are credits in your account. $10 should be enough.

---

### 3. Setting Up Environment Variables

We’ll keep your API key secure by using a .env file.

1. **Create a .env file** in your project root directory.
   - Inside .env, add your OpenAI API key:
   OPENAI_API_KEY=your_openai_api_key_here

2. **Install dotenv in Python** to load the environment variables:
   pip install python-dotenv

3. **When you want to load the environment variables, do this**:

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

**Why the .env file?**
API keys are sensitive. Using a .env file prevents accidental sharing of your API key when pushing code to GitHub or sharing your project.

---

### 4. Connecting the LLM to Mineflayer (`bot.py`)

Let’s integrate ChatGPT with Mineflayer so the bot can respond to in-game chat messages.

1. **Use OpenAI’s API to generate responses from ChatGPT.**
   - Install the OpenAI Python package:
     pip install openai
=
2. **Update bot.py:**

   1. Load the api key from the .env file in the init function
   2. When talking to the bot, if the message is not 'come', the LLM will respond
	   - Search up how to use the OpenAI API to get a response from the message. This is good practice at reading documentation, which you'll be doing a lot of in the future! This should only be a couple lines of code
	   - After you get the response, use the bot.chat command to output the response in Minecraft.
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

2. **Enhanced ChatGPT Responses:**
   - Improve ChatGPT’s responses by tweaking the prompts or using a different model.

---

Next week, we’ll explore **more advanced bot features** and how to build structures autonomously based on player commands. Keep pushing forward, and good luck!

--- 

This refined version keeps the focus on creating a bot with Mineflayer and connecting it to an AI using OpenAI’s API. The structure should help your audience smoothly transition from setting up the bot to interacting with it.


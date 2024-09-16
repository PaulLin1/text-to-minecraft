# Week 4: Building in Minecraft - Prompt Templating

Welcome to Week 4 of our **Text-to-Minecraft** project! This week, we’ll focus on **building structures in Minecraft** using a bot that takes advantage of **prompt templating** to generate code. By the end of this week, you'll be able to give the bot commands like "build a house," and it will generate and execute Python code to carry out the task in your Minecraft world.

---

## Your Mission This Week

1. Build a Mineflayer bot that can construct structures.
2. Implement prompt templating to generate Minecraft building code.
3. Use example-driven prompts to enhance your bot's building abilities.

### What You’ll Learn:

- Prompt templating for controlled LLM outputs.
- Connecting Minecraft with the bot to execute build commands.
- Crafting effective examples for the LLM to understand building requests.

---

## 1. Setting Up the Bot (`bot.py`)

Your bot will now build structures instead of just chatting! Let’s build on last week's bot setup to give it the ability to construct based on prompts.

### Steps:

1. **Install Mineflayer** (if you haven’t already):
   ```bash
   npm install mineflayer
   ```

2. **Update `BuilderBot` Class**:

In `bot.py`, create a bot that logs into the Minecraft server and listens for build commands:

```python
import mineflayer
from dotenv import load_dotenv
import os

class BuilderBot:
    def __init__(self):
        self.bot = mineflayer.createBot({
            'host': 'localhost',  # Replace with your server IP
            'port': 25565,         # Minecraft server port
            'username': 'BotName'  # Bot's Minecraft username
        })
        self.bot.on('spawn', self.spawn)
        self.bot.on('chat', self.handle_chat)

    def spawn(self):
        self.bot.chat("I am ready to build!")

    def handle_chat(self, username, message):
        if username == self.bot.username:
            return  # Don't respond to bot's own messages

        if message.startswith("build"):
            structure = message.replace("build", "").strip()
            self.bot.chat(f"Building {structure}...")
            # Call the code generation function (integrated with the LLM)
            code = generate_build_code(structure)
            exec(code)  # This will execute the building logic in Minecraft
```

---

## 2. Using Prompt Templating to Generate Minecraft Code (`MinecraftCodeGenerator`)

This is where **prompt templating** comes into play. You’ll teach the bot how to generate code that builds different structures in Minecraft based on examples and templates.

### What is Prompt Templating?

We use **few-shot learning** with templating to show the model how to respond by providing examples. These examples guide the model to return Python code that the bot can use to build things in Minecraft.

### Key Steps:

- **Set up the prompt template** that gives examples of build commands and their corresponding Python code.
- **Generate code** based on the player’s in-game command (e.g., "build a house").

### Example Code (`MinecraftCodeGenerator` class):

```python
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

class MinecraftCodeGenerator:
    def __init__(self):
        """
        Initializes the LLM with prompt templating
        """
        load_dotenv(find_dotenv())
        model = ChatOpenAI(api_key=os.environ.get('OPENAI_API_KEY'), model_name="gpt-3.5-turbo")

        # Few-shot examples to show the model how to generate building code
        examples = [
            {
                "input": "build a house",
                "output": "pos = bot.entity.position\nx = int(pos.x)\ny = int(pos.y)\nz = int(pos.z)\nsize = 5\nheight = 4\nblock_type = 'stone'\n\nx_start = x - size // 2\nx_end = x + size // 2\nz_start = z - size // 2\nz_end = z + size // 2\ny_floor = y\ny_ceiling = y + height\n\nfor i in range(x_start, x_end + 1):\n    for j in range(z_start, z_end + 1):\n        place_block(bot, block_type, i, y_floor, j)\n\nfor i in range(x_start, x_end + 1):\n    for j in range(z_start, z_end + 1):\n        for k in range(y_floor + 1, y_ceiling):\n            if i == x_start or i == x_end or j == z_start or j == z_end:\n                place_block(bot, block_type, i, k, j)\n\nfor i in range(x_start, x_end + 1):\n    for j in range(z_start, z_end + 1):\n        place_block(bot, block_type, i, y_ceiling, j)"
            },
            {
                "input": "build a snowman",
                "output": "pos = bot.entity.position\nx = int(pos.x)\ny = int(pos.y)\nz = int(pos.z)\nbody_radius = 2\nmiddle_radius = 1\nhead_radius = 1\n\nbody_block = 'snow_block'\nhead_block = 'carved_pumpkin'\narm_block = 'oak_fence'\n\ndef place_sphere(bot, block_type, center_x, center_y, center_z, radius):\n    for i in range(center_x - radius, center_x + radius + 1):\n        for j in range(center_y - radius, center_y + radius + 1):\n            for k in range(center_z - radius, center_z + radius + 1):\n                if (i - center_x) ** 2 + (j - center_y) ** 2 + (k - center_z) ** 2 <= radius ** 2:\n                    place_block(bot, block_type, i, j, k)\n\nplace_sphere(bot, body_block, x, y + body_radius, z, body_radius)\nplace_sphere(bot, body_block, x, y + body_radius + 2*middle_radius, z, middle_radius)\nplace_sphere(bot, head_block, x, y + body_radius + 2*middle_radius + 2*head_radius, z, head_radius)\n\nplace_block(bot, arm_block, x - middle_radius - 1, y + body_radius + middle_radius, z)\nplace_block(bot, arm_block, x + middle_radius + 1, y + body_radius + middle_radius, z)"
            }
        ]

        example_prompt = ChatPromptTemplate.from_messages([("human", "{input}"), ("ai", "{output}")])
        few_shot_prompt = FewShotChatMessagePromptTemplate(example_prompt=example_prompt, examples=examples)

        # Final prompt template for the model
        prompt_template = ChatPromptTemplate.from_messages([
            ('system', "You are an AI that generates Python code to build things in Minecraft."),
            few_shot_prompt,
            ('human', '{input}')
        ])

        self.chain = (prompt_template | model | StrOutputParser())

    def generate_code(self, message):
        """
        Sends a building command and returns generated Python code
        :param message: Command input (e.g., 'build a house')
        :return: Python code for building the structure
        """
        return self.chain.invoke({"input": message})
```

---

## 3. Testing Your Implementation

After setting up the bot and connecting it to your prompt templates, it's time to test it out.

### Steps for Testing:

1. **Run your Minecraft server** and launch the bot.
2. **Type commands** like "build a house" or "build a snowman" in the Minecraft chat.
3. **Check the results**: The bot should generate the code and start building the requested structure.

---

## Bonus Challenges

If you finish early, try these:

1. **Enhance the examples** by adding more complex builds like towers, bridges, or statues.
2. **Add error handling**: Ensure the bot can gracefully handle unknown or invalid commands.
3. **Refine prompt templating**: Experiment with different prompt formats to improve code generation quality.

Next week, we’ll dive deeper into **advanced structure building** and optimizing the bot’s performance. Happy building!
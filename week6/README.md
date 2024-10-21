# Week 6: Building in Minecraft - Retrieval Augmented Generation (Part 2)

Welcome to Week 6 of our **Text-to-Minecraft** project! This week, we’ll continue our journey into **Retrieval Augmented Generation** (RAG). We’ll be setting things up before fully implementing RAG next week. Get excited—there’s plenty of cool information ahead! Plus, we’ll be using a features that are less than a year old. Talk about being on the cutting edge!

---

## Your Mission This Week

1. Learn about structured output and its importance.
2. Add a skill for the bot to build based on JSON.
3. Create a new MinecraftGenerator model that uses structured output.

---

## 1. What is Structured Output?

LLMs and RAG have numerous real-world applications, but they typically output text without a clear format. For instance, if you wanted an LLM to return information in JSON format, you could only hope it would comply. People often joked, "Please return the output in JSON format, or I will get fired." While clever workarounds like this[https://www.youtube.com/watch?v=yj-wSRJwrrc] have emerged, they never guaranteed 100% JSON output, which can lead to significant problems if that output is used elsewhere in your app. OpenAI just recently released its own structured output feature that guarentees 100% structured output. However, since we are already using LangChain's tools, we'll stick to that.

---

## 2. Adding Skill to Build from JSON

Before diving into structured output, we need the bot to build using JSON. Previously, we had the LLM generate Python code that created place_block functions to communicate with Minecraft. Now, we want the LLM to generate JSON and implement a function that parses this JSON to output the same place_block commands.

### Basics of JSON Parsing

JSON is a structured file format similar to Python dictionaries, consisting of key-value pairs. If you look at the JSON files in the filtered_schematics_data folder that you downloaded last week, you’ll notice a consistent format: the schematic name is paired with a list of blocks, each represented as a dictionary. This uniformity means we can create a single parsing function for all JSON files.

### Create the build_from_json Function

In your skills.py file, add a function called build_from_json that accepts the bot and a file as parameters. Import the json library at the top of your file. Inside the function, use json.loads(file) to parse the JSON, which will turn it into a Python dictionary.

To access the schematic name, you can use parsed['schematic_name']. Use this, along with the existing code in the place_block file, to complete the build_from_json function. Test it by inputting a JSON file and verifying that the bot builds correctly.

### Update bot.py

In bot.py, instead of executing the response as code, call the build_from_json function with the JSON response. Now the response will be in JSON format rather than Python code.

---

## 3. Implementing Structured Output

Now that we can build from a JSON file, let’s ensure the LLM outputs JSON. With structured output, this process is straightforward.

### Update Your Bot File

1. Replace the string parser with LangChain’s JSON output parser. Create a schema using the following Python classes:

class Block(BaseModel):
    block_type: str = Field(description="Type of the block")
    x: int = Field(description="X coordinate of the block")
    y: int = Field(description="Y coordinate of the block")
    z: int = Field(description="Z coordinate of the block")

class MinecraftBuild(BaseModel):
    schematic_name: str = Field(description="Name of the schematic")
    blocks: List[Block] = Field(description="List of blocks in the schematic")

2. Pass this schema into the JsonOutputParser by initializing it with the MinecraftBuild class.

3. In your chain, update the parser to use the new JSON output parser.

### Update Few-Shot Examples and System Message

Change the few-shot examples and the system message so that the output is now JSON instead of Python code. Use a small JSON file as an example (keeping in mind the context window limits).

---

Everything should be ready now! Try this out and see if it works!

--- 

Feel free to reach out if you have any questions or need further assistance!

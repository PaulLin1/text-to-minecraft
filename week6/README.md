# Week 6: Building in Minecraft - Retrieval Augmented Generation (Part 2) 

Welcome to Week 6 of our **Text-to-Minecraft** project! This week, we’ll continue learning about **Retrieval Augmented Generation** also known as RAG. However, this week we'll still be setting stuff up before we fully implement it next week. Fear not, this week is still packed with a lot of cool information. We will be using a feature that was released on AUGUST 2024. Talk about being on the cutting edge! 
---

## Your Mission This Week

1. Learn about structured output and why it is so important
2. Add a skill for the bot to build based on JSON
3. Create a new MinecraftGenerator model that uses structured output

---

## 1. What is structured output? 

As we mentioned earlier, LLM's and RAG are being used in many real world applications. However, LLM's are only able to output text without any clear format. For example, if you wanted it to return information in as a JSON file, you could only hope that it would answer your request. People joked that they prompted, "Please return the output in JSON format or I will get fired". Additoinally, other people came up with clever workarounds like Pydantic is all you need. However, these were never able to guarentee that the output would be JSON 100% of the time. This can lead to big problems if you are using your LLM output for some other part of your app. The core problem that people were trying to solve is this: We need something that is basically a next word predictor to adhere to some guidelines on how their response should be formatted.

Here is where OpenAI's Structured Output comes in, a way to guarentee JSON formatted output all the time.

## 2. Adding skill to build from JSON

Before we start using structured output, we need the bot to be able to build using a JSON before. Before, we had the LLM generated python code that would create place_block functions that would be chatted into Minecraft. Now, we want the LLM to generate JSON and then have a function that parses the JSON and outputs the same place_block commands.

Basics of JSON parsing
JSON is a structured file format. This allows us to write code that is able to split it up. Its format is similar to python dictionaries. There is a key value pair. Take a look at what of the JSON files in the filtered_schematics_data folder that you downloaded last week. You will see a key value pair for the the schematic name and the blocks. The blocks holds a list that holds a dictoinary of block information. If you go to another JSON file, you will find that it has the same format. This means that we only need to create one function to parse every JSON file.

Lets create a parse_json function in skills.py file

def build_from_json(bot, file):

Next, we will have to use the JSON library to parse it.

Add import json to the top of your file

You can now cal it with

parsed = json.loads(file)

Now parsed is a python's dictoinary!

For example, if I wanted to get the schematic name, I could type parse['schematic_name'].

Use this, and the code we have in the place_block file to create the build_from_json function. You can test it by inputting a JSON file and seeing if the bot builds it correctly.


## 3. Implementing Structured Output

Now that we able to build from a JSON file, lets make the LLM output JSON. Again with structured output, this is super easy.

First go into the file where your bot is.
As of now, we are using a string parser. However, since we are using JSON we need something else to parse our files. We can ues LangChain's JSON output Parser instead. The schema will be a python class that looks like this.


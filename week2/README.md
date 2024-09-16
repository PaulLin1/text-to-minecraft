# Week 2: Building Your Tron Game

Welcome back! This week, we’ll be diving deeper into how ChatGPT works, exploring some of its limitations when it comes to creating Minecraft builds, and writing a Python function that will serve as the foundation for our bot to interact with Minecraft. While this week is more exploratory, it's an essential step in understanding how large language models (LLMs) respond and how we can leverage them for creative projects.

## Your Mission This Week

1. **Create an OpenAI account**
2. **Start prompting**
3. **Create a `place_block` function**

Let's break these down and tackle them step by step:

### 1. Create an OpenAI Account

Head over to [OpenAI's ChatGPT](https://chatgpt.com) and create an account if you haven't already. This will give you access to ChatGPT, which we'll use for generating Python code that helps build structures in Minecraft. 

### 2. Start Prompting

Once you have an account, start experimenting with ChatGPT by prompting it to build things in Minecraft using Python code. Analyze the responses and answer the following key question: 

**"Can this generated code be directly used to build in Minecraft? Why or why not?"**

Here are some example prompts you can try out:
- *"Build a car in Minecraft."*
- *"Write Python code to create a house in Minecraft."*
- *"Create a function that can build the Statue of Liberty in Minecraft."*

After generating code, look at how ChatGPT structures its responses and assess:
1. Does the code actually work in Minecraft?
2. What parts of the response are useful, and what parts might need adjustments?
3. Are there any limitations in the format or output?

### 3. Reflection: Understanding ChatGPT's Output

Hopefully, you’ve played around with a few prompts by now. Let’s reflect on some important considerations:

1. **Does the code provided by ChatGPT automatically work with Minecraft?**
   - Pay attention to whether the generated code requires additional libraries or assumes things like the bot’s position in the Minecraft world. This might make it unusable without modifications.
   
2. **Consistency of Output:**
   - Sometimes, the generated code will vary in format or structure. For example, one prompt may return code to place blocks, while another may require you to import packages. Can we ensure ChatGPT’s output is more consistent? If so, how might we go about it?

These are crucial questions to consider as you move forward. Keep them in mind as we continue developing our project.

### 4. Creating the `place_block` Function

Now that you’ve explored ChatGPT’s outputs, it’s time to create a Python function that allows us to interact with Minecraft.

Open the `skills.py` file and locate the `place_block` function header. This function will act as a bridge between the LLM-generated code and Minecraft. Your task is to complete the function so that it prints a `setblock` command, which will place a block in Minecraft at a specified location.

```python
def place_block(block_type, x, y, z):
    # Your task is to make this function print the correct setblock command
    print(f"/setblock {x} {y} {z} {block_type}")
```

This is the basic structure, but feel free to improve it! The goal here is to make sure the generated code can communicate effectively with Minecraft by printing a valid command in the console.


## Bringing It All Together

Once you've got the `place_block` function working, it’s time to test it with ChatGPT. The workflow looks like this:

1. **Prompt ChatGPT**: Ask it to generate code for what you want to build. Make sure to include the `place_block` function header in your prompt so ChatGPT knows how to format its output.
2. **Run the Code**: Take the generated code, run it in your Python environment, and copy the printed `setblock` commands.
3. **Place in Minecraft**: Paste the commands into Minecraft to build your structure.

You might not get everything right on the first try, but that’s okay! This week is all about understanding the interaction between ChatGPT and Minecraft. In the upcoming weeks, we’ll work on making the responses more structured and reliable.

## Bonus Challenges

Finished early? Want to push your skills further? Here are some bonus tasks to try out:

1. **Update the `place_block` Function**: 
   - Right now, the `place_block` function is quite simple. It doesn’t support orientations for blocks like doors or torches, which can face different directions. Extend the function to take an additional parameter that controls the block’s orientation. You might need to research how Minecraft handles block orientations to implement this!

2. **Consistency in Prompts**: 
   - Try creating a few more advanced prompts and analyze how ChatGPT handles complex structures. Can you guide the model to output a consistent response each time?

Next week, we’ll be expanding on this foundation by creating a bot that can interact with Minecraft, and we’ll start thinking about how we can integrate AI to enhance the experience. Great work so far—keep going!
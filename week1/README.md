# Week 1: Getting Started with Minecraft AI Builder - A Step-by-Step Guide

Welcome to the Minecraft AI Builder project! We're so glad you've decided to join us. This week, we're setting up everything you need to start building an AI that constructs structures in Minecraft. Don't worry if you're new to programming—we'll go through each step together this first week.

## 1. Understanding What We Are Building

Before diving into coding, let's understand what we're building.

**Task:** Watch the video that this project is based on.
1. Go to https://youtu.be/kbf9QJJn-UQ?feature=shared
2. Watch the video and try to understand what we are building.
3. Pay attention to:
   - How the bot is set up.
   - How blocks are placed.
   - How you can make it better!

**Side note:** In this project, we are not building a large language model from scratch. However, if you're interested in that, one of our graduate advisors, Mateja, will be hosting advanced workshops where we rebuild an LLM together. They will be held on Tuesdays throughout the semester. Keep an eye on our socials to get notified of when and where they'll take place!

## 2. Setting Up Your Development Environment

Now, let's set up your computer for Python development. We will be using Python, Mineflayer, OpenAI, LangChain and more. Don’t worry if you're unfamiliar with these tools; each will be introduced in detail throughout the following weeks.

### 2.1 Installing Python

1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or later for your operating system.
3. Run the installer.
   - On Windows, make sure to check "Add Python to PATH."
4. Verify the installation:
   - Open a command prompt or terminal.
   - Type `python --version` and press Enter.
   - You should see the Python version number.

### 2.2 Setting Up Your Repo

1. If you're the one making the repo, go to ##LINK HERE##/fork and make a copy of the MSUAIClub/FINALREPONAME repo.
2. Go to that repo and click the green "Code" button, then copy the link.
3. In the IDE of your choice, clone the repo by pasting the link you copied in the previous step. 
   - (If you're using VS Code, you can do this by clicking the "Clone Git Repository" button and pasting the link in the input field.)

### 2.3 Setting Up Your Virtual Environment

Virtual environments help keep your projects organized. They allow you to install libraries and packages specific to this project without affecting your system's Python installation.

1. Open a command prompt or terminal in the folder where your repo is cloned.
2. Create a virtual environment:
   - On Windows:
     ```
     python -m venv venv
     ```
   - On macOS/Linux:
     ```
     python3 -m venv venv
     ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

### 2.4 Installing Required Libraries

Now that your virtual environment is active, let's install the necessary libraries.

1. Ensure you're in your project directory with the virtual environment activated.
2. Install the libraries using pip:
   ```
   pip install mineflayer openai langchain
   ```
3. Verify the installations:
   ```
   pip list
   ```

You should see `mineflayer`, `openai`, and `langchain` in the list.

## 3. Setting Up Your Minecraft World

Because of some limitations of Mineflayer, we need to use a specific version of Minecraft.

1. Open Minecraft Java Edition.
2. Go to 'Installations' and add version 1.20.4. This is the **only** version we will be using for this project.
3. Create a new world:
    - Change the game mode to Creative.
    - Allow cheats.
    - **Optional:** Change the world type to Superflat so that all builds are flush with the ground.

## 4. Introduction to the /setblock Command

The `/setblock` command in Minecraft is used to change a block at specific coordinates to a different block type.
The syntax is `/setblock <x> <y> <z> <block>`, where `<x>`, `<y>`, and `<z>` are the coordinates, and `<block>` is the type of block you want to place.
This command allows us-and more importantly, the bot—to quickly and precisely change block types at coordinates to build structures.

Play around with the command to understand some of its quirks! You can use the F3 key to view your coordinates and change blocks near you.

## Wrapping Up

By the end of this week, you should have:
1. Understood what we are building.
2. Set up a Python development environment with a virtual environment.
3. Installed Mineflayer, OpenAI, and LangChain.
4. Familiarized yourself with the `/setblock` command.

Next week, we'll dive into ChatGPT and start coding in Python. Great job getting everything set up!
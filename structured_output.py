import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

import json
from textwrap import dedent
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List
from chapel import *
from langchain_core.output_parsers import JsonOutputParser


class Block(BaseModel):
    block_type: str = Field(description="Type of the block")
    x: int = Field(description="X coordinate of the block")
    y: int = Field(description="Y coordinate of the block")
    z: int = Field(description="Z coordinate of the block")

class MinecraftBuild(BaseModel):
    schematic_name: str = Field(description="Name of the schematic")
    blocks: List[Block] = Field(description="List of blocks in the schematic")

class MinecraftCodeGenerator:
    def __init__(self):
        """
        Initializes llm
        """
        load_dotenv(find_dotenv())

        # self.client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        # self.MODEL = "gpt-4o-2024-08-06"

        model = ChatOpenAI(
            api_key=os.environ.get('OPENAI_API_KEY'), 
            model_name="gpt-3.5-turbo"
        )

        parser = JsonOutputParser(pydantic_object=MinecraftBuild)

        chapel = pixel_art()

        examples = [
            {
                "input": "build a house",
                "output": chapel,
            }
            # {
            #     "input": "build a snowman",
            #     "output": "pos = bot.entity.position\nx = int(pos.x)\ny = int(pos.y)\nz = int(pos.z)n\nbody_radius = 2\nmiddle_radius = 1\nhead_radius = 1\n\nbody_block = 'snow_block'\nhead_block = 'carved_pumpkin'\narm_block = 'oak_fence'\n\ndef place_sphere(bot, block_type, center_x, center_y, center_z, radius):\n    for i in range(center_x - radius, center_x + radius + 1):\n        for j in range(center_y - radius, center_y + radius + 1):\n            for k in range(center_z - radius, center_z + radius + 1):\n                if (i - center_x) ** 2 + (j - center_y) ** 2 + (k - center_z) ** 2 <= radius ** 2:\n                    place_block(bot, block_type, i, j, k)\n\nplace_sphere(bot, body_block, x, y + body_radius, z, body_radius)\nplace_sphere(bot, body_block, x, y + body_radius + 2*middle_radius, z, middle_radius)\nplace_sphere(bot, head_block, x, y + body_radius + 2*middle_radius + 2*head_radius, z, head_radius)\n\nplace_block(bot, arm_block, x - middle_radius - 1, y + body_radius + middle_radius, z)\nplace_block(bot, arm_block, x + middle_radius + 1, y + body_radius + middle_radius, z)"
            # }
        ]
        example_prompt = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}"),
            ]
        )
        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=example_prompt,
            examples=examples,
        )

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ('system', "You are an AI that generates only JSON files of minecraft structures"),
                few_shot_prompt,
                ('human', '{input}')
            ]
        )

        self.chain = (
            prompt_template 
            | model 
            | parser
        )
        

        
    def generate_code(self, message):
        """
        Sends a message to the llm
        :param message: The message that is sent
        :return: The response of the llm
        """
        
        response = self.chain.invoke({"input": message})


        return response
    
# build_agent = MinecraftCodeGenerator()
# print(build_agent.generate_code("build a house"))

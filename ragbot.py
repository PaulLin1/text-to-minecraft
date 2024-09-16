import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
import json
from langchain.storage import InMemoryByteStore
from langchain.retrievers.multi_vector import MultiVectorRetriever
import uuid
from langchain_core.documents import Document
import pickle
from langchain_core.runnables import RunnablePassthrough

class MinecraftCodeGenerator:
    def __init__(self):
        """
        Initializes llm
        """
        load_dotenv(find_dotenv())

        model = ChatOpenAI(
            api_key=os.environ.get('OPENAI_API_KEY'), 
            model_name="gpt-4o-2024-05-13"
        )

        examples = [
            {
                "input": "build a house",
                "output": "pos = bot.entity.position\nx = int(pos.x)\ny = int(pos.y)\nz = int(pos.z)\nsize = 5\nheight = 4\nblock_type = 'stone'\n\nx_start = x - size // 2\nx_end = x + size // 2\nz_start = z - size // 2\nz_end = z + size // 2\ny_floor = y\ny_ceiling = y + height\n\nfor i in range(x_start, x_end + 1):\n    for j in range(z_start, z_end + 1):\n        place_block(bot, block_type, i, y_floor, j)\n\nfor i in range(x_start, x_end + 1):\n    for j in range(z_start, z_end + 1):\n        for k in range(y_floor + 1, y_ceiling):\n            if i == x_start or i == x_end or j == z_start or j == z_end:\n                place_block(bot, block_type, i, k, j)\n\nfor i in range(x_start, x_end + 1):\n    for j in range(z_start, z_end + 1):\n        place_block(bot, block_type, i, y_ceiling, j)"
            },
            {
                "input": "build a snowman",
                "output": "pos = bot.entity.position\nx = int(pos.x)\ny = int(pos.y)\nz = int(pos.z)n\nbody_radius = 2\nmiddle_radius = 1\nhead_radius = 1\n\nbody_block = 'snow_block'\nhead_block = 'carved_pumpkin'\narm_block = 'oak_fence'\n\ndef place_sphere(bot, block_type, center_x, center_y, center_z, radius):\n    for i in range(center_x - radius, center_x + radius + 1):\n        for j in range(center_y - radius, center_y + radius + 1):\n            for k in range(center_z - radius, center_z + radius + 1):\n                if (i - center_x) ** 2 + (j - center_y) ** 2 + (k - center_z) ** 2 <= radius ** 2:\n                    place_block(bot, block_type, i, j, k)\n\nplace_sphere(bot, body_block, x, y + body_radius, z, body_radius)\nplace_sphere(bot, body_block, x, y + body_radius + 2*middle_radius, z, middle_radius)\nplace_sphere(bot, head_block, x, y + body_radius + 2*middle_radius + 2*head_radius, z, head_radius)\n\nplace_block(bot, arm_block, x - middle_radius - 1, y + body_radius + middle_radius, z)\nplace_block(bot, arm_block, x + middle_radius + 1, y + body_radius + middle_radius, z)"
            }
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

        with open('data/blocks.json', 'r') as json_file:
            blocks = json.load(json_file)


        id_key = "doc_id"

        with open('data_docs.pickle', 'rb') as file:
            data = pickle.load(file)

        vectorstore = Chroma(
            collection_name="summaries",
            embedding_function=OpenAIEmbeddings()
        )

        store = InMemoryByteStore()
        self.retriever = MultiVectorRetriever(
            vectorstore=vectorstore,
            byte_store=store,
            id_key=id_key,
        )

        summary_docs = [
            Document(page_content=s, metadata={id_key: data['doc_ids'][i]})
            for i, s in enumerate(data['summaries'])
        ]

        self.retriever.vectorstore.add_documents(summary_docs)
        self.retriever.docstore.mset(list(zip(data['doc_ids'], data['docs'])))


        prompt_template = ChatPromptTemplate.from_messages(
            [
                ('system', f"""
                    You are an AI that generates only Python code to build realistic things in Minecraft.
                    You are a Python code generator. Your task is to provide only Python code in response to my requests. Do not include any explanations, descriptions, or comments.
                    for your build, only use minecraft blocks that are found in this list {blocks}.
                    make your builds extremely realistic and detailed.
                    You're code has to be less than 7000 characters and executable.
                 """),
                few_shot_prompt,
                ('human', '{input}'),
                ('human', 'base your build off of this: {context}'),
            ]
        )

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        self.chain = (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            |
            prompt_template
            | model 
            | StrOutputParser()
        )

    def generate_code(self, message):
        """
        Sends a message to the llm
        :param message: The message that is sent
        :return: The response of the llm
        """
 
        # retrieved_docs = self.retriever.get_relevant_documents(message)
        # print(retrieved_docs[0].page_content)
        # return self.chain.invoke({'input': message, 'context': retrieved_docs[0].page_content})
        return self.chain.invoke({'input': message})
    
client = MinecraftCodeGenerator()
response = client.generate_code('build a house')
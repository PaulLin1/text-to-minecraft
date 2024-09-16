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

load_dotenv(find_dotenv())

def get_schematic_names(directory):
    schematic_names = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r') as f:
                data = json.load(f)

                schematic_name = data.get('schematic_name')
                
                if schematic_name:
                    schematic_names.append(schematic_name)

    return schematic_names

summaries = get_schematic_names('./data/filtered_schematics_json')
loader = DirectoryLoader(
    './data/filtered_schematics_json', 
    loader_cls=JSONLoader, 
    loader_kwargs={
        'jq_schema': '.blocks',
        'text_content': False
    }
)
docs = loader.load()

# Initialize an empty vectorstore
vectorstore = Chroma(
    collection_name="summaries",
    embedding_function=OpenAIEmbeddings()
)

store = InMemoryByteStore()
id_key = "doc_id"

retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,
)

doc_ids = [str(uuid.uuid4()) for _ in docs]

summary_docs = [
    Document(page_content=s, metadata={id_key: doc_ids[i]})
    for i, s in enumerate(summaries)
]

# Add documents to the vectorstore
retriever.vectorstore.add_documents(summary_docs)
retriever.docstore.mset(list(zip(doc_ids, docs)))

# Serialize only the retriever's components that are serializable
with open('data_docs.pickle', 'wb') as file:
    pickle.dump({
        'doc_ids': doc_ids,
        'docs': docs,
        'summaries': summaries
    }, file)

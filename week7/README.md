# Week 7: Building in Minecraft - Retrieval Augmented Generation (Part 3)

Welcome to Week 7 of our **Text-to-Minecraft** project! This week, we’ll be ending our journey into **Retrieval Augmented Generation** (RAG). At the end of this week, you should be able to use the JSON file you downloaded to assist your bot in creating new structures.

---

## Your Mission This Week

1. Quickly review RAG
2. Learn how we have to modify the basic structure for this project
3. Finish implementing it!

---

    ## 1. What is RAG again?!?!

In case you forgot, RAG is a technique to use documents to provide extra context for the base model. For example, a company may use RAG to give its AI chatbot information about its terms of service. This is a crucial because LLM's are not trained on that company's terms of service. This allows the company to have a personalized chatbot without having to trin a whole new model. AI training is often criticized for its steep cost and affects on the environment. However, with tools like RAG and finetuning, we can reuse pre-trained models for completely new purposes.

If you want a deeper introduction to RAG, rewatch the videos from week 5. This will give you all the information you need to continue with this week's content.

---

## 2. Difference in this Project

In the example above, data is often split up into chunks. This makes it more manageable for indexing and retrieval. However, for this project, we would like to use the entire document because each one pertains to a single topic.

Additionally, we need to change the way each document is represented. When documentsa are usually indexed, all the words have an embedding. But for the minecraft schematics, the only part that represents the document is the part "schematic name". Knowing this, we can use a summary of the document (the schematic name) as the index of the document. This substaianlly lowers the amount of time it takes to retrieve a document because the agent is looking at small part of it.

Knowing this, lets get started implementing it!

---

## 3. Implementing Structured Output

Let's use this example from the LangChain documentation as a starting point: https://python.langchain.com/docs/tutorials/rag/

The first thing you'll notice is that they are getting data from a website and parsing it. Lets change that to a document loader.

summaries = get_schematic_names('./data/filtered_schematics_json')
loader = DirectoryLoader(
    './data/filtered_schematics_json', 
    loader_cls=JSONLoader, 
    loader_kwargs={
        'jq_schema': '.blocks',
        'text_content': False
    }
)

Next, we can skip the text splitting part. We want all our documents to be on the same document.

After that we will have to create our summaries for indexing. Let's first extract the summaries from the JSON files.

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

We can use them like this.

doc_ids = [str(uuid.uuid4()) for _ in docs]

summary_docs = [
    Document(page_content=s, metadata={id_key: doc_ids[i]})
    for i, s in enumerate(summaries)
]

retriever.vectorstore.add_documents(summary_docs)
retriever.docstore.mset(list(zip(doc_ids, docs)))

As you can see, we are using the 'summaries' to index the document. But we are still adding the entire document to the vectorstore.

Lastly, we would need to add it into our chain. In the example they are not using a prompt template like us. However, if you scroll down on that page, you can find an example where they do!

This was a pretty bare bones explanation, but everything you need to know is in this document and that link. You should have already gotten a good introduction in week 5!

---

After implementing this, everything should be ready now! Try this out and see if it works!

--- 

Feel free to reach out if you have any questions or need further assistance!

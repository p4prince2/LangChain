from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from ollama import chat
from langchain_core.runnables import RunnableParallel 

#### ************************************************************************************SQL***********************************************************************************

def sql_text(text_input):
    embedding = OllamaEmbeddings(model="nomic-embed-text")

    vector_store = FAISS.load_local(
        "faiss_index",
        embedding,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 1})


    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    prompt = PromptTemplate(
        template="""
    You are an SQL assistant.

    Use ONLY the provided context.

    Rules:
    1. If the SQL query exists in the context, return ONLY that SQL query.
    2. Do not explain.
    3. Do not rewrite the question.
    4. Do not generate a new query.
    5. If the SQL query is missing, reply exactly:
    I don't know.

    Context:
    {context}

    Question:
    {question}

    SQL:
    """,
        input_variables=["context", "question"],
    )


    parallel_chain = RunnableParallel({
        'context': retriever ,
        'question': RunnablePassthrough()
    })

    parser = StrOutputParser()

    main_chain = parallel_chain | prompt | llm | parser


    response = main_chain.invoke(text_input)
    return response






# def image_input( image_path):

#     system_prompt = """
#     Act as an expert OCR and data extraction assistant.

#     Please format your response clearly using the following headings:

#     ### User Statement
#     Extract the introductory text written by the user at the very top of the image.

#     ### Question Description
#     Extract the problem statement from the left-hand panel under the Description tab.

#     ### SQL Query
#     Extract the exact SQL code written inside the dark-themed code editor on the right.

#     ### Error Message
#     Extract the red error message displayed at the bottom right.
#     """

#     response = chat(
#         model="qwen2.5vl:7b",
#         messages=[
#             {
#                 "role": "system",
#                 "content": system_prompt
#             },
#             {
#                 "role": "user",
#                 "content": "Extract all requested information from this image.",
#                 "images": ["sql_eorror.png"]
#             }
#         ]
#     )

#     response_image_test =response.message.content


#     llm = ChatOllama(
#         model="llama3.2",
#         temperature=0
#     )


#     embedding = OllamaEmbeddings(model="nomic-embed-text")

#     vector_store = FAISS.load_local(
#         "faiss_index",
#         embedding,
#         allow_dangerous_deserialization=True
#     )

#     retriever = vector_store.as_retriever(
#         search_type="similarity",
#         search_kwargs={"k": 1}
#     )




#     prompt = PromptTemplate(
#         template="""
#     You are an SQL assistant.

#     Use ONLY the provided context.

#     Rules:
#     1. If the SQL query exists in the context, return ONLY that SQL query.
#     2. Do not explain.
#     3. Do not rewrite the question.
#     4. Do not generate a new query.
#     5. If the SQL query is missing, reply exactly:
#     I don't know.

#     Context:
#     {context}

#     Question:
#     {question}

#     SQL:
#     """,
#         input_variables=["context", "question"],
#     )


#     parallel_chain = RunnableParallel({
#         'context': retriever ,
#         'question': RunnablePassthrough()
#     })

#     parser = StrOutputParser()

#     main_chain = parallel_chain | prompt | llm | parser


#     response = main_chain.invoke(response_image_test)
#     return response




def sql_image(image_path):

    # --------------------------------------------------
    # STEP 1 : Extract ONLY the SQL question
    # --------------------------------------------------
    system_prompt = """
You are an OCR assistant.

Your job is to read the screenshot and extract ONLY the SQL problem statement.

Rules:
- Ignore the SQL editor.
- Ignore the error message.
- Ignore buttons.
- Ignore the database output.
- Ignore everything except the Question Description.

Return ONLY the question text.
Do not add headings.
Do not explain anything.
"""

    response = chat(
        model="qwen2.5vl:7b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": "Extract only the SQL question.",
                "images": [image_path]
            }
        ]
    )

    extracted_question = response.message.content.strip()

    print("\nExtracted Question:\n")
    print(extracted_question)

    # --------------------------------------------------
    # STEP 2 : Load LLM
    # --------------------------------------------------

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    # --------------------------------------------------
    # STEP 3 : Load Embeddings
    # --------------------------------------------------

    embedding = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_store = FAISS.load_local(
        "faiss_index",
        embedding,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":3}
    )

    # --------------------------------------------------
    # STEP 4 : Prompt
    # --------------------------------------------------

    prompt = PromptTemplate(
        template="""
You are an SQL assistant.

Use ONLY the retrieved context.

Rules:

1. Return ONLY the SQL query.
2. No explanation.
3. No markdown.
4. Do not rewrite the question.
5. If the answer is not present in the context, reply exactly:

I don't know.

Context:
{context}

Question:
{question}

SQL:
""",
        input_variables=["context", "question"],
    )

    # --------------------------------------------------
    # STEP 5 : Chain
    # --------------------------------------------------

    parallel_chain = RunnableParallel(
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
    )

    parser = StrOutputParser()

    main_chain = (
        parallel_chain
        | prompt
        | llm
        | parser
    )

    # --------------------------------------------------
    # STEP 6 : Retrieve using ONLY the extracted question
    # --------------------------------------------------

    response = main_chain.invoke(extracted_question)

    return response





def sql_text_image(question, image_path):
    # --------------------------------------------------
    # STEP 1 : Extract ONLY the SQL question from the image
    # --------------------------------------------------
    sql_answer1 = sql_image(image_path)
    sql_answer2 = sql_text(question)

    # --------------------------------------------------
    # STEP 2 : Combine the extracted question and the text input
    # --------------------------------------------------
    # Build the Parallel Chain
    prompt = f"""
You are an SQL expert.

Image SQL:
{sql_answer1}

User Question:
{sql_answer2}

Use BOTH pieces of information to produce the final SQL answer.

Output exactly in this format:

Kindly go through the provided information.
<final_answer> -> By Prince Kushwaha

Do not include any explanation or markdown.
Replace <final_answer> with the actual SQL answer.
"""
    

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )
    response = llm.invoke(prompt)

    return response.content





### *************************************************************************Excel**************************************************************************



def excel_text(question):
    ...

def excel_image(image_path):
    ...

def excel_text_image(question, image_path):
    ...
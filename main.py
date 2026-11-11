
# Import necessary libraries

# Document loaders
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# LLM
from langchain_ollama import ChatOllama

# Prompts
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Hugging Face embeddings
from langchain_huggingface import HuggingFaceEmbeddings

# FAISS vector database
from langchain_community.vectorstores import FAISS

# Chains
from langchain_classic.chains import (
    RetrievalQA,
    create_history_aware_retriever,
    create_retrieval_chain,
    LLMChain
)

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain
)

# Chat history
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Flask
from flask import Flask, render_template, request, redirect, url_for

# Other libraries
import os
from werkzeug.utils import secure_filename


# LLM
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
    num_ctx=2048,
    num_predict=256,
    keep_alive="30m"
)


# Text splitter
text_splitter = RecursiveCharacterTextSplitter(
    separators='\n',
    chunk_size=2000,
    chunk_overlap=100,
    length_function=len
)


# Embeddings
embeddings = HuggingFaceEmbeddings()


# Flask application
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Extract text from PDF
def extract_text_from_pdf(pdf_path):

    with open(pdf_path, 'rb') as file:

        reader = PyPDF2.PdfReader(file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# Resume summary template
resume_summary_template = '''
Role: You are an AI Career coach.

Task: Given the candidate's resume, provide a comprehensive summary
that includes the following key aspects:

Career objective
Skills and Expertise
Professional Experience
Education Background
Notable Achievements

Instructions:
Provide a concise summary of the resume, focusing on the candidate's
skills, experience and career trajectory. Ensure the summary is
well-structured, clear and highlights the candidate's strengths
in alignment with industry standards.

Resume:
{resume}
'''


# Resume prompt
resume_prompt = ChatPromptTemplate.from_template(
    resume_summary_template
)


# LLM Chain
resume_analysis_chain = LLMChain(
    llm=llm,
    prompt=resume_prompt
)


# Perform QA
def perform_qa(query):

    db = FAISS.load_local(
        "vector_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_type='similarity',
        search_kwargs={"k": 4}
    )

    rqa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
        return_source_documents=True
    )

    result = rqa.invoke({"query": query})

    return result['result']


# Home route
@app.route('/')
def index():
    return render_template('index.html')


# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == "":
        return redirect(url_for('index'))

    if not file.filename.lower().endswith('.pdf'):
        return "Please upload a PDF file."

    # Save uploaded file
    filename = secure_filename(file.filename)

    file_path = os.path.join(
        app.config['UPLOAD_FOLDER'],
        filename
    )

    file.save(file_path)

    # Extract text from PDF
    resume_text = extract_text_from_pdf(file_path)

    if not resume_text.strip():
        return "No readable text found in PDF."

    # Split text
    splitted_text = text_splitter.split_text(resume_text)

    # Create FAISS vector database
    vectorstore = FAISS.from_texts(
        splitted_text,
        embeddings
    )

    vectorstore.save_local('vector_index')

    # Resume analysis
    resume_analysis = resume_analysis_chain.run(
        resume=resume_text
    )

    return render_template(
        'results.html',
        resume_analysis=resume_analysis
    )


# Ask questions route
@app.route('/ask', methods=['GET', 'POST'])
def ask_query():

    if request.method == 'POST':

        query = request.form['query']

        result = perform_qa(query)

        return render_template(
            'qa_results.html',
            query=query,
            result=result
        )

    return render_template('ask.html')


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)

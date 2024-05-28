from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationSummaryBufferMemory
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnablePassthrough

# PDF 파일 불러오기
loader = PyPDFLoader("./static/download/resume.pdf")
docs=loader.load()
print(docs)
exit()


# Chunk(block) 단위로 Split(쪼개기)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = loader.load_and_split(text_splitter)

# 임베딩 → 형태소를 숫자로 표현!
#   ex) 5차원 텍스트 임베딩
#       dog : 0.3 0.7 1.5 59 32
embeddings = OpenAIEmbeddings()

cache_dir = LocalFileStore("./.cache/")
cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)
vectorstore = Chroma.from_documents(docs, cached_embeddings)

# Vector DB: Chroma 저장
directory = "./llm/chroma_db"
vector_index = Chroma.from_documents(
    docs,                           # Documents
    OpenAIEmbeddings(),             # Text embeddings model
    persist_directory=directory     # file system(저장경로)
)
vector_index.persist()  # Save        
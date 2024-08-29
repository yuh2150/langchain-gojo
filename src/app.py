import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langserver import add_routes

from src.base.llm_models import get_llm
# from src.rag.main impor

llm = get_llm(temperature=0.9)


app = FastAPI(
    title = "Gojo Server",
    version = "1.0",
    description = "A simple Gojo AI-powered language server",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
 
)

@app.get("/check")
async def check():
    return {"status": "Server is running"}


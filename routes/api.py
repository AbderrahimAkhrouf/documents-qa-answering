from fastapi import APIRouter
from src.endpoints import qa_answering

router = APIRouter()
router.include_router(qa_answering.router)
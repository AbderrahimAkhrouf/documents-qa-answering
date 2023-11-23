import openai
import timeit
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
    StorageContext,
    ServiceContext
)
from llama_index.llms import OpenAI
from llama_index.indices.query.schema import QueryBundle
from fastapi import APIRouter, Request, status
from src.models.answer_model import answer
from dotenv import dotenv_values

config = dotenv_values("config/.env")

openai.api_key = config["API_KEY"]

router = APIRouter(prefix='/question_answer',tags=["answring questions based on db"])
@router.post(
    '/',
    response_description='questions answering db based',
    status_code=status.HTTP_200_OK,
    response_model=answer
)
def generate_answer(
    request : Request, text : str
) :
    # choisir un LLM
    llm = OpenAI(temperature=0.01, model='gpt-4')
    service_context = ServiceContext.from_defaults(llm=llm)

    # loader les documents
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)

    # Enregistrer les index
    index.set_index_id("vector_index")
    index.storage_context.persist("storage")


    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context,index_id="vector_index")

    # Traitement du query
    start = timeit.default_timer()
    query_bundle = QueryBundle(
        query_str=text
    )
    query_engine = index.as_query_engine()

    # Génération de la réponse
    response = query_engine.query(query_bundle)
    end = timeit.default_timer()
    dur = (end - start)/60

    test = {"response" : str(response), "sources": str(response.get_formatted_sources()), "time" : dur}

    return test



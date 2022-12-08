from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

from src.inference import generate_question, get_model_and_tokenizer

app = FastAPI()


class QuestionRequest(BaseModel):
    context: str
    answer: str


class QuestionResponse(BaseModel):
    question: str


weights_path = Path("model_weights")

model, tokenizer = get_model_and_tokenizer(weights_path)


@app.get("/")
def index():
    return {"message": "Hello World!!"}


@app.post("/getquestion", response_model=QuestionResponse)
def generate_question_api(request: QuestionRequest):
    context = request.context
    answer = request.answer
    ques = generate_question(context, answer, model, tokenizer)
    return QuestionResponse(question=ques)

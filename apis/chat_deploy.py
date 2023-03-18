import uvicorn
import json
from argparse import ArgumentParser
from fastapi import FastAPI
from pydantic import BaseModel
from models.chat import(
    load_model,
    predict
)

app = FastAPI(
    title = 'sk gpt'
)

class ChatInput(BaseModel):
    text: str

class ChatOutput(BaseModel):
    chatting: str

@app.post("/chat", response_model=ChatOutput)
async def predict_chat(input: ChatInput):
    text = input.text
    result = predict(inputs= text, tokenizer=tokenizers, model=models)
    return ChatOutput(chatting=result)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/v0.0.1-chat.json")
    parse = parser.parse_args()
    config_path = parse.config
    config = json.load(open(config_path, encoding='utf-8'))

    tokenizers, models = load_model(config['chat']['model_name'])
    print("[=!=]chat model loaded[=!=]")
    uvicorn.run(app, host="0.0.0.0", port=config['deploy_port'])

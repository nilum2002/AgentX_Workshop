import os
from typing import List
from fastapi import FastAPI, HTTPException, Request
from dotenv import load_dotenv
import Agent as Agent
import json
from fastapi.middleware.cors import CORSMiddleware
# load the json file 
# with open("r.json", "r") as file:
#     data = json.load(file)



load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/ask")

async def ask_agent(request: Request):
    data = await request.json()
    question = data.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required")
    try:
        response = Agent.agent.run(str(data["question"]))
        print("Agent response:", response)
        
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # return {"response": data}

    
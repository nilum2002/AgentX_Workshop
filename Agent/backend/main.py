import os
from typing import List
from fastapi import FastAPI, HTTPException, Request
from dotenv import load_dotenv
import Agent as Agent



# print(Agent.agent.run("What is the capital of France?"))
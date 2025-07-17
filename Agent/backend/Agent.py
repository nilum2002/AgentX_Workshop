import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain_groq import ChatGroq
from fastapi import FastAPI
app = FastAPI()


# the graq api 
GROQ_API = "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"
os.environ["GROQ_API_KEY"] = GROQ_API

# set up the OpenAI LLM
llm = ChatGroq(model="llama3-70b-8192", temperature=0.7)

VERBOSE = False


# function to analyze the feedback
def commnet_on_feedback(feedback):
    return f"Here's a commnt on the feedback: \"{feedback}\" "

# wrapping the langchian too
feedback_tool = Tool(
    name = "Feedback Commentor",
    func=commnet_on_feedback,
    description="use this to analyze and comment on the customer feedback"
)

agent = initialize_agent(
    tools= [feedback_tool],
    llm = llm,
    agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose =  VERBOSE 
)

# smaple feedback 
customer_feedback = "The app craches every time I try to upload a photo It's really frustrating"
# response = agent.run(f"please comment professionally on this customer feedback: '{customer_feedback}'")
# print(response)
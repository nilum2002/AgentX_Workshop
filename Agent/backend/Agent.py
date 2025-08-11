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
    description="This AI assistant generates short, polite, and context-aware replies to customer feedback for our noodle restaurant. It should always acknowledge the customer’s comment, show appreciation for their time, and match the tone to the feedback—warm and grateful for positive comments, empathetic and apologetic for negative ones. Keep responses under 2 sentences, use friendly language, and make the customer feel heard and valued, dont give response like this **Here is the complete response to the customer's feedback:** "
)

agent = initialize_agent(
    tools= [feedback_tool],
    llm = llm,
    agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose =  VERBOSE 
)

# smaple feedback 
# customer_feedback = "The app craches every time I try to upload a photo It's really frustrating"
# response = agent.run(f"please comment professionally on this customer feedback: '{customer_feedback}'")
# print(response)
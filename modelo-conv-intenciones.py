import streamlit as st
from dotenv import load_dotenv
import os
import json

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

load_dotenv()
ls_prediction_endpoint = os.getenv('LS_CONVERSATIONS_ENDPOINT')
ls_prediction_key = os.getenv('LS_CONVERSATIONS_KEY')
cls_project = os.getenv('PROJECT_NAME')
deployment_slot = os.getenv('DEPLOYMENT_NAME')

# Create a client for the Language service model
client = ConversationAnalysisClient(
    ls_prediction_endpoint, 
    AzureKeyCredential(ls_prediction_key)
)

## Lanzar programa con `streamlit run modelo-conv-intenciones.py`

def devolver_intenciones(intencion):
    with client:
        query = intencion
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": cls_project,
                    "deploymentName": deployment_slot,
                    "verbose": True
                }
            }
        )

    top_intent = result["result"]["prediction"]["topIntent"]
    intents = result["result"]["prediction"]["intents"]
    entities = result["result"]["prediction"]["entities"]
    score = result["result"]["prediction"]["intents"][0]["confidenceScore"]

    result_json = {
            "query": query,
            "top_intent": top_intent,
            "score": score,
            "intents": intents,
            "entities": entities,
        }

    return result_json



st.title("Intent Recognition for a Restaurant")

st.write("Ask about the reservations or the menu.")

with st.sidebar:
    st.title("Example Questions")
    st.header("1. Asking About the Menu")
    st.text("What are your most popular dishes?")
    st.text("Do you have any vegetarian or vegan options?")
    st.text("Are there any daily specials or seasonal items?")
    st.text("Can you accommodate food allergies or dietary restrictions?")
    st.text("Do you serve fish in your menu? What about meat?")
    st.divider()
    st.header("2. Making a Reservation")
    st.text("Do you have a table available for 10 people on Friday at 11pm?")
    st.text("Can I book a dinner for Tuesday?")
    st.text("I urgently need to get a table fom 20 people, can you help me?")
    st.text("Can I get a table tomorrow at 10pm?")
    st.text("Can I get a table by the window?")
    st.divider()
    st.header("3. Modifying a Reservation")
    st.text("Can I change my reservation to a different time?")
    st.text("Is it possible to add more people to my reservation?")
    st.text("Can I switch my terrace table to a table by the window?")
    st.text("Can I change my reservation today at 8pm to tomorrow at 9pm?")
    st.text("Can I change my table from 10 to 20 people?")
    st.divider()
    st.header("4. Cancelling a Reservation")
    st.text("I want to cancel my reservation for tomorrow.")
    st.text("I want to cancel my reservation for 10 people.")
    st.text("My girlfriend left me, I dont want the table anymore.")
    st.text("Can I cancel online or do I need to call the restaurant?")
    st.text("Will you cancel my reservation for tonight at 11pm?")
    st.divider()
    st.header("5. Consulting the Availability")
    st.text("Do you have any tables available for tonight?")
    st.text("How far in advance do I need to book a table for the weekend?")
    st.text("Is there a waitlist if no tables are available?")
    st.text("What are your least busy times for walk-ins?")
    st.text("Do you offer outdoor seating, and is it available now?")
    

pregunta = st.text_input("Write your question:")

if st.button("Ask!", icon=":material/trending_flat:"):
    st.json(devolver_intenciones(pregunta), expanded=1)

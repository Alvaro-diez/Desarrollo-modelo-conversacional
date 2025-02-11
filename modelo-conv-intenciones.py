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

pregunta = st.text_input("Write your question:")

if st.button("Ask!", icon=":material/trending_flat:"):
    st.json(devolver_intenciones(pregunta), expanded=1)

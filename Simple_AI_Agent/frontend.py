# from dotenv import load_dotenv
# load_dotenv()

#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

st.set_page_config(page_title="Rejo's AI Agent", layout="centered")
st.title("Rejo's AI agent")
st.write("Create and interact with the AI agent")
system_prompt=st.text_area("Define your AI agent: ", height=70, placeholder="Type your system prompt here")

MODEL_NAMES_GROQ = ["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-3.5-turbo","gpt-4o-mini"]

provider=st.radio("Select Provider:", ("Groq", "OpenAI"))
if provider=="Groq":
    selected_model = st.selectbox("Select the Groq model", MODEL_NAMES_GROQ)
elif provider=="OpenAI":
    selected_model = st.selectbox("Select the OpenAI model", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Ask Agent: ", height=150, placeholder="Ask Anything!")

API_URL="http://127.0.0.1:8001/chat"
if st.button("Ask Agent"):
    if user_query.strip():

        import requests
        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        response=requests.post(API_URL, json=payload)
        if response.status_code==200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response** {response_data}")
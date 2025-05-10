import streamlit as st
import requests
from io import BytesIO

st.set_page_config(page_title="Theory2Real", layout="centered")

# Add a logo at the top
st.image("https://bernardmarr.com/wp-content/uploads/2021/07/5-Reasons-Why-Artificial-Intelligence-Really-Is-Going-To-Change-Our-World.png", width=700)

st.title("Theory2Real - AI Powered Learning")
st.subheader("Enter a topic to explore its real-world use, visuals, and videos")

# Retrieve API key securely from Streamlit secrets
api_key = st.secrets["OPENROUTER_API_KEY"]
topic = st.text_input("Enter a learning topic:")

# Add a "Search" button
if st.button("Search"):
    if topic:
        # --- AI Explanation via OpenRouter ---
        st.subheader("AI Explanation")
        openrouter_headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": f"Explain the topic '{topic}' in simple words. Include how it is used in real-world, small project idea, and fields it is useful in."}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=openrouter_headers, json=data)
        if response.ok:
            explanation = response.json()["choices"][0]["message"]["content"]
            st.markdown(explanation)
        else:
            st.error("Failed to get AI explanation")

        # --- YouTube Video Search ---
        st.subheader("YouTube Learning Video")
        yt_query = topic.replace(" ", "+")
        st.markdown(f"[Click here to search on YouTube](https://www.youtube.com/results?search_query={yt_query})")
    else:
        st.warning("Please enter a topic to search.")
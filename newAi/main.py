import streamlit as st
from dotenv import load_dotenv
import os
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests
import re
import os
import openai
import time

load_dotenv()
def clean_text_from_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove unwanted elements
        for tag in soup(['script', 'style', 'noscript', 'header', 'footer', 'form', 'svg', 'nav', 'aside']):
            tag.decompose()
        
        # Extract paragraph text
        paragraphs = soup.find_all('p')
        text = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        
        return text[:150]
    except Exception as e:
        return f"[Failed to fetch from {url}]: {str(e)}"


def get_combined_text(query, num_results=5):
    all_text = ""
    ddgs = DDGS()
    results = ddgs.text(query, max_results=num_results)
    
    for res in results:
        url = res.get("href")
        if url:
            print(f"Scraping: {url}")
            cleaned = clean_text_from_url(url)
            all_text += f"\n\n--- Content from {url} ---\n\n{cleaned}"
    
    return all_text

def duckSearh(content):
    combined_text = get_combined_text(content)
    return combined_text


def main(query):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "[Error: OPENAI_API_KEY environment variable not set. Please set your OpenAI API key.]"

    system_prompt = (
        "You are a political events AI assistant. Your job is to answer only questions about political events. "
        "For every answer:\n"
        "- Use only verifiable facts from reputable sources (news APIs, government data, etc.).\n"
        "- Provide proper citations (with URLs) for every factual claim.\n"
        "- On partisan issues, always present both Republican and Democratic viewpoints, clearly separated and neutrally worded.\n"
        "- Explicitly check for and correct any partisan language or framing.\n"
        "- If you cannot maintain strict neutrality or provide citations for every claim, politely refuse to answer.\n"
        "- If a question is not about political events, politely refuse and explain your scope.\n"
        "- Never make up facts or hallucinate information. If you cannot verify something, say so.\n"
        "- For legislative, election, or court questions, include dates, vote counts, and official statements where possible.\n"
        "- Always maintain strict neutrality and avoid partisan framing.\n"
        "- If you are unsure about neutrality or citation, state your uncertainty and ask for clarification."
    )

    context = duckSearh(query)
    context = context + "use this to answer the question > "
    content = context + "ApiResponse"

    # print(len(context))

    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context + query}
            ],
            temperature=0.2,
            max_tokens=800,
        )
        content = response.choices[0].message.content
        if content:
            return content.strip()

    # return "Sample response"
        else:
            return "[OpenAI API returned no content in the response.]"
    except Exception as e:
        return f"[OpenAI API error: {e}]"

if __name__ == "__main__":
    
    # UI elements
    st.header("Chatbot tool")
    user_input = st.text_input("Enter Your Prompt")

    if st.button("Response"):
        start_time = time.time()
        
        with st.spinner("Processing..."):
            response = main(user_input)
        
        end_time = time.time()
        elapsed = int(end_time - start_time)

        # Format time
        if elapsed < 60:
            st.success(f"Done in {elapsed} seconds.")
        else:
            minutes = elapsed // 60
            seconds = elapsed % 60
            st.success(f"Done in {minutes} minute(s) and {seconds} second(s).")
        
        # Show the response
        st.write(response)
from langchain_anthropic import chatAnthropic
import os


model = chatAnthropic(model="claude-3-7-sonnet-20250219", api_key=os.getenv("ANTHROPIC_API_KEY"))

query = "What is gravity?"

response = model.invoke(query)

print(response.content)
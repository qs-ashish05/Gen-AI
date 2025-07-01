from langchain_core.prompts import ChatPromptTemplate


# 1. Define a prompt template with system and human messages
chat_prompt = ChatPromptTemplate([
    ('system', 'You are a helpful assistant knowledgeable in {domain}'),
    ('human',"Can you explain the concept of {topic}?")
])

# 2. Provide values for the input variables
input_values = {
    "domain": "machine learning",
    "topic": "gradient descent"
}

# 3. Format the prompt using the values
formatted_prompt = chat_prompt.invoke(input_values)

# 4. Print the resulting prompt
print(formatted_prompt)

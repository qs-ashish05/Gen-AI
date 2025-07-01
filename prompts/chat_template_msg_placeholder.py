from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# chats = [
#     HumanMessage(content="i want refund for my order id #1234"),
#     AIMessage(content="refund for id #1234 is initiated you will get 4 to 5 hrs")
# ]

# # chattemplate
# chat_template = ChatPromptTemplate([
#     ('sytem', 'you are an restaurant booking chatbot'),
#     MessagesPlaceholder(variable_name='chats')
#     ('human', '{query}')
# ])

# # load the chathistory


# print(chat_template)



prompt = MessagesPlaceholder("history")
prompt.format_messages() # raises KeyError

prompt = MessagesPlaceholder("history", optional=True)
prompt.format_messages() # returns empty list []

prompt.format_messages(
    history=[
        ("system", "You are an AI assistant."),
        ("human", "Hello!"),
    ]
)



prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder("history"),
        ("human", "{question}")
    ]
)
prompt.invoke(
   {
       "history": [("human", "what's 5 + 2"), ("ai", "5 + 2 is 7")],
       "question": "now multiply that by 4"
   }
)

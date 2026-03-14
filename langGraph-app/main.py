from langchain_core.messages import HumanMessage
from graph import graph

result = graph.invoke({
    "messages": [HumanMessage(content="hello")]
})

print(result["messages"][-1].content)
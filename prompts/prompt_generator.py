from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    template="""
    Explain the research topic {paper_name} with the following specifications
    Explaination Style: {input_style}
    Explaination Length: {explaination_length}
    Include relavernt maths accordingly,
    Include relavent examples 

    If you dont know about certain Topics then response with "Insufficeient contens available" instead of gusessing and producing wrong responses,
    Ensure the summary is clear, easy and aligned with the query asked
""",
input_variables = ['paper_name', 'input_style', 'explaination_length'],
validate_template=True
)

prompt_template.save("example.json")
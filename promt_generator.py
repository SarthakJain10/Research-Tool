from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template='''
Please summarize the reaserch paper titled "{paper_input}" with the following specifications:
Explanation style: {style_input}
Explanation length: {length_input}
1. Mathematical details:
    -Include relevant mathematical details if present in the paper
    -Explain the mathematical concept using simple intuitive code snippets where applicable
2. Analogies:
    -use relatable analogies to complex ideas
If certain information is not available in the paper respond with: "Insuficiant information"
Ensure the summary is clear, accurate and aligned with the provided style and length.
''',
input_variables = ['paper_input', 'style_input', 'length_input'],
validate_template = True
)

template.save('template.json')
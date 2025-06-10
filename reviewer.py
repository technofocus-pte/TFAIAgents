# reviewer.py

import os
from openai import AzureOpenAI

def review_code(code_snippet):
    client = AzureOpenAI(
        api_key=os.getenv('AZURE_OPENAI_KEY'),
        endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )

    prompt = f"Review the following code snippet and provide feedback:\n\n{code_snippet}"

    response = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

print(review_code("def add(x, y): return x + y"))

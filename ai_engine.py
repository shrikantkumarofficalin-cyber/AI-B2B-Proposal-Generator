import openai
from prompt_template import generate_prompt

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_proposal(company, industry, budget):

    prompt = generate_prompt(company, industry, budget)

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
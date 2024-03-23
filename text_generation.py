from openai import OpenAI

client = OpenAI(api_key='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')

# Generate a text completion
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": "be an expert about music festival in taiwan"},
        {"role": "user", "content": prompt},
        ]
    )
   return completion.choices[0].message.content

prompt=input("Enter a prompt: ")
response = get_completion(prompt)
print(response)
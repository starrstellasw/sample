import streamlit as st 
from openai import OpenAI

client = OpenAI(api_key='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')

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"): 
    completion = client.chat.completions.create(
        model=model, 
        messages=[
            {"role": "system", "content": "taiwan travel guide"}, 
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

# create our streamlit app
with st.form(key = "chat"):
    prompt = st.text_input("Insert a description of the function of your completions function") # TODO!
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))

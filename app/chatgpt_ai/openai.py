from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')


def chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  #gpt-3.5-turbo or text-davinci-003 (change to different endpoint)
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=1000
    )
    response_dict = response.get('choices')
    if response_dict and len(response_dict) > 0:
        prompt_response = response.choices[0].message.content
    return prompt_response

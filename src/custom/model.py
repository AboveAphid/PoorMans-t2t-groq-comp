'''
Class implementing interface for AI T2T models running on Groq servers!

"model" will be one of Groq's models such as 'llama3-8b-8192'.
Your a poor man! You think there's finetuning? Hahahahahaha
Make sure you have your groq token is in your ".env" as specified in the ".env-template"
'''

from groq import Groq
import logging

class GroqModel():
    def __init__(self, api_key, model_name):
        self.client = Groq(
            api_key=api_key
        )
        self.model_name = model_name

    def __call__(self, sys_prompt, user_prompt):
        messages=[
            { "role": "system", "content": sys_prompt },
            { "role": "user", "content": user_prompt }
        ]

        logging.debug(f"Sending messages: {messages}")
        stream = self.client.chat.completions.create(
            messages=messages,
            model=self.model_name,
            stream=True
        )

        logging.debug(f"Streaming results")
        full_response = ""
        for chunk in stream:
            content_chunk = chunk.choices[0].delta.content or ""
            full_response += content_chunk
            yield content_chunk
        logging.debug(f"Finished with full response: {full_response}")
from odoo import fields, models
import requests
from openai import OpenAI

class IziOpenAIModels(models.Model):
    _name = 'chatgpt.message'

    name = fields.Char('Name')
    message = fields.Text('Message')
    response = fields.Text('Response')

    def send_message(self):
        secret_key = ''
        client = OpenAI(api_key=secret_key)
        msg_to_send = self.message
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": msg_to_send},
            ]
        )
        
        if response and 'choices' in response and response['choices']:
            self.response = response['choices'][0]['message']['content']
        else:
            self.response = "No response from OpenAI"

        return True

from requests import post
from os import getenv
from datetime import datetime


class Discord:
    def __init__(self):
        self.discord_url = getenv('DISCORD_WEBHOOK_URL') + 'FdhvFVnSZN9-lVb0iEqzKbIILC7aLzyAJ2lSLn2LagorNnhUBa-vCMkNA8ajuzeh37DZ'

        self.headers = {
            'Content-Type': 'application/json'
        }

    def send_embed(self, data):
        response = post(self.discord_url, headers=self.headers, json=data)
        return response
    
    def notify_dev(self, data):
        json_data = {
            'embeds': [
                {
                    'title': f'Started By {getenv("USERNAME")} at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                    'description': f'csv: {data}',
                    'color': 0x00ff00
                }
            ]
        }

        response = self.send_embed(json_data)

    def log_sent_message(self, name, message, caption, count):
        json_data = {
            'embeds': [
                {
                    'title': f'Message Sent to {name}',
                    'description': f'Message: {message}\nCaption: {caption}',
                    'color': 0x8742f5
                }
            ]
        }

        response = self.send_embed(json_data)
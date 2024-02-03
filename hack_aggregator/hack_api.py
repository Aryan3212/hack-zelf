import requests
import time
from .models import Content, Author
from dotenv import load_dotenv
import os

load_dotenv()

headers = { 'x-api-key': os.environ.get('HACK_API_KEY') }
base_url = os.environ.get('HACK_API_BASE_URL')

def get_content_list(page):
    try:
        response = requests.get(base_url + '/contents?page=' + str(page) , headers=headers )
        return response
    except Exception as e:
        return e
    
def get_author(authorId):
    try:
        response = requests.get(base_url + '/authors/' + authorId, headers=headers )
        return response
    except Exception as e:
        return e

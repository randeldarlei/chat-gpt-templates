import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return file.read()

def resumo(texto):
    response = openai.Completion.create(
        engine="",
        prompt="",
        temperature="",
        max_tokens="",
        top_p="",
        frequency_penalty="",
        presence_penalty="",
        stop=""
    )
    return response['choices'][0]['text']
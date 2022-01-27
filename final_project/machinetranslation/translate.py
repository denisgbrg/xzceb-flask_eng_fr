''' Final Project - testing Translator API'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VER = "2018-05-01"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VER,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    ''' Translate EN-FR via Watson Translate API'''
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']


def frenchToEngish(french_text):
    ''' Translate FR-EN via Watson Translate API'''
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']



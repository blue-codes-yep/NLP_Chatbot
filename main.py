import spacy
import requests

nlp = spacy.load("en_core_web_md")

doc = nlp("I live in Texas for the past two years.")


def get_weather(state, city):
    pass


def user_input():
    pass

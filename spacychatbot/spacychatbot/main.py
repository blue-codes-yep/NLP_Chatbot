import spacy
import requests

nlp = spacy.load("en_core_web_md")

topic_weather = nlp("Weather conditions in a city")
exit_conditions = nlp("End of conversation.")


def get_weather(city):
    open_weather_api = "http://api.openweathermap.org/data/2.5/weather/?appid=7bde52051f0e228e2831fdf8c1fce32e&q=" + city
    response = requests.get(open_weather_api)
    weather = response.json()["weather"][0]["description"]
    return("It's " + weather + " in " + city)


def take_user_input(user_input):
    # Convert user input into nlp document
    user_input = nlp(user_input)

    # Check similiarity thershold
    if user_input.similarity(topic_weather) >= 0.80:
        # Check entities with spacy
        for ent in user_input.ents:
            # Verify it's a geographical location.
            if ent.label_ == "GPE":
                city = ent.text
                return get_weather(city)
            else:
                return "Sorry If you're trying to get the weather for an area, I was not able to detect the location. Try again."
    else:
        if user_input.similarity(exit_conditions) >= 0.70:
            return "Okay, see ya later."
        else:
            return "Sorry I don't understand, Please try asking something again."

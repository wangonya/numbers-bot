# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import requests

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class GetNumberFactAction(Action):

    def name(self) -> Text:
        return "get_number_fact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number = tracker.get_slot('number')
        fact = requests.get(f'http://numbersapi.com/{number}')
        if fact.status_code != 200:
            dispatcher.utter_message("I'm sorry, I couldn't understand that 😞")
        else:
            dispatcher.utter_message(fact.text)

        return []


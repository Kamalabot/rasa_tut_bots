# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionSayBack(Action):
#
    def name(self) -> Text:
         return "action_say_back"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         name = tracker.get_slot('callname')
         city = tracker.get_slot('cityname')
         old = tracker.get_slot('howold')

         dispatcher.utter_message(text=f"You are {name}, from {city} {old} old!")

         return []

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
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionSayPhone(Action):

    def name(self) -> Text:
        return "action_say_phone"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        phone = tracker.get_slot('phone')
        if not phone:

            dispatcher.utter_message(text="There is no phone number!")

        else:

            dispatcher.utter_message(text=f"Your number is {phone}!")

        return []

class ActionSayData(Action):

    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name= tracker.get_slot('name')
        city = tracker.get_slot('city')
        dob = tracker.get_slot('DOB')
        print(name,city,dob)
        if not name or not city or not dob:

            dispatcher.utter_message(text="There is somed data missing!")

        else:

            dispatcher.utter_message(text=f"Hey {name}.I see you are from {city} and born on {dob}!")

        return []

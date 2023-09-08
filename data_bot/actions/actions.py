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
class ActionExtractData(Action):
#
    def name(self) -> Text:
        return "action_extract_data"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name1 = tracker.get_slot('Name1')
        name2 = tracker.get_slot('Name2')
        ph_1 = tracker.get_slot('Phone_num1')
        ph_2 = tracker.get_slot('Phone_num2')
        ph_3 = tracker.get_slot('Phone_num3')
        ph_4 = tracker.get_slot('Phone_num4')
        ph_5 = tracker.get_slot('Phone_num5')
        ph_6 = tracker.get_slot('Phone_num6')
        addr = tracker.get_slot('Address')

        dispatcher.utter_message(text=f"""Here are the details: 
                                        name_1 : {name1}
                                        name_2 : {name2}
                                        ph_1 : {ph_1}
                                        ph_2 : {ph_2}
                                        ph_3 : {ph_3}
                                        ph_4 : {ph_4}
                                        ph_5 : {ph_5}
                                        ph_6 : {ph_6}
                                        address : {addr}""")

        return []

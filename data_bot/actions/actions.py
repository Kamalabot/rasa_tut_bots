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

        ph_1 = tracker.get_slot('Phone_number')
        mail = tracker.get_slot('Mail')
        number = tracker.get_slot('Nums')

        dispatcher.utter_message(text=f"""Here are the details: 
                                        ph_1 : {ph_1}
                                        mail_id : {mail}
                                        number : {number}""")

        return []

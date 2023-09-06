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
class ActionOperateNums(Action):
#
    def name(self) -> Text:
        return "action_operate_nums"
#
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operator = tracker.get_slot('operation')
        num1 = tracker.get_slot('numone')
        num2 = tracker.get_slot('numtwo')
        
        if operator == 'sum' or operator == '+' or operator == 'add' or operator == 'plus':
            try:
                output = int(num1) + int(num2)
            except e as Exception:
                output = "recheck your input..."
        
        elif operator == 'difference' or operator == '-' or operator == 'minus' or operator == 'subtract':
            try:
                output = int(num1) - int(num2)
            except e as Exception:
                output = "recheck your input..."
        elif operator == 'product' or operator == '*' or operator == 'multiply' or operator == 'into':
            try:
                output = int(num1) * int(num2)
            except e as Exception:
                output = "recheck your input..."
        elif operator == 'division' or operator == '/' or operator == 'divide' or operator == 'by':
            try:
                output = int(num1) / int(num2)
            except e as Exception:
                output = "recheck your input..."
        else:
            output = "The operation requested is complex for me. Try a different bot"


        dispatcher.utter_message(text=f"Output: {output}")

        return []

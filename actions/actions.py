# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


import wikipedia
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class ActionWikipediaSearch(Action):
    def name(self) -> Text:
        return "action_wikipedia_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_input = tracker.latest_message.get('text')

        try:
            summary = wikipedia.summary(user_input, sentences=2)
            dispatcher.utter_message(text=summary)
        except wikipedia.exceptions.DisambiguationError:
            dispatcher.utter_message(text="Too many results found. Can you be more specific?")
        except wikipedia.exceptions.PageError:
            dispatcher.utter_message(text="I couldn't find anything about that.")
        except Exception:
            dispatcher.utter_message(text="Something went wrong while searching. Please try again.")
        
        return []


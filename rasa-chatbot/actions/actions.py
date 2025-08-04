from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCustomGreeting(Action):

    def name(self) -> str:
        return "action_custom_greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        dispatcher.utter_message(text="Hello! How can I assist you today?")
        return []


class ActionFetchData(Action):

    def name(self) -> str:
        return "action_fetch_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        # Here you would implement the logic to fetch data from a database or an API
        data = "Sample data fetched from the source."
        dispatcher.utter_message(text=data)
        return []
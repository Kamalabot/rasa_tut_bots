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
import pandas as pd

file_path = "/home/kamal/gitfolders/rasa_tut_bots/econobot/Countries_Economies.csv"
econ_df = pd.read_csv(file_path)

#Modifying the columns 
econ_df.columns = ['Country',
 'Poverty_headcount_ratio',
 'Life_expectancy_in_years',
 'Population',
 'Population_growth_in_Pc',
 'Net_migration',
 'Human_Capital_Index',
 'GDP_LCU',
 'GDP_per_capita_LCU',
 'GDP_growth_in_Pc',
 'Unemployment_Pc',
 'Inflation_Pc',
 'Personal_remittances_Pc',
 'CO2_emissions_Tons',
 'Forest_area_Pc_Land_Area',
 'Access_to_electricity_Pc',
 'Annual_freshwater_withdrawals_Pc',
 'Electricity_production_Pc',
 'Sanitation_services_Pc_of_population',
 'Intentional_homicides',
 'Central_government_debt_Pc_GDP',
 'SPI',
 'Individuals_with_Internet_Pc_Population',
 'Seats_held_by_women_in_national_parliaments_Pc',
 'FDI_Pc_of_GDP',
 'Unnamed']

#Accessing particular column data for a country

def data_access(country, column):
    if country not in econ_df.Country.unique():
        return 'Country not in list'

    if column not in econ_df.columns:
        return 'Column not in list for requested country'

    return econ_df[econ_df.Country == country][column].to_list()[0]

# Access the country lowest in a dimension
def lowest_in(column):
    "Which country is minimum in a dimension"

    if column not in econ_df.columns:
        return 'NA'

    minimum = econ_df[column].min()

    print(minimum)

    return econ_df.loc[econ_df[column] == minimum,'Country'].to_list()[0]

# Access the country highest in a dimension
def highest_in(column):
    "Which country is maximum in a dimension"

    if column not in econ_df.columns:
        return 'NA'

    maximum = econ_df[column].max()

    print(maximum)

    return econ_df.loc[econ_df[column] == maximum,'Country'].to_list()[0]


class ActionColumnsList(Action):
#
    def name(self) -> Text:
        return "action_columns_list"
#
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        cols = econ_df.columns

        dispatcher.utter_message(text=f"The list of dimensions are: {cols}")
#
        return []

class ActionCountryList(Action):
#
    def name(self) -> Text:
        return "action_country_list"
#
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        country = econ_df.Country.unique()

        dispatcher.utter_message(text=f"There are {len(country)} countries. Showing first 10 for reference {country[:10]}")
#
        return []

class ActionDataAccess(Action):
#
    def name(self) -> Text:
        return "action_data_access"
#
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot('country') 
        column = tracker.get_slot('column')

        data = data_access(country, column)

        dispatcher.utter_message(text=f"The {column} of {country} is {data}")
#
        return []

class ActionLowest(Action):
#
    def name(self) -> Text:
        return "action_lowest"
#
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        column = tracker.get_slot('column')
        print(column)
        country = lowest_in(column)

        dispatcher.utter_message(text=f"The country with lowest {column} is {country}")
#
        return []

class ActionHighest(Action):
#
    def name(self) -> Text:
        return "action_highest"
#
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        column = tracker.get_slot('column')
        print(column)
        country = highest_in(column)

        dispatcher.utter_message(text=f"The country with highest {column} is {country}")
#
        return []

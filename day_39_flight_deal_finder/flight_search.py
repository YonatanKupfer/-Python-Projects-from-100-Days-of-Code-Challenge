import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "JJs2d8Mm_rF5fLO55BiylSJs40cA1ZAY"

class FlightSearch:

    def get_destination_code(self, cityName):
        parms = {"term": cityName, "location_type": "city"}
        headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            params=parms,
            headers=headers)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code


    def check_flights(self, origin_city_code, dest_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "USD"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=headers)
        print(response.json())
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            org_city=data["route"][0]["cityFrom"],
            org_airport=data["route"][0]["flyFrom"],
            dest_city=data["route"][0]["cityTo"],
            dest_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
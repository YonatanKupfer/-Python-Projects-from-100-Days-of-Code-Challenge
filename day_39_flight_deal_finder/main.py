from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORG_CITY_IATA = "TLV"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=6*30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORG_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_mail(body=f"Low price alert! only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                                            f" to {flight.destination_city}-{flight.destination_airport},"
                                            f" from {flight.out_date} to {flight.return_date}.")
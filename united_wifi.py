from pprint import pprint
from argparse import ArgumentParser
from requests import get
from scapy.sendrecv import sniff
from scapy.layers.dot11 import Dot11

# Settings
BASE_URL = "https://www.unitedwifi.com"
METRIC_DEFUALT = False
ON_PlANE = False


def parse_args():
    parser = ArgumentParser(
        prog="United_Wifi", description="Gives you all info from `United_Wi-Fi`")
    parser.add_argument("-m", "--metric", help="prints info in metric",
                        action="store_true")
    parser.add_argument("-j", "--json", help="prints raw json received",
                        action="store_true")
    return parser.parse_args()


def united_wifi(packet):
    if packet.haslayer(Dot11) and packet.type == 0 and packet.subtype == 8:
        try:
            ssid = packet.info.decode("utf-8")
            ON_PlANE = ON_PlANE and ssid == "United_Wi-Fi"
        except:
            pass


def get_info():
    try:
        response = get(BASE_URL + "/portal/r/getAllSessionData")
        return response.json()
    except ValueError as error:
        print(repr(error))
        exit(0)


def print_weather(day, metric=METRIC_DEFUALT):
    print("\n" + day.get("day").upper())
    print("Text: %s" % day.get("text"))
    if metric:
        print("Current Temperature: %sc" % day.get("currtempc"))
        print("High Temperature: %sc" % day.get("hightempc", 0))
        print("Low Temperature: %sc" % day.get("lowtempc"))
    else:
        print("Current Temperature: %sf" % day.get("currtempf"))
        print("High Temperature: %sf" % day.get("hightempf", 0))
        print("Low Temperature: %sf" % day.get("lowtempf"))


def print_info(info_dict, metric=METRIC_DEFUALT):
    print("GENERAL")
    print("Portal Initialized: %s" % info_dict.get("isPortalInitialized"))
    print("Flight Offers Internet Service: %s" %
          info_dict.get("flightOffersInternetService"))
    print("Internet Connection Available: %s" %
          info_dict.get("internetConnectionIsAvailable"))
    print("Subscription Available: %s" %
          info_dict.get("isSubscriptionAvailable"))
    print("Logged in: %s" % info_dict.get("IsLoggedIn"))

    if info_dict.get("IsLoggedIn") or info_dict.get("internet").get("accessType") != "NONE":
        print("\nINTERNET")
        print("Access Type: %s" % info_dict.get("internet").get("accessType"))
        print("Tier: %s" % info_dict.get("internet").get("tier"))
        print("Tier Description: %s" %
              info_dict.get("internet").get("tierDescription"))
        print("Fulfilment State: %s" %
              info_dict.get("internet").get("fulfilmentState"))
        print("Order State: %s" % info_dict.get("internet").get("orderState"))
        print("Time Remaining: %s" %
              info_dict.get("internet").get("timeRemaining"))

    print("\nFLIGHT INFO")

    print("Fake Flight: %s" % info_dict.get("flifo").get("isFake"))
    print("Flight Status: %s" % info_dict.get("flifo").get("flightStatus"))
    print("Flight Number: %s" % info_dict.get("flifo").get("flightNumber"))
    print("Flight GUID: %s" % info_dict.get("flifo").get("flightGuid"))
    print("Flight Map: %s" % BASE_URL +
          info_dict.get("flifo").get("flightMapPath").strip())
    print("Flight Duration: %s min" %
          info_dict.get("flifo").get("flightDurationMinutes"))
    print("Time Remaining To Destination: %s min" %
          info_dict.get("flifo").get("timeRemainingToDestination"))
    print("Origin Airport Code: %s" %
          info_dict.get("flifo").get("originAirportCode"))
    print("Origin City: %s" % info_dict.get("flifo").get("originCity"))
    print("Origin State: %s" % info_dict.get("flifo").get("originState"))
    print("Departure Gate: %s" % info_dict.get("flifo").get("departureGate"))
    print("Departure Terminal: %s" %
          info_dict.get("flifo").get("departureTerminal"))
    print("Departure Concourse: %s" %
          info_dict.get("flifo").get("departureConcourse"))
    print("Destination Airport Code: %s" %
          info_dict.get("flifo").get("destinationAirportCode"))
    print("Destination City: %s" %
          info_dict.get("flifo").get("destinationCity"))
    print("Destination State: %s" %
          info_dict.get("flifo").get("destinationState"))
    print("Arrival Gate: %s" % info_dict.get("flifo").get("arrivalGate"))
    print("Arrival Terminal: %s" %
          info_dict.get("flifo").get("arrivalTerminal"))
    print("Arrival Concourse: %s" %
          info_dict.get("flifo").get("arrivalConcourse"))
    print("Scheduled Departure Time in %s: %s" %
          (info_dict.get("flifo").get("originCity"), info_dict.get("flifo").get("scheduledDepartureTimeLocal")))
    print("Estimated Departure Time in %s: %s" %
          (info_dict.get("flifo").get("originCity"), info_dict.get("flifo").get("estimatedDepartureTimeLocal")))
    print("Actual Departure Time in %s: %s" %
          (info_dict.get("flifo").get("originCity"), info_dict.get("flifo").get("actualDepartureTimeLocal")))
    print("Scheduled Arrival Time in %s: %s" %
          (info_dict.get("flifo").get("destinationCity"), info_dict.get("flifo").get("scheduledArrivalTimeLocal")))
    print("Estimated Arrival Time in %s: %s" %
          (info_dict.get("flifo").get("destinationCity"), info_dict.get("flifo").get("estimatedArrivalTimeLocal")))
    print("Actual Arrival Time in %s: %s" %
          (info_dict.get("flifo").get("destinationCity"), info_dict.get("flifo").get("actualArrivalTimeLocal")))
    print("Wind Direction: %s kph" %
          info_dict.get("flifo").get("windDirection"))
    if metric:
        print("Air Speed: %s kph" % info_dict.get("flifo").get("airSpeedKPH"))
        print("Ground Speed: %s kph" %
              info_dict.get("flifo").get("groundSpeedKPH"))
        print("Air Temperature: %sc" %
              info_dict.get("flifo").get("airTemperatureC"))
        print("Altitude: %sft" % info_dict.get("flifo").get("altitudeMeters"))
    else:
        print("Air Speed: %s mph" % info_dict.get("flifo").get("airSpeedMPH"))
        print("Ground Speed: %s mph" %
              info_dict.get("flifo").get("groundSpeedMPH"))
        print("Air Temperature: %sf" %
              info_dict.get("flifo").get("airTemperatureF"))
        print("Altitude: %sm" % info_dict.get("flifo").get("altitudeFt"))

    print("\nPLANE INFO")
    print("Aircraft Model: %s" % info_dict.get("flifo").get("aircraftModel"))
    print("Nose Number: %s" % info_dict.get("flifo").get("noseNumber"))
    print("Equipment Code: %s" % info_dict.get("flifo").get("equipmentCode"))

    print("\nWEATHER")
    for key in info_dict.get("weather").keys():
        if key == "currently":
            print_weather(info_dict.get("weather").get(key))
        elif key == "forecast":
            for day in info_dict.get("weather").get(key):
                if day != "lastitem":
                    print_weather(day)


def print_json(info_dict):
    pprint(info_dict)


if __name__ == "__main__":
    args = parse_args()
    print("Checking wifi...")
    sniff(prn=united_wifi, store=False, timeout=3, monitor=True)
    if not ON_PlANE:
        print("You are not connected to `United_Wi-Fi`. Please connect and try again.")
        exit(1)
    info_dict = get_info()
    print_info(info_dict, metric=args.metric)
    if args.json:
        print_json(info_dict)

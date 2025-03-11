#!/usr/bin/python3
import json
import time


FILENAME = "/run/dump1090-fa/aircraft.json"


def aircraft_has_mlat(aircraft):
    mlat = aircraft.get("mlat")
    return mlat is not None and len(mlat) > 0


def test():
    with open(FILENAME) as f:
        dump1090 = json.load(f)
    aircrafts = dump1090['aircraft']
    mlat_count = 0
    for aircraft in aircrafts:
        if aircraft_has_mlat(aircraft):
            print(F"Found mlat for {aircraft}")
            mlat_count += 1
    print(f"{mlat_count} of {len(aircrafts)} aircraft have mlat")


def main():

    while True:
        test()
        time.sleep(1)


if __name__ == "__main__":
    main()

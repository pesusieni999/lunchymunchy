#!/usr/bin/env python3


import urllib.request
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser
from bs4 import BeautifulSoup


def get_lunch_menu():
    menu = get_data(
        "http://www.linkosuo.fi/kahvilat/ravintola-hertta/lounaslista-hertta.html"
    )
    if menu is not None:
        menu = parse_lunch_menu(menu)
    return menu


def parse_lunch_menu(data):
    """

    :param data:
    :return: Dict containing lunch data for week.

     Attempts to
    """
    if not isinstance(data, str):
        print("Error: Illegal parameter. Expected String.")
        return None

    soup = BeautifulSoup(data, "html.parser")
    div = soup.find(id="sivu_sisalto_sis")
    print(div)
    c = {}
    return c


def get_data(url):
    if not isinstance(url, str):
        print("Error: Illegal parameter. Expected String.")
        return None
    data = None
    try:
        lunch_data = urllib.request.urlopen(url)
        data = lunch_data.read().decode("utf8")
        lunch_data.close()
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    return data


def send_data(data):
    pass


def main():
    menu = get_lunch_menu()
    send_data(menu)
    # print("Lunch menu is:\n", menu)

if __name__ == "__main__":
    main()


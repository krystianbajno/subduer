#!/usr/bin/python

from bs4 import BeautifulSoup

with open("virustotalsubs.html", "r") as virus:
    minified = virus.read()
    minified = minified.replace("\n", "")
    minified = minified.replace("  ", "")

    soup = BeautifulSoup(minified)
    rows = soup.find_all("div", class_="tr")

    data = []

    for row in rows:
        to_add = []
        for td in row.find_all("div", class_="td", ):
            worth_rows = td.find_all(text=True)
            for worth_row in worth_rows:
                if not "?lit" in worth_row and not " " in worth_row and worth_row != "-":
                    to_add.append(worth_row)

        data.append(to_add)

    with open("subdomains_virustotal.csv", "w") as towrite:
        to_write = ""
        for row in data:
            for td in row:
                to_write += f"{td},"
            to_write += "\n"
        print(to_write)
        towrite.write(to_write)

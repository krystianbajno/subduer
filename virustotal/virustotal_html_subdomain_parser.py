from bs4 import BeautifulSoup

from mappers.data_mapper import map_data

def parse_html(html):
    minified = html.replace("\n", "").replace("  ", "")
    soup = BeautifulSoup(minified, features="html.parser")
    rows = soup.find_all("div", class_="tr")

    data = []

    for row in rows:
        entry = []
        for td in row.find_all("div", class_="td"):
            worth_rows = td.find_all(string=True)
            for worth_row in worth_rows:
                if not "?lit" in worth_row and not " " in worth_row and worth_row != "-":
                    entry.append(worth_row)
        data.append(entry)
        
    return map_data(data)
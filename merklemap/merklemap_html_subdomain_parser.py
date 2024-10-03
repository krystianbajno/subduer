from bs4 import BeautifulSoup

from mappers.data_mapper import map_data

def parse_html(htmls):
    ret_html = []
    for html in htmls: 
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', {'aria-label': 'Subdomain listing table with async pagination'})

        tbody = table.find('tbody')
        rows = tbody.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            row_data = [cell.get_text(strip=True) for cell in cells][1:]
            ret_html.append(row_data)
        
    return map_data(ret_html)
            
            
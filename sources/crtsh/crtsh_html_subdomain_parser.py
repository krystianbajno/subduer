from bs4 import BeautifulSoup
from mappers.data_mapper import map_data

def parse_html(html):
    ret_html = []
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find_all('table')[1]
    hrow = table.find("tr")
    rows = hrow.find_all('tr')[1:]

    for row in rows:
        cells = row.find_all('td')
        
        row_data = [cell.get_text(strip=True) for cell in cells]

        out_row = []
        out_row.append(row_data[1])
        out_row.append(row_data[2]) 
        out_row.append(row_data[3]) 
        
        domain_1_html = cells[4].decode_contents()
        domains_1 = [d.strip() for d in domain_1_html.split("<br/>")]
        
        for domain in domains_1:
            out_row.append(domain)

        domain_2_html = cells[5].decode_contents()
        domains_2 = [d.strip() for d in domain_2_html.split("<br/>")]
        
        for domain in domains_2:
            out_row.append(domain)

        ret_html.append(out_row)
            
    return map_data(ret_html)

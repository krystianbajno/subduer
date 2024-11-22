from io import BytesIO
import openpyxl

from mappers.data_mapper import map_data

def parse_xlsx(data):
    ret_data = []
    
    workbook = openpyxl.load_workbook(BytesIO(data))
    
    sheet = workbook["DNS Records"]
    
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = list(row)
        ret_data.append(row_data)
        
    return map_data(ret_data)
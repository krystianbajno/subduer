from dateutil import parser

def normalize_date(date_str):
    date_str = date_str.replace("/", "-")
    
    try:
        normalized_date = parser.parse(date_str, dayfirst=True)
        return normalized_date
    except Exception as e:
        print(f"Error parsing date: {date_str} - {e}")
        return None

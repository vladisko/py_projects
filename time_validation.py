from re import fullmatch

def time_validation(value:str) -> bool:
    if not fullmatch(r'\d{2}:\d{2}', value):
        return False
    hours, minutes = map(int, value.split(":"))
    return 24 > hours >= 0 and 60 > minutes >= 0

def time_interval_validation(start:str, end:str) -> bool:
    if not (time_validation(start) and time_validation(end)):
        return False
        
    start = start.split(":")
    start = {"hours": start[0],
             "minutes": start[1]
            }
    
    end = end.split(":")
    end = {"hours": end[0],
           "minutes": end[1]
          }
    
    if (start["hours"] == end["hours"]):
        return start["minutes"] < end["minutes"]
    else:
        return start["hours"] < end["hours"]
"""
Module for handling dates

Calculates datecode from str date or int date via: from_string, from_date_quarter

Calculates dates from datecode via: to_string, to_year_quarter

Grabs int year and quarter from str date: get_year_quarter_from_string
"""

def from_year_quarter(year: int, quarter: int) -> int:
    """
    Input year and quarter (in int)
    Get datecode
    """
    if year<0:
        raise Exception("Year must be non-negative.")
    if quarter<1 or quarter>4:
        raise Exception("Quarter must be between 1 and 4.")
    datecode = year*4+quarter
    return datecode

def to_string(datecode: int) -> str:
    """
    Input datecode (in int)
    Get string date ('XXXX-QX')
    """
    if datecode<1:
        raise Exception("Datecode must be non-negative and mustn't be 0")
    year = int((datecode-1)/4)
    quarter = (datecode-1)%4+1
    str_date = str(year) + '-Q' + str(quarter)
    return str_date

def to_year_quarter(datecode: int) -> (int, int):
    """
    Input datecode (in int)
    Get year and quarter
    """
    if datecode<1:
        raise Exception("Datecode must be non-negative and mustn't be 0")
    year = int((datecode-1)/4)
    quarter = (datecode-1)%4+1
    return year, quarter

def get_year_quarter_from_string(full_date: str) -> (int, int):
    """
    Input date (in str: 'XXXX-QX')
    Get year and quarter
    """
    year = int(full_date[0:-3])
    quarter = int(full_date[-1])
    return year, quarter

def from_string(full_date: str) -> int:
    """
    Input date (in str: 'XXXX-QX')
    Get datecode
    """
    year, quarter = get_year_quarter_from_string(full_date)
    if year<0:
        raise Exception("Year must be non-negative.")
    if quarter<1 or quarter>4:
        raise Exception("Quarter must be between 1 and 4.")
    datecode = year*4+quarter
    return datecode

def create_range(start:int, end: int) -> list[int]:
    """
    Input start and end datecode (in int)
    Get list of the range from start to end
    """
    range_of_datecodes = []
    for i in range(end-start):
        range_of_datecodes.append(start+i)
    range_of_datecodes.append(end)
    return range_of_datecodes

def value_selection(values, dates, date_selection):
    selected_values = []
    for date in dates:
        if date in date_selection:
            value = values[dates.index(date)]
        else:
            value = math.nan
        selected_values.append(value)
    return selected_values

def max_dates(date1, date2):
#find maximum(for start) out of 2 dates
    if date1 > date2:
        maximum_date = date1
    elif date1 == date2:
        maximum_date = date1
    else:
        maximum_date = date2
    return maximum_date

def min_dates(date1, date2):
#find minimum -''-
    if date1 < date2:
        minimum_date = date1
    elif date1 == date2:
        minimum_date = date1
    else:
        minimum_date = date2
    return minimum_date

def plus_with_datecodes(values1, datecodes1, values2, datecodes2):
    start1 = datecodes1[0]
    start2 = datecodes2[0]
    start = max_dates(start1, start2)
    end1 = datecodes1[-1]
    end2 = datecodes2[-1]
    end = min_dates(end1, end2)
    range = create_range(start, end)
    selected_values1 = value_selection(values1, datecodes1, range)
    selected_values2 = value_selection(values2, datecodes2, range)
    return [ i[0]+i[1] for i in zip(selected_values1, selected_values2) ]

class TimeSeries:
    def __init__(self, dates, values):
        self.dates = dates
        self.values = values

    def __add__(self, n):
        if isinstance(n, TimeSeries) == True:
            self.values = plus_with_datecodes(self.values, self.dates, n.values, n.dates)
        else:
            self.values = [ i+1 for i in self.values ]

    __radd__ = __add__

import datahandling as dh
import random
from datahandling import TimeSeries

def test_with_same_range():
    start_date = random.randint(1, 500)
    end_date = random.randint(501, 1000)
    range_of_dates = dh.create_range(start_date, end_date)


import datahandling as dh
import random
from datahandling import TimeSeries

def generate_with_same_range():
    start_date = random.randint(1, 500)
    end_date = random.randint(501, 1000)
    range_of_dates = dh.create_range(start_date, end_date)
    generate = lambda num, lower, upper: [random.randint(lower, upper) for i in range(num)]
    values1 = generate(len(range_of_dates), -1e6, 1e6)
    values2 = generate(len(range_of_dates), -1e6, 1e6)
    series1 = TimeSeries(range_of_dates, values1)
    series2 = TimeSeries(range_of_dates, values2)
    return series1, series2


#for tests in range(1000):
series1, series2 = generate_with_same_range()
pc_sum = dh.plus_with_datecodes(series1.values, series1.dates, series2.values, series2.dates)
manual_sum = [series1.values[i]+series2.values[i] for i in range(series1.dates)]
assert pc_sum == manual_sum


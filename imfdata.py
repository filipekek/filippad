import requests
import json
import random
import plotly.express as px
import datahandling as qdate
import math

x = requests.get("http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/Q.CZ.NGDP_R_SA_XDC")
z = x.json()["CompactData"]["DataSet"]["Series"]["Obs"]
values = []
dates = []

#with open("imfdata.json", "w+") as outfile:
#    outfile.write(x.text)

for i in z:
    values.append(float(i["@OBS_VALUE"]))
    dates.append(i["@TIME_PERIOD"])

value_length = len(values)

qoq = list()
yoy = list()
for i in range(value_length):
    qoq.append(float(100*(values[i]/values[i-1]-1)))
    yoy.append(float(100*(values[i]/values[i-4]-1)))
qoq[0] = None
yoy[0:4] = [None]*4

#px.line(x=dates, y=values, labels={'x': 'dates', 'y': 'obs values'}).show()
#px.line(x=dates, y=qoq, labels={'x': 'dates', 'y': 'qoq'}).show()
#px.line(x=dates, y=yoy, labels={'x': 'dates', 'y': 'yoy'}).show()

#=============================================================================================

nz_x = requests.get("http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/Q.NZ.NGDP_R_SA_XDC")
nz_z = nz_x.json()["CompactData"]["DataSet"]["Series"]["Obs"]
nz_values = []
nz_dates = []

#with open("imfdata.json", "w+") as outfile:
#    outfile.write(x.text)

for i in nz_z:
    nz_values.append(float(i["@OBS_VALUE"]))
    nz_dates.append(i["@TIME_PERIOD"])

nz_value_length = len(nz_values)

nz_qoq = list()
nz_yoy = list()
for i in range(nz_value_length):
    nz_qoq.append(float(100*(nz_values[i]/nz_values[i-1]-1)))
    nz_yoy.append(float(100*(nz_values[i]/nz_values[i-4]-1)))
nz_qoq[0] = None
nz_yoy[0:4] =    [None]*4

#==============================================================================================

def get_year_quarter(str_date):
    year_and_quarter = str_date.split("-")
    year = int(year_and_quarter[0])
    quarter = int(year_and_quarter[1].replace("Q",""))
    return year, quarter
#
#def calc_datecode(year, quarter):
##datecodes starting at year 0 quarter 1
#    if year<0:
#        raise Exception("Year must be non-negative.")
#    if quarter<1 or quarter>4:
#        raise Exception("Quarter must be between 1 and 4.")
#    datecode = year*4+quarter
#    return datecode
#
#def get_date_from_code(datecode):
#    if datecode<1:
#        raise Exception("Datecode must be non-negative and mustn't be 0")
#    year = int((datecode-1)/4)
#    quarter = (datecode-1)%4+1
#    return year, quarter
#
#def test_datecode():
#    for test in range(100):
#        year1 = random.randint(0, 3000)
#        quarter1 = random.randint(1,4)
#        datecode = calc_datecode(year1, quarter1)
#        year2, quarter2 = get_date_from_code(datecode)
#        print(year1, quarter1, year2, quarter2)
#        assert [year1, quarter1]==[year2, quarter2], 'Error in code'

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

def create_range_of_dates(start, end):
#create list of dates from start to end
    start_year, start_quarter = get_year_quarter(start)
    end_year, end_quarter = get_year_quarter(end)
    years = []

    def year_with_quarters(year):
        year = str(year)
        years = []
        for i in range(1, 5):
            years.append(year + '-Q' + str(i))
        return years

    years_between = list(range(start_year+1, end_year))

    for year in years_between:
        year_now = year_with_quarters(year)
        years = years + year_now

    def gen_all_years(years, start_year, start_quarter, end_year, end_quarter):
        all_years = []
        for i in range(1, 5):
            if i>=start_quarter:
                all_years.append(str(start_year) + '-Q' + str(i))
        all_years = all_years + years
        for i in range(1, 5):
            if i<=end_quarter:
                all_years.append(str(end_year) + '-Q' + str(i))
        return all_years
    range_of_years = gen_all_years(years, start_year, start_quarter, end_year, end_quarter)
    return range_of_years

#def plus(values1, dates1, values2, dates2, all_dates):
#    start1 = dates1[0]
#    start2 = dates2[0]
#    start = max_dates(start1, start2)
#    end1 = dates1[-1]
#    end2 = dates2[-1]
#    end = min_dates(end1, end2)
#    range = create_range(start, end, all_dates)
#    selected_values1 = value_selection(values1, dates1, range)
#    selected_values2 = value_selection(values2, dates2, range)
#    return  [ i[0]+i[1] for i in zip(selected_values1,selected_values2) ], range

def plus_with_datecodes(values1, dates1, values2, dates2):
    datecodes1 = []
    datecodes2 = []
    [ datecodes1.append(qdate.from_string(i)) for i in dates1 ]
    [ datecodes2.append(qdate.from_string(i)) for i in dates2 ]
    start1 = datecodes1[0]
    start2 = datecodes2[0]
    start = max_dates(start1, start2)
    end1 = datecodes1[-1]
    end2 = datecodes2[-1]
    end = min_dates(end1, end2)
    range = qdate.create_range(start, end)
    selected_values1 = value_selection(values1, datecodes1, range)
    selected_values2 = value_selection(values2, datecodes2, range)
    return [ i[0]+i[1] for i in zip(selected_values1, selected_values2) ], range

def test_plus():
    dates1 = ['2015-Q1', '2015-Q2', '2015-Q3', '2015-Q4', '2016-Q1']
    dates2 = dates1
    values1 = [1, 2, 3, 4, 5]
    values2 = values1
    summed_up = plus_with_datecodes(values1, dates1, values2, dates2)
    return summed_up, values2

#nz_vector_values = [None]*len(all_dates)
#cz_vector_values = [None]*len(all_dates)
#for dtv in all_dates:
#    if dtv not in dates:
#        continue
#    cz_vector_values[all_dates.index(dtv)] = qoq[dates.index(dtv)]
#for dtv in all_dates:
#    if dtv not in nz_dates:
#        continue
#    nz_vector_values[all_dates.index(dtv)] = nz_qoq[nz_dates.index(dtv)]
#px.line(x=all_dates, y=[nz_vector_values, cz_vector_values], labels={'x': 'dates', 'y': 'obs values'}).show()
#px.line(x=dates, y=qoq, labels={'x': 'dates', 'y': 'qoq'}).show()
#px.line(x=dates, y=yoy, labels={'x': 'dates', 'y': 'yoy'}).show()

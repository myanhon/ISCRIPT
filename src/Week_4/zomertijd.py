import datetime
# Mike Yan
# s1098641

from datetime import date, timedelta

def klok(datum):
    dag = datetime.datetime.strptime(datum, '%d/%m/%Y')
    dag = datetime.datetime.date(dag)
    jaar = dag.year

    if dag == zomerTijd(jaar):
        return "omschakeling van wintertijd naar zomertijd"
    if dag == winterTijd(jaar):
        return "omschakeling van zomertijd naar wintertijd"

    if( (dag < winterTijd(jaar)) and (dag > zomerTijd(jaar))):
        return "zomertijd"
    else:
        return "wintertijd"


def checkZondag(date):
    while date.weekday() != 6:
        date = date - timedelta(1)
    return date

def zomerTijd(year):
 return checkZondag(datetime.date(year, 3, 31))

def winterTijd(year):
 return  checkZondag(datetime.date(year, 10, 31))

print(zomerTijd(1000))
print(zomerTijd(2013))
print(zomerTijd(2014))
print(zomerTijd(2015))

print(winterTijd(2013))
print(winterTijd(2014))
print(winterTijd(2015))


print(klok('27/06/2015'))
print(klok('27/11/2013'))
print(klok('31/03/2013'))
print(klok('27/10/2013'))
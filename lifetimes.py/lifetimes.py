#!/usr/bin/python
# coding: utf-8

"""
    lifetimes.py 1.0 - Compares the time, you've lived up to now,
                       to the lifetimes of selected famous persons.

    Copyright (C) 2021 hlubenow

    This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import datetime
import sys

CELEBRITY_GRAVEYARD = (("Douglas Adams", "11.03.1952", "11.05.2001"),
                       ("Ludwig van Beethoven", "17.12.1770", "26.03.1827"),
                       ("David Bowie", "08.01.1947", "10.01.2016"),
                       ("Lewis Collins", "27.05.1946", "27.11.2013"),
                       ("Falco", "19.02.1957", "06.02.1998"),
                       ("Marie Fredriksson", "30.05.1958", "09.12.2019"),
                       ("Edvard Grieg", "15.06.1843", "04.09.1907"),
                       ("George Harrison", "25.02.1943", "29.11.2001"),
                       ("Gordon Jackson", "19.12.1923", "15.01.1990"),
                       ("Michael Jackson", "29.08.1958", "25.06.2009"),
                       ("Steve Jobs", "24.02.1955", "05.10.2011"),
                       ("Franz Kafka", "03.07.1883", "03.06.1924"),
                       ("Klaus Kinski", "18.10.1926", "23.11.1991"),
                       ("Bruce Lee", "27.11.1940", "20.07.1973"),
                       ("John Lennon", "09.10.1940", "08.12.1980"),
                       ("Steve McQueen", "24.03.1930", "07.11.1980"),
                       ("Freddie Mercury", "05.09.1946", "24.11.1991"),
                       ("George Michael", "25.06.1963", "25.12.2016"),
                       ("Jay Miner", "31.05.1932", "20.06.1994"),
                       ("Marilyn Monroe", "01.06.1926", "05.08.1962"),
                       ("Wolfgang Amadeus Mozart", "27.01.1756", "05.12.1791"),
                       ("Luke Perry", "11.10.1966", "04.03.2019"),
                       ("Elvis Presley", "08.01.1935", "16.08.1977"),
                       ("Prince", "07.06.1958", "21.04.2016"),
                       ("Friedrich Schiller", "10.11.1759", "09.05.1805"),
                       ("Romy Schneider", "23.09.1938", "29.05.1982"),
                       ("Lino Ventura", "14.07.1919", "22.10.1987"))

def checkDate(d):
    e = False
    if len(d) != 10:
        dateError("Wrong date format.", 2)
    for i in (0, 1, 3, 4, 6, 7, 8, 9):
        if not d[i].isdigit():
            dateError("Wrong number format.", 3)
    for i in (2, 5):
        if d[i] != ".":
            dateError("Point not at right place.", 4)

def dateError(m, nr):
     print
     print "Error: " + m
     print
     sys.exit(nr)

def getTimeStr(days):
    years = days // 365
    restdays = days % 365
    timestr = ""
    if years > 0:
        timestr += str(years) + " year"
    if years > 1:
        timestr += "s"
    if years > 0:
        timestr += " and "
    if restdays > 0:
        timestr += str(restdays) + " day"
    if restdays > 1:
        timestr += "s"
    if years >= 1:
        timestr +=  " (" + str(days) + " days)"
    return timestr

class Person:

    def __init__(self, name, birthstr, laststr):
        self.name     = name
        self.birthstr = birthstr
        self.laststr  = laststr
        if self.laststr == "":
            self.setLastStrAsTodayStr()
        self.days = self.getDays()
        self.timestr = getTimeStr(self.days)

    def getDays(self):
        diff = self.strToDateObj(self.laststr) - self.strToDateObj(self.birthstr)
        return diff.days

    def strToDateObj(sefl, a):
        b = a.split(".")
        return datetime.date(int(b[2]), int(b[1]), int(b[0]))

    def setLastStrAsTodayStr(self):
        today = datetime.date.today()
        today = today.timetuple()
        self.laststr = str(today[2]) + "."
        if today[1] < 10:
            self.laststr += "0"
        self.laststr += str(today[1]) + "." + str(today[0])


# Main:

if len(sys.argv) < 2:
    print
    print "Usage: lifetimes.py [DD.MM.YYYY] - (Where the date is your birthday.)"
    print
    sys.exit(1)

userbirthday = sys.argv[1]
checkDate(userbirthday)

user = Person("User", userbirthday, "")

deceasedpersons = []
for i in CELEBRITY_GRAVEYARD:
    deceasedpersons.append(Person(i[0], i[1], i[2]))

# Sort by lifetime (days lived):
deceasedpersons.sort(key = lambda a : a.days, reverse = False)

print
print "You have lived " + user.timestr + " yet."
print

firstmore = False

for i in deceasedpersons:
    sum_ = i.days - user.days
    if sum_ < 0:
        sum_ *= -1
        print i.name + " lived " + i.timestr + "."
        print "You already survived " + i.name + " by " + getTimeStr(sum_) + "."
    else:
        if firstmore == False:
            print "----------------------"
            print
            firstmore = True
        print i.name + " lived " + i.timestr + "."
        print i.name + " lived " + getTimeStr(sum_) + " more than you have lived up to now."
    print

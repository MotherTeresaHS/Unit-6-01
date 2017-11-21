# Created by: Mr. Coxall
# Created on: Nov 2017
# Created for: ICS3U
# This program is an example of enumerated types

from enum import Enum

# an enumerated type of planets
Planets = Enum('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')

print(len(Planets))
print(Planets.Earth.index)
print(Planets[3])
print(Planets.Earth)

print('Earth' in Planets)
planet_selected = 'Pluto'
if planet_selected in Planets:
    print(planet_selected + ' is a valid planet')
else:
    print('That is not a planet')

planet_selected = int(input('Enter the planet # you would like to visit: '))
print(Planets[planet_selected])

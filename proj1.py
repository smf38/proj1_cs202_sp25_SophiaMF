#complete your tasks in this file

import sys
import unittest
import math
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**6)

#Task 1
@dataclass(frozen=True)
class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass(frozen=True)
class Region:
    rect: GlobeRect
    name: str
    terrain: str # ocean|mountains|forest|other

@dataclass(frozen=True)
class RegionCondition:
    region: Region
    year: int
    pop: int
    ghg_rate: float

#Task 2

region_conditions = [RegionCondition(
                        Region(
                            GlobeRect(
                                37.43, 37.70, 126.77, 127.18
                            ), 'Seoul', 'other'
                        ), 2025, 9600000, 2537300000),
                     RegionCondition(
                         Region(
                             GlobeRect(
                                 24.55, 25.5, 54.75, 55.65
                             ), 'Dubai', 'other'
                         ), 2025, 4000000, 200000000
                     ),
                    RegionCondition(
                        Region(
                            GlobeRect(
                                24, 26, -92, -88)
                            , 'Gulf of Mexico', 'ocean'),
                        2025, 0, 0),
                    RegionCondition(
                        Region(
                            GlobeRect(
                                35.15, 35.45, -120.80, -120.4)
                            , 'SLO', 'forest'),
                        2025, 130000, 1200000)
]

#Task 3

#subtask 3.1

#Return the greenhouse gas emissions per person for the given region condition.
def emissions_per_capita(rc: RegionCondition)->float:
    if rc.pop == 0 or rc.pop < 0.0:
        return 0.0
    return rc.ghg_rate / rc.pop

#subtask 3.2

#Return the surface area in square kilometers of the given geographic rectangle.
def area(gr: GlobeRect)->float:
    lo_lat_rad = math.radians(gr.lo_lat)
    hi_lat_rad = math.radians(gr.hi_lat)
    west_long_rad = math.radians(gr.west_long)
    east_long_rad = math.radians(gr.east_long)
    return (6378.1 ** 2) * abs(east_long_rad - west_long_rad) * abs(math.sin(hi_lat_rad) - math.sin(lo_lat_rad))

#subtask 3.3

#Return the greenhouse gas emissions per square kilometer for the given region condition.
def emissions_per_square_km(rc: RegionCondition)->float:
    return rc.ghg_rate / area(rc.region.rect)

#subtask 3.4

#Return the name of the region with the highest population density from the list.
def densest(rc_list: list[RegionCondition])->str:
    def calculate_density(rc_list: list[RegionCondition]) -> RegionCondition:
        if len(rc_list) == 1:
            return rc_list[0]
        first: RegionCondition = rc_list[0]
        rest: RegionCondition = calculate_density(rc_list[1:])
        if first.pop/area(first.region.rect) > rest.pop/area(rest.region.rect):
            return first
        else:
            return rest
    return calculate_density(rc_list).region.name

#Task 4

#Return a new RegionCondition projected forward by the given number of years,
#updating population and emissions based on terrain growth rates.
def project_condition(rc: RegionCondition, years: int)->RegionCondition:
    # Return the annual population growth rate associated with the given terrain type.
    def get_growth_rate(terrain: str) -> float:
        if terrain == "ocean":
            return 0.0001
        elif terrain == "mountains":
            return 0.0005
        elif terrain == "forest":
            return -0.00001
        return 0.0003

    #Return the population after applying compound growth for the given number of years.
    def grow_population(pop: int, pop_rate: float, years: int) -> float:
        if years == 0:
            return pop
        else:
            return grow_population(pop * (1 + pop_rate), pop_rate, years - 1)

    rate: float = get_growth_rate(rc.region.terrain)
    new_pop_float = grow_population(rc.pop, rate, years)
    new_population = int(new_pop_float)

    if rc.pop == 0:
        new_ghg: float = 0.0
    else:
        new_ghg: float = rc.ghg_rate * (new_pop_float / rc.pop)

    return RegionCondition(rc.region, rc.year + years,
                           int(new_population), new_ghg)


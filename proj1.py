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
def emissions_per_capita(rc):
    if rc.pop == 0 or rc.pop < 0.0:
        return 0.0
    return rc.ghg_rate / rc.pop

#subtask 3.2
def area(gr):
    return (6378.1**2) * (abs(gr.east_long - gr.west_long)) * (abs(math.sin(gr.hi_lat) - math.sin(gr.lo_lat)))

#subtask 3.3
def emissions_per_square_km(rc):
    return rc.ghg_rate / area(rc.region.rect)

#subtask 3.4
def densest(rc_list):
    def calculate_density(rc_list):
        if len(rc_list) == 1:
            return rc_list[0]
        first = rc_list[0]
        rest = calculate_density(rc_list[1:])
        if first.pop/area(first.region.rect) > rest.pop/area(rest.region.rect):
            return first
        else:
            return rest
    return calculate_density(rc_list).region.name


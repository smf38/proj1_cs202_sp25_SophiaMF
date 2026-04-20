#complete your tasks in this file
#I was here

#Task 1
from dataclasses import dataclass
@dataclass
class GlobeRect(frozen=True):
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass
class Region(frozen=True):
    rect: GlobeRect
    name: str
    terrain: str # ocean|mountains|forest|other

@dataclass
class RegionCondition(frozen=True):
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

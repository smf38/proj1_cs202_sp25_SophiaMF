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


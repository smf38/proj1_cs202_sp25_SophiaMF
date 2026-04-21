#proj1.py should contain your data class and function definitions
#these do not contribute positively to your grade.
#but your grade will be lowered if they are missing
from proj1 import *
import unittest
class TestRegionFunctions(unittest.TestCase):

    #normal
    def test_emissions_per_capita_one(self):
        rc = region_conditions[0]   #Seoul
        expected = 2537300000 / 9600000
        self.assertAlmostEqual(emissions_per_capita(rc), expected)

    #edge
    def test_emissions_per_capita_two(self):
        rc = region_conditions[2]   #Gulf of Mexico
        self.assertEqual(emissions_per_capita(rc), 0.0)

    #normal again
    def test_emissions_per_capita_three(self):
        rc = region_conditions[3]   #SLO
        expected = 1200000 / 130000
        self.assertAlmostEqual(emissions_per_capita(rc), expected)

    #normal
    def test_area_one(self):
        gr = region_conditions[0].region.rect
        self.assertGreater(area(gr), 0)

    #normal
    def test_area_two(self):
        gr = region_conditions[1].region.rect
        self.assertGreater(area(gr), 0)

    #edge make sure small is less than large
    def test_area_three(self):
        slo_rect = region_conditions[3].region.rect
        gulf_rect = region_conditions[2].region.rect
        self.assertLess(area(slo_rect), area(gulf_rect))

    #normal
    def test_emissions_per_square_km_one(self):
        rc = region_conditions[0]   #Seoul
        expected = rc.ghg_rate / area(rc.region.rect)
        self.assertAlmostEqual(emissions_per_square_km(rc), expected)

    #edge
    def test_emissions_per_square_km_two(self):
        rc = region_conditions[2]   #Gulf of Mexico
        expected = 0.0
        self.assertAlmostEqual(emissions_per_square_km(rc), expected)

    #normal
    def test_emissions_per_square_km_three(self):
        rc = region_conditions[3]   #SLO
        expected = rc.ghg_rate / area(rc.region.rect)
        self.assertAlmostEqual(emissions_per_square_km(rc), expected)

    #normal
    def test_densest_one(self):
        self.assertEqual(densest(region_conditions), "Seoul")

    #edge one item list
    def test_densest_two(self):
        self.assertEqual(densest([region_conditions[1]]), "Dubai")

#Part 4
    #normal
    def test_projection_seoul(self):
        rc = region_conditions[0]
        result = project_condition(rc, 2)
        rate = 0.0003
        new_pop = rc.pop
        for i in range(2):
            new_pop = new_pop * (1 + rate)
        expected_ghg = rc.ghg_rate * (new_pop / rc.pop)
        expected_pop = int(new_pop)
        self.assertEqual(result.region, rc.region)
        self.assertEqual(result.year, rc.year + 2)
        self.assertEqual(result.pop, expected_pop)
        self.assertAlmostEqual(result.ghg_rate, expected_ghg)


if __name__ == '__main__':
    unittest.main()

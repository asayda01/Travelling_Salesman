import pytest
import math
from cities import *

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    x2_x1 = (road_map1[0][2]-road_map1[1][2])**2
    y2_y1 = (road_map1[0][3]-road_map1[1][3])**2
    total_distance1= pytest.approx(math.sqrt(x2_x1+y2_y1),0.01)
    x4_x3 = (road_map1[2][2] - road_map1[1][2]) ** 2
    y4_y3 = (road_map1[2][3] - road_map1[1][3]) ** 2
    total_distance6 = pytest.approx(math.sqrt(x4_x3 + y4_y3), 0.01)
    assert (total_distance1 == 9.39) and (total_distance6 == 18.50)

def test_swap_cities():
    road_map2 = [("Kentucky", "Frankfort", 44.95 ,-93.094 ),\
                ("Delaware", "Dover", 38.197274, -84.86311),\
                ("Minnesota", "Saint Paul",39.161921 , -75.526755)]
    x2_x1 = (road_map2[0][2] - road_map2[1][2]) ** 2
    y2_y1 = (road_map2[0][3] - road_map2[1][3]) ** 2
    total_distance2 = pytest.approx(math.sqrt(x2_x1 + y2_y1), 0.01)

    x4_x3 = (road_map2[2][2] - road_map2[1][2]) ** 2
    y4_y3 = (road_map2[2][3] - road_map2[1][3]) ** 2
    total_distance3 = pytest.approx(math.sqrt(x4_x3 + y4_y3), 0.01)
    assert (total_distance2 == 10.65) and (total_distance3 == 9.39)

def test_shift_cities():
    road_map3 = [("Minnesota", "Saint Paul", 38.197274, -84.86311), \
                 ("Kentucky", "Frankfort", 39.161921, -75.526755), \
                 ("Delaware", "Dover", 44.95, -93.094)]
    x2_x1 = (road_map3[2][2] - road_map3[1][2]) ** 2
    y2_y1 = (road_map3[2][3] - road_map3[1][3]) ** 2
    total_distance4 = pytest.approx(math.sqrt(x2_x1 + y2_y1), 0.01)
    x4_x3 = (road_map3[0][2] - road_map3[1][2]) ** 2
    y4_y3 = (road_map3[0][3] - road_map3[1][3]) ** 2
    total_distance5 = pytest.approx(math.sqrt(x4_x3 + y4_y3), 0.01)

    assert (total_distance4 == 18.50)  and (total_distance5 == 9.39)

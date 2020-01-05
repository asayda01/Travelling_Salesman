import pytest
import math
from cities import *

def test_compute_total_distance():

    #test - 1

    road_map1 = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'),
                 ('Delaware', 'Dover', '39.161921', '-75.526755')]

    assert isinstance(compute_total_distance(road_map1), float)

    #test - 2

    total_dist2 = 0.0
    for i in range(0, len(road_map1)):
        city_x1 = float(road_map1[i][2])
        city_y1 = float(road_map1[i][3])
        city_x2 = float(road_map1[(i + 1) % len(road_map1)][2])
        city_y2 = float(road_map1[(i + 1) % len(road_map1)][3])
        total_dist2 += sqrt(((city_x2 - city_x1) ** 2) + ((city_y2 - city_y1) ** 2))

    assert (total_dist2 == compute_total_distance(road_map1))

    #test - 3

    road_map3 = [['Florida', 'Tallahassee', '30.4518', '-84.27277'],
                 ['Georgia', 'Atlanta', '33.76', '-84.39'],
                 ['Hawaii', 'Honolulu', '21.30895', '-157.826182'],
                 ['Idaho', 'Boise', '43.613739', '-116.237651'],
                 ['Illinois', 'Springfield', '39.78325', '-89.650373'],
                 ['Indiana', 'Indianapolis', '39.790942', '-86.147685'],
                 ['Iowa', 'Des Moines', '41.590939', '-93.620866'],
                 ['Kansas', 'Topeka', '39.04', '-95.69'],
                 ['Kentucky', 'Frankfort', '38.197274', '-84.86311'],
                 ['Louisiana', 'Baton Rouge', '30.45809', '-91.140229'],
                 ['Maine', 'Augusta', '44.323535', '-69.765261'],
                 ['Maryland', 'Annapolis', '38.972945', '-76.501157'],
                 ['Massachusetts', 'Boston', '42.2352', '-71.0275']]

    total_dist3 = 0.0
    for i in range(0, len(road_map3)):
        city_x1 = float(road_map3[i][2])
        city_y1 = float(road_map3[i][3])
        city_x2 = float(road_map3[(i + 1) % len(road_map3)][2])
        city_y2 = float(road_map3[(i + 1) % len(road_map3)][3])
        total_dist3 += sqrt(((city_x2 - city_x1) ** 2) + ((city_y2 - city_y1) ** 2))

    assert (total_dist3 == compute_total_distance(road_map3))

    #test - 4

    road_map4 = [['Montana', 'Helana', '46.595805', '-112.027031'],
                 ['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                 ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                 ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                 ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                 ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                 ['New York', 'Albany', '42.659829', '-73.781339'],
                 ['North Carolina', 'Raleigh', '35.771', '-78.638'],
                 ['North Dakota', 'Bismarck', '48.813343', '-100.779004'],
                 ['Ohio', 'Columbus', '39.962245', '-83.000647'],
                 ['Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'],
                 ['Oregon', 'Salem', '44.931109', '-123.029159'],
                 ['Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'],
                 ['Rhode Island', 'Providence', '41.82355', '-71.422132'],
                 ['South Carolina', 'Columbia', '34', '-81.035'],
                 ['South Dakota', 'Pierre', '44.367966', '-100.336378'],
                 ['Tennessee', 'Nashville', '36.165', '-86.784'],
                 ['Texas', 'Austin', '30.266667', '-97.75'],
                 ['Utah', 'Salt Lake City', '40.7547', '-111.892622'],
                 ['Vermont', 'Montpelier', '44.26639', '-72.57194'],
                 ['Virginia', 'Richmond', '37.54', '-77.46']]

    total_dist4 = 0.0
    for i in range(0, len(road_map4)):
        city_x1 = float(road_map4[i][2])
        city_y1 = float(road_map4[i][3])
        city_x2 = float(road_map4[(i + 1) % len(road_map4)][2])
        city_y2 = float(road_map4[(i + 1) % len(road_map4)][3])
        total_dist4 += sqrt(((city_x2 - city_x1) ** 2) + ((city_y2 - city_y1) ** 2))

    assert (total_dist4 == compute_total_distance(road_map4))


    # test - 5

    road_map5 = [['Alabama', 'Montgomery', '32.361538', '-86.279118'],
                 ['Alaska', 'Juneau', '58.301935', '-134.41974'],
                 ['Arizona', 'Phoenix', '33.448457', '-112.073844'],
                 ['Arkansas', 'Little Rock', '34.736009', '-92.331122'],
                 ['California', 'Sacramento', '38.555605', '-121.468926'],
                 ['Colorado', 'Denver', '39.7391667', '-104.984167'],
                 ['Connecticut', 'Hartford', '41.767', '-72.677'],
                 ['Delaware', 'Dover', '39.161921', '-75.526755'],
                 ['Florida', 'Tallahassee', '30.4518', '-84.27277'],
                 ['Georgia', 'Atlanta', '33.76', '-84.39'],
                 ['Hawaii', 'Honolulu', '21.30895', '-157.826182'],
                 ['Idaho', 'Boise', '43.613739', '-116.237651'],
                 ['Illinois', 'Springfield', '39.78325', '-89.650373'],
                 ['Indiana', 'Indianapolis', '39.790942', '-86.147685'],
                 ['Iowa', 'Des Moines', '41.590939', '-93.620866'],
                 ['Kansas', 'Topeka', '39.04', '-95.69'],
                 ['Kentucky', 'Frankfort', '38.197274', '-84.86311'],
                 ['Louisiana', 'Baton Rouge', '30.45809', '-91.140229'],
                 ['Maine', 'Augusta', '44.323535', '-69.765261'],
                 ['Maryland', 'Annapolis', '38.972945', '-76.501157'],
                 ['Massachusetts', 'Boston', '42.2352', '-71.0275'],
                 ['Michigan', 'Lansing', '42.7335', '-84.5467'],
                 ['Minnesota', 'Saint Paul', '44.95', '-93.094'],
                 ['Mississippi', 'Jackson', '32.32', '-90.207'],
                 ['Missouri', 'Jefferson City', '38.572954', '-92.189283'],
                 ['Montana', 'Helana', '46.595805', '-112.027031'],
                 ['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                 ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                 ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                 ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                 ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                 ['New York', 'Albany', '42.659829', '-73.781339'],
                 ['North Carolina', 'Raleigh', '35.771', '-78.638'],
                 ['North Dakota', 'Bismarck', '48.813343', '-100.779004'],
                 ['Ohio', 'Columbus', '39.962245', '-83.000647'],
                 ['Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'],
                 ['Oregon', 'Salem', '44.931109', '-123.029159'],
                 ['Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'],
                 ['Rhode Island', 'Providence', '41.82355', '-71.422132'],
                 ['South Carolina', 'Columbia', '34', '-81.035'],
                 ['South Dakota', 'Pierre', '44.367966', '-100.336378'],
                 ['Tennessee', 'Nashville', '36.165', '-86.784'],
                 ['Texas', 'Austin', '30.266667', '-97.75'],
                 ['Utah', 'Salt Lake City', '40.7547', '-111.892622'],
                 ['Vermont', 'Montpelier', '44.26639', '-72.57194'],
                 ['Virginia', 'Richmond', '37.54', '-77.46'],
                 ['Washington', 'Olympia', '47.042418', '-122.893077'],
                 ['West Virginia', 'Charleston', '38.349497', '-81.633294'],
                 ['Wisconsin', 'Madison', '43.074722', '-89.384444'],
                 ['Wyoming', 'Cheyenne', '41.145548', '-104.802042']]

    total_dist5 = 0.0
    for i in range(0, len(road_map5)):
        city_x1 = float(road_map5[i][2])
        city_y1 = float(road_map5[i][3])
        city_x2 = float(road_map5[(i + 1) % len(road_map5)][2])
        city_y2 = float(road_map5[(i + 1) % len(road_map5)][3])
        total_dist5 += sqrt(((city_x2 - city_x1) ** 2) + ((city_y2 - city_y1) ** 2))

    assert (total_dist5 == compute_total_distance(road_map5))


def test_swap_cities():

    # test - 1

    road_map_swap_1 = [['California', 'Sacramento', '38.555605', '-121.468926'],
                 ['Colorado', 'Denver', '39.7391667', '-104.984167'],
                 ['Connecticut', 'Hartford', '41.767', '-72.677']]

    assert (swap_cities(road_map_swap_1, 1, 2)) == ([['California', 'Sacramento', '38.555605', '-121.468926'],
                                            ['Connecticut', 'Hartford', '41.767', '-72.677'],
                                            ['Colorado', 'Denver', '39.7391667', '-104.984167']],compute_total_distance(road_map_swap_1))

    # test - 2

    road_map_swap_2 = [['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                       ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                       ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                       ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                       ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                       ['New York', 'Albany', '42.659829', '-73.781339'],
                       ['North Carolina', 'Raleigh', '35.771', '-78.638']]

    assert (swap_cities(road_map_swap_2, 3, 5)) == ([['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                                                     ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                                                     ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                                                     ['New York', 'Albany', '42.659829', '-73.781339'],
                                                     ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                                                     ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                                                     ['North Carolina', 'Raleigh', '35.771', '-78.638']],162.921023302501)




    # test - 3

    road_map_swap_3 = [['Florida', 'Tallahassee', '30.4518', '-84.27277'],
                 ['Georgia', 'Atlanta', '33.76', '-84.39'],
                 ['Hawaii', 'Honolulu', '21.30895', '-157.826182'],
                 ['Idaho', 'Boise', '43.613739', '-116.237651'],
                 ['Illinois', 'Springfield', '39.78325', '-89.650373'],
                 ['Indiana', 'Indianapolis', '39.790942', '-86.147685'],
                 ['Iowa', 'Des Moines', '41.590939', '-93.620866'],
                 ['Kansas', 'Topeka', '39.04', '-95.69'],
                 ['Kentucky', 'Frankfort', '38.197274', '-84.86311'],
                 ['Louisiana', 'Baton Rouge', '30.45809', '-91.140229'],
                 ['Maine', 'Augusta', '44.323535', '-69.765261'],
                 ['Maryland', 'Annapolis', '38.972945', '-76.501157'],
                 ['Massachusetts', 'Boston', '42.2352', '-71.0275']]

    assert (swap_cities(road_map_swap_3, 10,4 )) ==([['Florida', 'Tallahassee', '30.4518', '-84.27277'],
                 ['Georgia', 'Atlanta', '33.76', '-84.39'],
                 ['Hawaii', 'Honolulu', '21.30895', '-157.826182'],
                 ['Idaho', 'Boise', '43.613739', '-116.237651'],
                                                     ['Maine', 'Augusta', '44.323535', '-69.765261'],
                 ['Indiana', 'Indianapolis', '39.790942', '-86.147685'],
                 ['Iowa', 'Des Moines', '41.590939', '-93.620866'],
                 ['Kansas', 'Topeka', '39.04', '-95.69'],
                 ['Kentucky', 'Frankfort', '38.197274', '-84.86311'],
                 ['Louisiana', 'Baton Rouge', '30.45809', '-91.140229'],
                                                     ['Illinois', 'Springfield', '39.78325', '-89.650373'],
                 ['Maryland', 'Annapolis', '38.972945', '-76.501157'],
                 ['Massachusetts', 'Boston', '42.2352', '-71.0275']],266.9761645698053)


    # test - 4

    road_map_swap_4 = [['Montana', 'Helana', '46.595805', '-112.027031'],
                 ['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                 ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                 ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                 ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                 ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                 ['New York', 'Albany', '42.659829', '-73.781339'],
                 ['North Carolina', 'Raleigh', '35.771', '-78.638'],
                 ['North Dakota', 'Bismarck', '48.813343', '-100.779004'],
                 ['Ohio', 'Columbus', '39.962245', '-83.000647'],
                 ['Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'],
                 ['Oregon', 'Salem', '44.931109', '-123.029159'],
                 ['Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'],
                 ['Rhode Island', 'Providence', '41.82355', '-71.422132'],
                 ['South Carolina', 'Columbia', '34', '-81.035'],
                 ['South Dakota', 'Pierre', '44.367966', '-100.336378'],
                 ['Tennessee', 'Nashville', '36.165', '-86.784'],
                 ['Texas', 'Austin', '30.266667', '-97.75'],
                 ['Utah', 'Salt Lake City', '40.7547', '-111.892622'],
                 ['Vermont', 'Montpelier', '44.26639', '-72.57194'],
                 ['Virginia', 'Richmond', '37.54', '-77.46']]
    assert (swap_cities(road_map_swap_4, 1, 19)) == ([['Montana', 'Helana', '46.595805', '-112.027031'],
                                                      ['Vermont', 'Montpelier', '44.26639', '-72.57194'],
                 ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                 ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                 ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                 ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                 ['New York', 'Albany', '42.659829', '-73.781339'],
                 ['North Carolina', 'Raleigh', '35.771', '-78.638'],
                 ['North Dakota', 'Bismarck', '48.813343', '-100.779004'],
                 ['Ohio', 'Columbus', '39.962245', '-83.000647'],
                 ['Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'],
                 ['Oregon', 'Salem', '44.931109', '-123.029159'],
                 ['Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'],
                 ['Rhode Island', 'Providence', '41.82355', '-71.422132'],
                 ['South Carolina', 'Columbia', '34', '-81.035'],
                 ['South Dakota', 'Pierre', '44.367966', '-100.336378'],
                 ['Tennessee', 'Nashville', '36.165', '-86.784'],
                 ['Texas', 'Austin', '30.266667', '-97.75'],
                 ['Utah', 'Salt Lake City', '40.7547', '-111.892622'],
                                                      ['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                                                      ['Virginia', 'Richmond', '37.54', '-77.46']],503.30894852173606)

    # test - 5

    road_map_swap_5 = [['Alabama', 'Montgomery', '32.361538', '-86.279118'],
                 ['Alaska', 'Juneau', '58.301935', '-134.41974'],
                 ['Arizona', 'Phoenix', '33.448457', '-112.073844'],
                 ['Arkansas', 'Little Rock', '34.736009', '-92.331122'],
                 ['California', 'Sacramento', '38.555605', '-121.468926'],
                 ['Colorado', 'Denver', '39.7391667', '-104.984167'],
                 ['Connecticut', 'Hartford', '41.767', '-72.677'],
                 ['Delaware', 'Dover', '39.161921', '-75.526755'],
                 ['Florida', 'Tallahassee', '30.4518', '-84.27277'],
                 ['Georgia', 'Atlanta', '33.76', '-84.39'],
                 ['Hawaii', 'Honolulu', '21.30895', '-157.826182'],
                 ['Idaho', 'Boise', '43.613739', '-116.237651'],
                 ['Illinois', 'Springfield', '39.78325', '-89.650373'],
                 ['Indiana', 'Indianapolis', '39.790942', '-86.147685'],
                 ['Iowa', 'Des Moines', '41.590939', '-93.620866'],
                 ['Kansas', 'Topeka', '39.04', '-95.69'],
                 ['Kentucky', 'Frankfort', '38.197274', '-84.86311'],
                 ['Louisiana', 'Baton Rouge', '30.45809', '-91.140229'],
                 ['Maine', 'Augusta', '44.323535', '-69.765261'],
                 ['Maryland', 'Annapolis', '38.972945', '-76.501157'],
                 ['Massachusetts', 'Boston', '42.2352', '-71.0275'],
                 ['Michigan', 'Lansing', '42.7335', '-84.5467'],
                 ['Minnesota', 'Saint Paul', '44.95', '-93.094'],
                 ['Mississippi', 'Jackson', '32.32', '-90.207'],
                 ['Missouri', 'Jefferson City', '38.572954', '-92.189283'],
                 ['Montana', 'Helana', '46.595805', '-112.027031'],
                 ['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                 ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                 ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                 ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                 ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                 ['New York', 'Albany', '42.659829', '-73.781339'],
                 ['North Carolina', 'Raleigh', '35.771', '-78.638'],
                 ['North Dakota', 'Bismarck', '48.813343', '-100.779004'],
                 ['Ohio', 'Columbus', '39.962245', '-83.000647'],
                 ['Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'],
                 ['Oregon', 'Salem', '44.931109', '-123.029159'],
                 ['Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'],
                 ['Rhode Island', 'Providence', '41.82355', '-71.422132'],
                 ['South Carolina', 'Columbia', '34', '-81.035'],
                 ['South Dakota', 'Pierre', '44.367966', '-100.336378'],
                 ['Tennessee', 'Nashville', '36.165', '-86.784'],
                 ['Texas', 'Austin', '30.266667', '-97.75'],
                 ['Utah', 'Salt Lake City', '40.7547', '-111.892622'],
                 ['Vermont', 'Montpelier', '44.26639', '-72.57194'],
                 ['Virginia', 'Richmond', '37.54', '-77.46'],
                 ['Washington', 'Olympia', '47.042418', '-122.893077'],
                 ['West Virginia', 'Charleston', '38.349497', '-81.633294'],
                 ['Wisconsin', 'Madison', '43.074722', '-89.384444'],
                 ['Wyoming', 'Cheyenne', '41.145548', '-104.802042']]

    assert (swap_cities(road_map_swap_5, 5, 45)) == ([['Alabama', 'Montgomery', '32.361538', '-86.279118'],
                                                      ['Alaska', 'Juneau', '58.301935', '-134.41974'],
                                                      ['Arizona', 'Phoenix', '33.448457', '-112.073844'],
                                                      ['Arkansas', 'Little Rock', '34.736009', '-92.331122'],
                                                      ['California', 'Sacramento', '38.555605', '-121.468926'],
                                                      ['Virginia', 'Richmond', '37.54', '-77.46'],
                                                      ['Connecticut', 'Hartford', '41.767', '-72.677'],
                                                      ['Delaware', 'Dover', '39.161921', '-75.526755'],
                                                      ['Florida', 'Tallahassee', '30.4518', '-84.27277'],
                                                      ['Georgia', 'Atlanta', '33.76', '-84.39'],
                                                      ['Hawaii', 'Honolulu', '21.30895', '-157.826182'],
                                                      ['Idaho', 'Boise', '43.613739', '-116.237651'],
                                                      ['Illinois', 'Springfield', '39.78325', '-89.650373'],
                                                      ['Indiana', 'Indianapolis', '39.790942', '-86.147685'],
                                                      ['Iowa', 'Des Moines', '41.590939', '-93.620866'],
                                                      ['Kansas', 'Topeka', '39.04', '-95.69'],
                                                      ['Kentucky', 'Frankfort', '38.197274', '-84.86311'],
                                                      ['Louisiana', 'Baton Rouge', '30.45809', '-91.140229'],
                                                      ['Maine', 'Augusta', '44.323535', '-69.765261'],
                                                      ['Maryland', 'Annapolis', '38.972945', '-76.501157'],
                                                      ['Massachusetts', 'Boston', '42.2352', '-71.0275'],
                                                      ['Michigan', 'Lansing', '42.7335', '-84.5467'],
                                                      ['Minnesota', 'Saint Paul', '44.95', '-93.094'],
                                                      ['Mississippi', 'Jackson', '32.32', '-90.207'],
                                                      ['Missouri', 'Jefferson City', '38.572954', '-92.189283'],
                                                      ['Montana', 'Helana', '46.595805', '-112.027031'],
                                                      ['Nebraska', 'Lincoln', '40.809868', '-96.675345'],
                                                      ['Nevada', 'Carson City', '39.160949', '-119.753877'],
                                                      ['New Hampshire', 'Concord', '43.220093', '-71.549127'],
                                                      ['New Jersey', 'Trenton', '40.221741', '-74.756138'],
                                                      ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'],
                                                      ['New York', 'Albany', '42.659829', '-73.781339'],
                                                      ['North Carolina', 'Raleigh', '35.771', '-78.638'],
                                                      ['North Dakota', 'Bismarck', '48.813343', '-100.779004'],
                                                      ['Ohio', 'Columbus', '39.962245', '-83.000647'],
                                                      ['Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'],
                                                      ['Oregon', 'Salem', '44.931109', '-123.029159'],
                                                      ['Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'],
                                                      ['Rhode Island', 'Providence', '41.82355', '-71.422132'],
                                                      ['South Carolina', 'Columbia', '34', '-81.035'],
                                                      ['South Dakota', 'Pierre', '44.367966', '-100.336378'],
                                                      ['Tennessee', 'Nashville', '36.165', '-86.784'],
                                                      ['Texas', 'Austin', '30.266667', '-97.75'],
                                                      ['Utah', 'Salt Lake City', '40.7547', '-111.892622'],
                                                      ['Vermont', 'Montpelier', '44.26639', '-72.57194'],
                                                      ['Colorado', 'Denver', '39.7391667', '-104.984167'],
                                                      ['Washington', 'Olympia', '47.042418', '-122.893077'],
                                                      ['West Virginia', 'Charleston', '38.349497', '-81.633294'],
                                                      ['Wisconsin', 'Madison', '43.074722', '-89.384444'],
                                                      ['Wyoming', 'Cheyenne', '41.145548', '-104.802042']],
                                                     1059.0139332789988)

# def test_shift_cities():
#     road_map3 = [("Minnesota", "Saint Paul", 38.197274, -84.86311), \
#                  ("Kentucky", "Frankfort", 39.161921, -75.526755), \
#                  ("Delaware", "Dover", 44.95, -93.094)]
#     x2_x1 = (road_map3[2][2] - road_map3[1][2]) ** 2
#     y2_y1 = (road_map3[2][3] - road_map3[1][3]) ** 2
#     total_distance4 = pytest.approx(math.sqrt(x2_x1 + y2_y1), 0.01)
#     x4_x3 = (road_map3[0][2] - road_map3[1][2]) ** 2
#     y4_y3 = (road_map3[0][3] - road_map3[1][3]) ** 2
#     total_distance5 = pytest.approx(math.sqrt(x4_x3 + y4_y3), 0.01)
#
#     assert (total_distance4 == 18.50)  and (total_distance5 == 9.39)


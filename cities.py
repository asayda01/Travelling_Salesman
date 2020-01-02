import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from time import sleep
from tkinter import *
from random import choice
from math import sqrt
from random import randint
import random
from copy import copy
import copy

def read_cities(file_name):
    file_name1 = open(file_name, "r")
    list1,list2,list3=[],[],[]
    for line1 in file_name1:
        list2 = line1.rstrip().split("\t")
        list1.append(list2)
    for i in range(len(list1)):
        list3.append([list1[i][0], list1[i][1], (((list1[i][2]))), ((list1[i][3]))])
    return list3

def print_cities(road_map):
    list4=[]
    for i in range(0,len(road_map)):
        list4.append([road_map[i][0],road_map[i][1],(round((float(road_map[i][2])),2)),(round(float(road_map[i][3]),2))])
    print(*list4,sep="\n")

def compute_total_distance(road_map):
    total_dist1 = 0.0
    for i in range(0,len(road_map)):
        city_x1 = float(road_map[i][2])
        city_y1 = float(road_map[i][3])
        city_x2 = float(road_map[(i + 1) % len(road_map)][2])
        city_y2 = float(road_map[(i + 1) % len(road_map)][3])
        total_dist1 += sqrt(  ( (city_x2-city_x1)  ** 2)   + (    ( city_y2-city_y1 )  ** 2)   )
    return (total_dist1)

def swap_cities(road_map,index1,index2):
    new_road_map = copy.deepcopy(road_map)
    new_value_1 = new_road_map[index1]
    new_value_2 = new_road_map[index2]
    new_road_map[index1] = new_value_2
    new_road_map[index2] = new_value_1
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map,new_total_distance)

def shift_cities(road_map):
    new_shifted_road_map=[road_map[-1]] + road_map[:-1]
    return new_shifted_road_map

def find_best_cycle(road_map):
    min_dist = compute_total_distance(road_map)
    new_best_map = road_map
    count=0
    while (count <= 10000):
        index1 = int(len(new_best_map)* random.random())
        index2 = int(len(new_best_map)* random.random())
        new_route1 = (swap_cities(shift_cities(new_best_map), index1, index2)[0])
        new_dist = (swap_cities(shift_cities(new_best_map), index1, index2)[1])
        if new_dist < min_dist:
            min_dist = new_dist
            new_best_map = new_route1
        count += 1
    return new_best_map,min_dist

def print_map(road_map):
    road_map_last = road_map
    total_dist =0
    list5 = []
    for i in range(0,len(road_map_last) - 1):
        new_city_x3 = float(road_map_last[i][2])
        new_city_y3 = float(road_map_last[i][3])
        new_city_x4 = float(road_map_last[(i + 1) % len(road_map_last)][2])
        new_city_y4 = float(road_map_last[(i + 1) % len(road_map_last)][3])
        #new_dist1 = sqrt((new_city_x3 - new_city_x4) ** 2 + (new_city_y3 - new_city_y4) ** 2)
        new_dist1 = ((compute_total_distance([[str(),str(),new_city_x3,new_city_y3],[str(),str(),new_city_x4,new_city_y4]]))/2)
        total_dist += new_dist1
        new_line1 = " From City : " + road_map_last[i][1] + " ( " + " State : " +  road_map_last[i][0] + " ) to" +" City : "+ road_map_last[(i + 1) % len(road_map_last)][1] + " ( "  + " State : " + road_map_last[(i + 1) % len(road_map_last)][0]  + " ) " + " Distance : " + str(round(new_dist1, 2))
        list5.append(new_line1)
        list5.append("Total distance : ---> " + str(round(total_dist, 2)))
    print(*list5,sep="\n")

def main():
    file_name = "city-data.txt"
    #print("-------------------file-name-yazdik------------------------------------------------------------------")
    road_map= read_cities(file_name)
    #print("----------read-cities-(file_name)-yazdik--------------------------------------------------------------------------")
    print_cities(road_map)
    #print("--------------print_cities(road_map)---fonksyionunu-cagirdik---------------------------------------------------------------------")
    print(compute_total_distance(road_map))
    #print("----------------print---compute_total_distance(road_map)------------------------------------------------------------------")
    index1 = int(len(road_map) * random.random())
    index2 = int(len(road_map) * random.random())
    #print("-------------------index-1-2-yazdik-----------------------------------------------------------------")
    swap_cities(road_map, index1, index2)
    #print(swap_cities(road_map, index1, index2))
    #print("-------------------swap-cities-yazdik------------------------------------------------------------------")
    #print(*shift_cities(road_map),sep="\n")
    shift_cities(road_map)
    #print("-----------print-shift-cities--------------------------------------------------------------------------------------------------")
    print_map(road_map)
    #print("------------------print-road-map------------------------------------------------------------------------------------------------------------------")
    #print("--------------------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------------------")

"""
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
"""

if __name__ == "__main__": #keep this in
    main()

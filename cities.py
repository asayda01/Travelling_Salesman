# ----- ----- ----- MSc Data Science - Ahmet Cem Saydam - 13173584 - 2019/2020  ----- ----- ----- #
# ----- ----- ----- MSc Data Science - Ahmet Cem Saydam - 13173584 - 2019/2020  ----- ----- ----- #
# ----- ----- ----- MSc Data Science - Ahmet Cem Saydam - 13173584 - 2019/2020  ----- ----- ----- #

import tkinter
from tkinter import *
from tkinter import messagebox
import numpy as np
import math
import random
from random import choice
from math import sqrt
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
        list4.append([road_map[i][0],road_map[i][1],(round((float(road_map[i][2])),2)),
                      (round(float(road_map[i][3]),2))])
    print(*list4,sep="\n")

def compute_total_distance(road_map):
    total_dist1 = 0.0
    for i in range(0,len(road_map)):
        city_x1 = float(road_map[i][2])
        city_y1 = float(road_map[i][3])
        city_x2 = float(road_map[(i + 1) % len(road_map)][2])
        city_y2 = float(road_map[(i + 1) % len(road_map)][3])
        total_dist1 += sqrt( ( (city_x2-city_x1) ** 2)   + ( ( city_y2-city_y1 )  ** 2) )
    return (total_dist1)

def swap_cities(road_map,index1,index2):
    new_road_map = copy.deepcopy(road_map)
    if (index1!= index2):
        new_value_1 = new_road_map[index1]
        new_value_2 = new_road_map[index2]
        new_road_map[index1] = new_value_2
        new_road_map[index2] = new_value_1
        new_total_distance = compute_total_distance(new_road_map)
    else:
        index1 = int(len(new_road_map) * random.random())
        index2 = int(len(new_road_map) * random.random())
        new_road_map,new_total_distance = (swap_cities(new_road_map, index1, index2)[0]),\
                                          (swap_cities(new_road_map, index1, index2)[1])
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
    return new_best_map

def print_map(road_map):
    road_map_last = road_map
    total_dist =0
    list5 = []
    for i in range(0,len(road_map_last)):
        new_city_x3 = float(road_map_last[i][2])
        new_city_y3 = float(road_map_last[i][3])
        new_city_x4 = float(road_map_last[(i + 1) % len(road_map_last)][2])
        new_city_y4 = float(road_map_last[(i + 1) % len(road_map_last)][3])
        new_dist1 = ((compute_total_distance([[str(),str(),new_city_x3,new_city_y3],
                                              [str(),str(),new_city_x4,new_city_y4]]))/2)
        total_dist += new_dist1
        new_line1 = " From City : " + road_map_last[i][1] + " ( " + " State : " +  road_map_last[i][0] \
                    + " ) to" +" City : "+ road_map_last[(i + 1) % len(road_map_last)][1] + " ( "  \
                    + " State : " + road_map_last[(i + 1) % len(road_map_last)][0]  + " ) " \
                    + " Distance : " + str(round(new_dist1, 2))
        list5.append(new_line1)
        list5.append("Total distance : ---> " + str(round(total_dist, 2)))
    print(*list5,sep="\n")

def Visualizer(road_map):
    root = tkinter.Tk()
    canvas_width = 1250
    canvas_height = 625
    line_distance = 25
    visualize_1= tkinter.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
    root.title(" The Traveling Salesman ")
    visualize_1.pack(side=LEFT)

    exe_1 = Frame(root)
    exe_1.pack()

    best_route_2 = road_map
    minDistance = compute_total_distance(best_route_2)

    def dialog ():
        messagebox.showinfo(" Best Ciycle ",information_2 )
    information_2 = str(("Best Route : " + " From City : " + str(best_route_2[0][1]) + " ( State : " \
                         + str(best_route_2[0][0]) + " ) to City : " + str(best_route_2[-1][1]) + " ( State : " \
                         + str(best_route_2[-1][0]) + " ) " + " Minimum Distance : " + str(round(minDistance, 2))))
    button1 = Button(exe_1, text=" ---> Best Cycle <--- ", fg="white", bg="lightblue", command=dialog)
    button1.pack()

    for x in range(line_distance, canvas_width + line_distance, line_distance):
        visualize_1.create_line(x, line_distance, x, canvas_height, fill="blue", dash=())
    for y in range(line_distance, canvas_height + line_distance, line_distance):
        visualize_1.create_line(line_distance, y, canvas_width, y, fill="red", dash=())

    maximum_Longtt, minumum_Longtt = np.max([float(i[3]) for i in best_route_2]),\
                                     np.min([float(i[3]) for i in best_route_2])
    maximum_Latt, minumum_Latt = np.max([float(i[2]) for i in best_route_2]),\
                                 np.min([float(i[2]) for i in best_route_2])
    Longtt_Range = np.append([0], np.linspace(math.floor(minumum_Longtt),
                                              math.ceil(maximum_Longtt), int(canvas_width / line_distance) - 2))
    Latt_Range = np.append([0], np.flip(np.linspace(math.floor(minumum_Latt),
                                                    math.ceil(maximum_Latt), int(canvas_height / line_distance) - 2)))

    for x in range(line_distance, canvas_width - line_distance, line_distance):
        visualize_1.create_text(x + line_distance, line_distance, text=round((Longtt_Range[int(x / line_distance)]), 2),
                      angle=90, font=("Lucida Console", 9), fill='black')
    for y in range(line_distance, canvas_height - line_distance, line_distance):
        visualize_1.create_text(line_distance, y + line_distance, text=round((Latt_Range[int(y / line_distance)]), 2),
                      font=("Lucida Console", 9), fill='black')

    count = 0
    for i in best_route_2:
        count += 1
        differeance_Longtt = line_distance / abs(Longtt_Range[6] - Longtt_Range[5])
        inter_Longtt = differeance_Longtt * ((float(i[3])) - math.floor(minumum_Longtt))
        differeance_Latt = line_distance / abs(Latt_Range[6] - Latt_Range[5])
        inter_Latt = differeance_Latt * (math.ceil(maximum_Latt) - float(i[2]))
        my_color = "#" + "".join((choice(['0', '1', '2', '3', '4', '5', '6', '7', '8']) for _ in range(0, 9)))
        visualize_1.create_oval(inter_Longtt + 30, inter_Latt + 30, inter_Longtt + 50,
                                inter_Latt + 50, fill=my_color, outline=my_color)
        visualize_1.create_text(inter_Longtt + 40, inter_Latt + 40, text=str(count),
                                font=("Lucida Console", 9), fill='white')
        information_1=Label(text=(str(count),str(i[1]),str(i[0])),font=("Lucida Console", 9))
        information_1.pack(side=TOP)

    tkinter.mainloop()

def main():
    file_name = input("Please type a file name that contains the data (for example type :city-data) :")
    road_map= read_cities(("%s.txt" % (file_name)))
    print_cities(road_map)
    compute_total_distance(road_map)
    index1,index2 = int(len(road_map) * random.random()),int(len(road_map) * random.random())
    swap_cities(road_map, index1, index2)
    shift_cities(road_map)
    print_map(road_map)
    best_route_1 = find_best_cycle(road_map)
    Visualizer(best_route_1)

if __name__ == "__main__": #keep this in
    main()

# ----- ----- ----- MSc Data Science - Ahmet Cem Saydam - 13173584 - 2019/2020  ----- ----- ----- #
# ----- ----- ----- MSc Data Science - Ahmet Cem Saydam - 13173584 - 2019/2020  ----- ----- ----- #
# ----- ----- ----- MSc Data Science - Ahmet Cem Saydam - 13173584 - 2019/2020  ----- ----- ----- #

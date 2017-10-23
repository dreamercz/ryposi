#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def str2bool(str):
    if str == "0":
        return False
    else:
        return True

# Read the CSV file and save it as list of arrays
with open('F015_M062.csv', 'r') as csv_file:
    read_file = csv.reader(csv_file)
    ryposi_list = list(read_file)

# Turn the file into list of arrays each with separated values
prepared_ryposi_list = []
ryposi_list_all_times = []
for line in ryposi_list:
    new_line = line[0].split(";")
    prepared_ryposi_list.append(new_line)
    ryposi_list_all_times.append(new_line[0])

# Remove redundant times from the times list, note it orders the resulting list randomly
ryposi_list_all_times = list(set(ryposi_list_all_times))

# Group each four by time
i = 0
for line in ryposi_list_all_times:
    four_by_time = [array for array in prepared_ryposi_list if array[0] == ryposi_list_all_times[i]]
    # print(four_by_time)
    i += 1
    print("\n")

    for element in four_by_time:
        print(element)
        print(element[1])
        print(element[2])
        print(str2bool(element[1]) & str2bool(element[2]))

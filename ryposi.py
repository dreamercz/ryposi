#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy
import random


def str2bool(string):
    if string in ("1"):
        return bool(True)
    else:
        return bool(False)


# Read the CSV file and save it as list of arrays
with open('test.csv', 'r') as csv_file:
    read_file = csv.reader(csv_file)
    ryposi_list = list(read_file)

# Turn the file into list of arrays each with separated values
prepared_ryposi_list = []
ryposi_list_all_times = []
for line in ryposi_list:
    new_line = line[0].split(";")
    prepared_ryposi_list.append(new_line)
    ryposi_list_all_times.append(new_line[0])

# Remove redundant times from the times list, note that it orders the resulting list randomly for some reason
ryposi_list_all_times = list(set(ryposi_list_all_times))

# Group each four by time
for step in range(1):

    counted_x = 0
    i = 0
    for line in ryposi_list_all_times:
        four_by_time = [array for array in prepared_ryposi_list if array[0] == ryposi_list_all_times[i]]

        value_matrix = []
        for element in four_by_time:
            element = list(element)

            # Remove time stamp
            element.remove(ryposi_list_all_times[i])
            value_matrix.append(element)

        # Shuffle values in the column
        numpy.random.shuffle(value_matrix)
        # Turn the matrix on the side
        value_matrix = numpy.swapaxes(value_matrix, 0, 1)
        print(value_matrix)
        # Return logical AND when comparing both arrays
        truth_values = numpy.logical_and(numpy.array(value_matrix[0], dtype=bool), numpy.array(value_matrix[1], dtype=bool))
        print(truth_values)

        i += 1
    print("\nHodnota X pro beh cislo {}: {}".format(step, counted_x))
    step += 1

print("Celkovy pocet kroku: {}".format(step))

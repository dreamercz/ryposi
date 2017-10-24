#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy
import random
from typing import List


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

# Remove redundant times from the times list, note that it orders the resulting list randomly for some reason
ryposi_list_all_times = list(set(ryposi_list_all_times))

# Group each four by time
all_x = []  # type: List[int]
for step in range(10):

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

        print("Puvodni matice:\n{}".format(value_matrix))

        # Turn the matrix on the side
        value_matrix = numpy.swapaxes(value_matrix, 0, 1)
        print("Otocena matice:\n{}".format(value_matrix))

        # Shuffle values in each column
        random.shuffle(value_matrix[0])
        random.shuffle(value_matrix[1])
        print("Prohazena matice:\n{}".format(value_matrix))

        # Return logical AND when comparing both arrays
        truth_values = numpy.logical_and(numpy.array(value_matrix[0], dtype=bool), numpy.array(value_matrix[1], dtype=bool))
        print("Konjunkce obou poli:\n{}".format(truth_values))

        # Count the number of [1;1] matches towards this step's X value
        if True in truth_values:
            counted_x += 1

        i += 1

    print("\n Hodnota X pro beh cislo {}: {}\n---".format(step + 1, counted_x))
    all_x.append(counted_x)
    step += 1

print("Celkovy pocet kroku: {}".format(step))
print("Celkovy pocet hodnot X: {}".format(all_x))

# Compute overall p value

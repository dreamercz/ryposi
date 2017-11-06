#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy
import random
from typing import List  # noqa F401


# Configuration
synchron_file_path = "test/xxx.csv"
number_of_phases = 1000
doshuffle = True
TRUE_X = 0

# Read the CSV file and save it as list of arrays
with open(synchron_file_path, 'r') as csv_file:
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
all_xp_array = []  # type: List[int]
for step in range(number_of_phases):

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

        # print("-----\nPuvodni matice:\n{}".format(value_matrix))

        # Turn the matrix on the side
        value_matrix = numpy.swapaxes(value_matrix, 0, 1)
        # print("Otocena matice:\n{}".format(value_matrix))

        # Shuffle values in each column
        if doshuffle is True:
            random.shuffle(value_matrix[0])
            random.shuffle(value_matrix[1])
        # print("Prohazena matice:\n{}".format(value_matrix))

        # Return logical AND when comparing both arrays
        truth_values = numpy.logical_and(numpy.array(value_matrix[0], dtype=bool), numpy.array(value_matrix[1], dtype=bool))
        # print("Konjunkce obou poli:\n{}".format(truth_values))

        # Count the number of [1;1] matches towards this step's X value
        counted_x += sum(truth_values)
        # print(counted_x)
        # print(sum(truth_values))
        i += 1

    print("Hodnota X pro fazi cislo {}: {}".format(step + 1, counted_x))
    all_xp_array.append(counted_x)
    step += 1

print("Celkovy pocet fazi: {}".format(step))
print("Hodnoty X celkem: {}".format(all_xp_array))

# Compute overall p value
# Kolikrat jsou nahodne x vetsi nebo rovno pravemu x
occurences = 0
for value in all_xp_array:
    if value >= TRUE_X:
        occurences += 1
    else:
        pass

print("Nahodne ziskane xp jsou vyssi nebo rovny v celkem {} pripadech.".format(occurences))
p_value = occurences / step
print("P value = {}".format(p_value))

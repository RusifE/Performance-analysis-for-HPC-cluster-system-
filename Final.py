from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
import csv
import re # for grabing a part of the file name
import argparse # for optional arguments
parser = argparse.ArgumentParser()

#Argument
#('arg_name', nargs='?' means optional arg., help="Help message when we run 'python name.py -h'")
parser.add_argument('File1', help="Enter the file name to graph it | At least one file is required to graph")
parser.add_argument('File2', nargs='?', help="Enter the second file to graph both together")
parser.add_argument('File3', nargs='?', help="Enter the second file to graph all together")
parser.add_argument('-title',nargs='?', help="Overwrites the current title")

args=parser.parse_args()
    
# Opens the sorted hostnum.csv file and reads it; replaces the quotation marks.
# Python has built-in support for Windows, Linux and Mac line endings -(rtU):
# If the PY program is going to be run on Linux, use 'rtU' instead of 'r'ex: 
# f = open(filename, 'rtU')
Dict = {} 
csv_file = []
csv_file.append("placeholder")
with open('hostnum.csv', 'rtU') as host:
    for line in host.readlines():
        line = line.replace('"', '')
        line = line.strip('\n')
        rank, value = line.split("\t")
        Dict[value] = rank
        csv_file.append(value)

#File1
file1 = args.File1
file_1 = []
with open(file1, 'r') as f:
    csvreader = csv.reader(f, delimiter='\t')
    for line in csvreader:
        file_1.append([Dict[line [2]], line[9]])

# splits the words between - - symbols and takes the element #1
scatter1_label=re.split("[--]",file1)[1]
# scatter(start_pt, end_pt, size_of_symbol, color, label)
plt.scatter([int(item[0]) for item in file_1], [int(item[1]) for item in file_1], s=4, c='b', label=scatter1_label)
# wrapped title, unless specified by the user using -title
plt.title("\n".join(wrap("Performance for "+file1)), size = 12)

#File2
if args.File2:
    file2=args.File2
    file_2 = []
    with open(file2, 'r') as f:
        csvreader = csv.reader(f, delimiter='\t')
        for line in csvreader:
            file_2.append([Dict[line [2]], line[9]])
    scatter2_label=re.split("[--]",file2)[1]
    plt.scatter([int(item[0]) for item in file_2], [int(item[1]) for item in file_2], s=4, c='r', label=scatter2_label)
    plt.title("\n".join(wrap("Performance for "+file1+' & '+file2)), size = 12)

#File3
if args.File3:
    file3=args.File3
    file_3 = []
    with open(file3, 'r') as f:    
        csvreader = csv.reader(f, delimiter='\t')
        for line in csvreader:
            file_3.append([Dict[line [2]], line[9]])
    scatter3_label=re.split("[--]",file3)[1]
    plt.scatter([int(item[0]) for item in file_3], [int(item[1]) for item in file_3], s=4, c='g', label=scatter3_label)
    plt.title("\n".join(wrap("Performance for "+file1+' & '+file2 +' & '+file3)), size = 12)

# If title specified as an arg. it overwrites wrapped title for the graph using title arg.
if args.title:
    plt.title("\n".join(wrap(args.title)), size = 12)
    
# Indicates the label names at the given spot (location, shadow, edgecolor, space between marker and word)
# prop={'size':8})  -> if want to change size of the legend: 
# markerfirst=False -> if want the markers show after legend labels
plt.legend(loc='upper right', shadow=True, edgecolor = 'grey', handletextpad = 0.1)

# Creates grid for x-y axises
# plt.grid(True, linewidth = 0.25)
    
# x-y labels for the graph
# labelpad is the distance between x label and the xticks
plt.xlabel("Node Names", fontsize = 12, labelpad = 7)
plt.ylabel("Run Times", fontsize = 12)

# ticks - x and y axisses' data format (change both ::? values in order to change the frequency)
# size is the font size; (start, end_value, frequency)
# just in case if changed: item[0:5] 
plt.xticks(np.arange(1,len(csv_file))[::20], [item[0:5] for item in csv_file[1::20]], rotation=90, size=8)
plt.yticks(np.arange(0,11000,1000), size=8)

# Saves a PNG file of the current graph to the folder and updates it every time
# (nameOfimage, dpi=(sizeOfimage),Keeps_Labels_From_Disappearing)
# pic_name gets the Python file's name
pic_name = re.split("[.]",__file__)[0]
plt.savefig(pic_name, dpi=(250), bbox_inches='tight')
# Hard coded name: './test.png'

# Not to cut-off bottom labels(manually) - enlarges bottom
plt.gcf().subplots_adjust(bottom=0.15)

plt.show()


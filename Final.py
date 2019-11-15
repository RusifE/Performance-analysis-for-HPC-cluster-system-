
"""
    Developer:           Rusif Eyvazli
    Date:                07/15/2019
    Update:              11/15/2019
    Project link:        https://rusife.github.io/Performance-analysis-for-HPC-cluster-system-/
    Learn more about me: https://www.linkedin.com/in/rusifeyvazli/
    Contact:             eyvazlirusif@gmail.com
    
    Program name:        Performance analysis for HPC cluster system.
    Purpose:             Using this program, you can graph a scatter plot using hostnum.csv file for X-axis 
                         and at least one and at most three of the CSV files that include data to analyze 
                         a sample cluster system. 
    Copyright (C) <2019>  <Rusif Eyvazli>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pandas
import matplotlib
from matplotlib.pyplot import xticks
from matplotlib.animation import adjusted_figsize
matplotlib.use('TkAgg') # backend option for matplotlib
from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
import csv
import re # for grabbing a part of the file name
import argparse # for optional arguments
parser = argparse.ArgumentParser()

#Data (csv) file name needs to be in the format of: stats-NAME-.csv. There can be string before or after "-" symbol.
#Otherwise, please change the following in the code:
#from: " scatter#_label=re.split("[--]",file1)[1] "
#to:  " scatter#_label=file# "

#Arguments
#('arg_name', nargs='?' means optional arg., help="Help message when we run 'python name.py -h'")
parser.add_argument('File1', help="Enter the file name to graph it | At least one file is required to graph")
parser.add_argument('File2', nargs='?', help="Enter the second file to graph both together")
parser.add_argument('File3', nargs='?', help="Enter the second file to graph all together")
parser.add_argument('-title',nargs='?', help="Overwrites the current title")
parser.add_argument('-width',nargs='?', help=";Adjusts the width of the vertical lines")
# parser.add_argument('-size',nargs='?', help=";Adjusts the saved picture's size in pixels")
args=parser.parse_args()
    
# Opens the sorted hostnum.csv file and reads it; replaces the quotation marks.
# Python has built-in support for Windows, Linux and Mac line endings -(rtU):
# If the PY program is going to be run on Linux, use 'rtU' instead of 'r'. Ex: 
# f = open(filename, 'rtU')
Dict = {} #empty dictionary
List = [] #empty list
List.append("placeholder")

with open('hostnum.csv', 'rtU') as hostnum:
    for line in hostnum.readlines():
        line = line.strip('\n') #get rid of \n at the end of the line (due to Win/Linux environments change)
        rank, value = line.split("\t") #rank and value are seperated by tab; 
        Dict[value] = rank #each value gets an index number within dict: {'bc017.source.aa': '1', 'bc018.source.aa': '2', ... , 'mc252.source.aa': '387'}}
        List.append(value) #creates a list with first member as 'placeholder': ['placeholder', 'bc017.source.aa', ..., 'mc252.source.aa']]

#File1
file1 = args.File1
file_1 = []

#reads the file using pandas and appends them in dict by rows' index numbers and run times
data_file=pandas.read_csv(file1, sep="\t")
for row in data_file.itertuples(index=False, name=False):
    file_1.append([Dict[row [2]], row[9]])

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
    
    data_file=pandas.read_csv(file2, sep="\t")
    for row in data_file.itertuples(index=False, name=False):
        file_2.append([Dict[row [2]], row[9]])
            
    scatter2_label=re.split("[--]",file2)[1]
    
    plt.scatter([int(item[0]) for item in file_2], [int(item[1]) for item in file_2], s=4, c='r', label=scatter2_label)
    plt.title("\n".join(wrap("Performance for "+file1+' & '+file2)), size = 12)

#File3
if args.File3:
    file3=args.File3
    file_3 = []
    
    data_file=pandas.read_csv(file3, sep="\t")
    for row in data_file.itertuples(index=False, name=False):
        file_3.append([Dict[row [2]], row[9]])
        
    scatter3_label=re.split("[--]",file3)[1]
        
    plt.scatter([int(item[0]) for item in file_3], [int(item[1]) for item in file_3], s=4, c='g', label=scatter3_label)
    plt.title("\n".join(wrap("Performance for "+file1+' & '+file2 +' & '+file3)), size = 12)

# If title specified as an arg. it overwrites wrapped title for the graph using '-title' argument.
if args.title:
    plt.title("\n".join(wrap(args.title)), size = 12)
    
# Indicates the label names (location, shadow, edgecolor, space between marker and word)
# prop={'size':8})  -> if wants to change size of the legend: 
# markerfirst=False -> if wants the markers show after the legend labels
plt.legend(loc='upper right', shadow=True, edgecolor = 'grey', handletextpad = 0.1)

# Creates grid for x-y axises
#plt.grid(True, linewidth = 0.25)

    
# x-y labels for the graph
# 'labelpad' is the distance between x label and the X-ticks
plt.xlabel("Node Names", fontsize = 12, labelpad = 7)
plt.ylabel("Run Times (sec)", fontsize = 12)

# ticks - x and y axisses formats 
# change both ::? values in order to change the frequency
# size is the font size; (start, end_value, frequency)
# backup: plt.xticks(np.arange(1,len(List))[::20],[item[0:5] for item in List[1::20]], rotation=90,size=8)
plt.xticks(np.arange(1,len(List))[::20], [item[0:5] for item in List[1::20]], rotation=90, size=8)
plt.yticks(np.arange(0,11000,1000), size=8)


# Drawing vertical lines in the graph, if the file exists
try:
    colnames = ["Vertical Lines"]
    data = pandas.read_csv('vertical_lines.csv', names=colnames, header=0)
    vertical = data["Vertical Lines"]
    #print(vertical)

    for nodes in vertical:
        x = List.index(nodes + ".source.aa") #takes the index of the nodes from the column
        if args.width:
            plt.axvline(x,linewidth=args.width,zorder=1)
        else:
            plt.axvline(x,linewidth=0.5,zorder=1)
            
except FileNotFoundError:
    print()


# Saves a PNG file of the current graph to the folder and updates it every time
# (nameOfimage, dpi=(sizeOfimage),Keeps_Labels_From_Disappearing)
# pic_name gets the Python file's name
pic_name = re.split("[.]",__file__)[0]
plt.savefig(pic_name, dpi=100 )
# Hard coded name: './test.png'
#bbox_inches='tight'

# Not to cut-off bottom labels(manually) - enlarges bottom
plt.gcf().subplots_adjust(bottom=0.15)
plt.show()

# Analyzing Performance of HPC Cluster System using Python.

## About

Using this Python program, developed by me, _Rusif Eyvazli_, you can graph a scatter plot using _hostnum.csv_ file for X-axis and at least one and at most three of the CSV files that include data to analyze a sample cluster system. It reads _**Run Times**_ and _**Node Names**_ columns from the data file(s) and indexed _**Node Names**_ from _hostnum.csv_. The graph is being plotted using the indexed _**Node Names**_ in X-axis as X-ticks with corresponding values from the CSV data files.

## How to run
To run the program, please use the following command:

`python Final.py stats-firstFile-.csv`

You can add other two optional files and _-title_ optional argument to the command as following:

`python Final.py stats-firstFile-.csv stats-secondFile-.csv stats-thirdFile-.csv -title "Performance for GITHUB sample"`


_Let me know, if there are any recommendations or issues._

## License
**The contents of this repository are licensed under the GNU Affero General Public License v3.0**

    Copyright (C) <2019>  <Rusif Eyvazli>

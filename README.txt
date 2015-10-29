Test randomizer v. 0.1
Author: Alex Speaks (alex@speaks.io)
required python libraries : csv, random, argparse

installation:
=============
git clone the repository
#git clone https://github.com/logicalmethods/testrandomizer.git 

set the executable flag in the file system:
# chmod a+x testrandomizer.py

if your python executable is somewhere other than /usr/bin/python then update the #! line at the top of testrandomizer.py
# which python


CSV file:
=========
The csv file must be formatted correctly for this script to work:
1) do not title the columns, the very first row should contain useful data
2) place the required data as follows:
   1     |   2           |   3                |   ...
------------------------------------------------------------------
question |correct answer |incorrect answer 1  |incorrect answer n

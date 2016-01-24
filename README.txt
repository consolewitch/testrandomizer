Test randomizer v. 0.2
Author: Alex Speaks (alex@speaks.io)
required python libraries : csv, random, argparse

installation:
=============
Prerequesites:
 - git repository management software: http://git-scm.com/downloads
 - python: comes pre-installed on everything but Windows.
 - working understanding of the bash terminal (or similar)

 
Clone the testrandomizer repository from github.
# git clone https://github.com/logicalmethods/testrandomizer.git 

set the executable flag on the python script:
# chmod a+x testrandomizer/testrandomizer.py

run the script:
# .testrandomizer/testrandomizer.py

How to format your input CSV file:
==================================
The csv file must be formatted correctly for this script to work:
1) do not title the columns, the very first row should contain useful data
2) place the required data as follows:

   1     |   2           |   3                |   ...
------------------------------------------------------------------
question |correct answer |incorrect answer 1  |incorrect answer n

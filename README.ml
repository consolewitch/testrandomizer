Test randomizer v. 0.2
Please send suggestions to Alex Speaks (alex@speaks.io)
required python libraries : csv, random, argparse
Note: The following instructions are written for Apple users.


Installation:
=============
Prerequesites:
 - git repository management software: http://git-scm.com/downloads
 - python: comes pre-installed on everything but Windows.
 - working understanding of the terminal application

1) Open the "terminal" application in OSX and paste the following commands into its window.
Note: the hash mark (#) indicates a command and should be omitted from what you paste.

	A) Clone the testrandomizer repository from github.
	# git clone https://github.com/logicalmethods/testrandomizer.git 

	B) set the executable flag on the python script:
	# chmod a+x testrandomizer/testrandomizer.py


How to format your input CSV file:
==================================
The csv file must be formatted correctly for this script to work:

1) Create your CSV file using Microsoft Excel.  No other spreadsheet software is guaranteed to work.
1) Do not title the columns, the very first row should contain useful data.
2) place the required data as follows:

   1     |   2           |   3                |   ...
------------------------------------------------------------------
question |correct answer |incorrect answer 1  |incorrect answer n


Using the script:
=================
Example command to run the script.  Note that you should replace [jdoe] with your user name.
# ./testrandomizer/testrandomizer.py /Users/[jdoe]/Desktop/test_input.csv > /Users/[jdoe]/Desktop/test_output.txt


Optional command line parameters:
=================================
-h 		Print out help information.
-a 		Provide a correct answer key in output.
-n #    Specify the maximum number of choices the software will output (defaults to 4).



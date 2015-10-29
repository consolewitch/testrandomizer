#!/usr/bin/python

import csv, random, argparse

# deal with command line arguments
epilogText='''\
Excel generated CSV file must be in the format:
________________________________________________________________________________
|question text |correct answer |alternate answer |alternate answer |...
'''
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, prog='testrandomizer.py',description='Generate test with randomized answers.',epilog=epilogText)
parser.add_argument('filename', metavar='filename', type=str, help='path to the Excel csv file to convert')
parser.add_argument('-n', metavar='#', type=int, default='4',
                   help='number of possible answers. Note: csv must have sufficient answers available')
parser.add_argument('-a', action='store_true', default=False, help='specify whether to include the correct answers in output')
args=parser.parse_args()

#initialize variables
CSVFileName = args.filename
numOfOptions = args.n
lastAnswerPointer = numOfOptions -1 

#randomize answers and output formatted questions

try:
	with open(CSVFileName, 'rbU') as csvfile:
		inputCSV = csv.reader(csvfile, dialect='excel')
		for row in inputCSV:
			randomizedAnswers = [] #(re)initialize the randomizedAnswers list for each loop
			try:
				correctAnswerPointer = random.randint(0,lastAnswerPointer) 
			except ValueError:
				print "Error, you probably tried to pass a number of options fewer than 1"
				break
			question=row.pop(0)
			correctAnswer =row.pop(0)
			try:
				for i in range(0,numOfOptions):
					if i == correctAnswerPointer:
						randomizedAnswers.append(correctAnswer)
					else:
						randomizedAnswers.append(row.pop(random.randint(0,len(row)-1)))
			except ValueError:
				print "There are not enough wrong answers available in the Excel formated CSV file"
				break
			print '\n',question
			for index, answer in enumerate(randomizedAnswers):
				print chr(index+65),') ',answer	
			if args.a:
				print '\n',"correct answer is: ",chr(correctAnswerPointer +65)
except IOError:
	print "could not locate Excel formated CSV file"

				


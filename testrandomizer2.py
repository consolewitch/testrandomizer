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

class question:
	def __init__(self):
		self.questionText = ""
		self.correct = ""
		self.alternatives = []

	def putQuestionText(self, questionText):
		self.questionText=questionText

	def putCorrect(self, correct):
		self.correct=correct

	def pushAlternative(self, alternative):
		self.alternatives.append(alternative)

	def popRandomAlternative(self):
		try:
			alternative=self.alternatives.pop(random.randint(0,len(self.alternatives)-1))
		except ValueError:
			print "There are not enough wrong answers available in the Excel formated CSV file"
		return alternative

#initialize variables
CSVFileName = args.filename
maxNumOfOptions = args.n
#lastAnswerPointer = numOfOptions -1 




def readSource (CSVFileName):
	rawTestSource=[]
	try:
		with open(CSVFileName, 'rbU') as csvfile:
			inputCSV = csv.reader(csvfile, dialect='excel')
			for row in inputCSV:
				rawTestSource.append(question())
				rawTestSource[len(rawTestSource) -1].putQuestionText(row.pop(0))
				rawTestSource[len(rawTestSource) -1].putCorrect(row.pop(0))
				for i in range(0,len(row)-1):
					rawTestSource[len(rawTestSource) -1].pushAlternative(row.pop(0))
	except IOError:
		print "could not locate Excel formated CSV file"
	return rawTestSource

def randomizeTest (rawTestSource):
	return randomizedTest

def outputTest (randomizedTest):
	print randomizedTest

rawTestSource = readSource(CSVFileName)
#randomizedTest = randomizeTest(rawTestSource)
outputTest(rawTestSource)
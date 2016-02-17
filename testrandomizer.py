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
                   help='maximum number of possible answers. Note: csv must have sufficient answers available')
parser.add_argument('-a', action='store_true', default=False, help='specify whether to include the correct answers in output')
args=parser.parse_args()


# define question class
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

	def getQuestionText(self):
		return self.questionText

	def getCorrect(self):
		return self.correct

	def getNumOfAlternatives(self):
		return len(self.alternatives)

	def popRandomAlternative(self):
		try:
			alternative = self.alternatives.pop(random.randint(0,len(self.alternatives)-1))
			while alternative == "":
				alternative = self.alternatives.pop(random.randint(0,len(self.alternatives)-1))
			return alternative
		except:
			return None


#initialize variables
CSVFileName = args.filename
maxNumOfOptions = args.n


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
					alternative = row.pop(0)
					if alternative != "":
						rawTestSource[len(rawTestSource) -1].pushAlternative(alternative)
	except IOError:
		print "could not locate Excel formated CSV file"
	return rawTestSource

def randomizeTest (rawTestSource):
	randomizedTest=[]
	while len(rawTestSource) > 0:
		randomizedTest.append(rawTestSource.pop(random.randint(0,len(rawTestSource)-1)))
	return randomizedTest

def outputTest (randomizedTest,maxNumOfOptions):
	for count,item in enumerate(randomizedTest):
		print '\n',count+1,". ",item.getQuestionText(),'\n'
		if item.getNumOfAlternatives()+1 < maxNumOfOptions:
			totalNumOfAnswers=item.getNumOfAlternatives()+1
		else:
			totalNumOfAnswers=maxNumOfOptions
		correctAnswerPointer=random.randint(0,totalNumOfAnswers-1)
		for j in range(0,totalNumOfAnswers):
			if j != correctAnswerPointer:
				print chr(j+65),') ',item.popRandomAlternative()
			else:
				print chr(j+65),') ',item.getCorrect()
		if args.a:
			print '\n',"correct answer is: ",chr(correctAnswerPointer +65)

rawTestSource = readSource(CSVFileName)
randomizedTest = randomizeTest(rawTestSource)
outputTest(randomizedTest,maxNumOfOptions)
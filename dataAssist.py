# coding: utf-8
import csv
import numpy as np
import utils
import pdb
import pickle
max_train = None
max_steps = None

class DataAssistMatrix():
    def __init__(self):
        print('Build a DataAssistMatrix')

        self.longest = 100
        self.questions = []
        self.n_questions = 0
        self.max_questionID = 0
        self.trainData = []

    def build(self):
        print('Loading data...')
        #training process
        root = '../'
        trainPath = root + 'processed_data.csv'
        csvFile = open(trainPath, 'r')
        csvInput = csv.reader(csvFile)
        count = 0
        trainData = []
        '''
        we assume self.questions is useless, we only need self.n_questions
        '''
        totalAnswers = 0
        while(True):
            student = self.loadStudent(csvInput)
            if student == None:
                print ('Load student failed !')
                break
            if(student.n_answers >= 2 and student.n_answers<=self.longest):
                trainData.append(student)
            if len(trainData) % 100 == 0:
                print ('The length of train data is now ',len(trainData))
            totalAnswers = totalAnswers + student.n_answers
        self.trainData = trainData
        csvFile.close()


    def loadStudent(self, csvInput):
        try:
            nStep = next(utils.inputStudent(csvInput))
            questionsID = next(utils.inputStudent(csvInput))
            correct = next(utils.inputStudent(csvInput))
        except:
            print ('execption loadStudent')
            return None
        # if nStep == None or questionsID == None or correct == None:
        #     return None
        n = int(nStep[0])
        if(max_steps != None):
            n = max_steps
        for i in  range(len(questionsID)):
            if questionsID[i] not in self.questions:
                self.questions.append(questionsID[i])
                self.n_questions = self.n_questions + 1
        stu = student(n,questionsID,correct)
        if max(stu.questionsID) > self.max_questionID:
            self.max_questionID = max(stu.questionsID)
        return stu

class student():
    def __init__(self,n,questionsID,correct):
        self.n_answers = n
        self.questionsID = np.zeros(n,int)
        self.correct = np.zeros(n,int)
        for i in  range(n):
            if i > n:
                break
            self.questionsID[i] = int(float(questionsID[i])) # we don't plus 1 as the origin code
        for i in  range(n):
            if i > n:
                break
            self.correct[i] = int(float(correct[i]))
#
#fn = 'data.pkl'
#data = DataAssistMatrix()
#data.build()
#with open(fn, 'wb') as f:                     # open file with write-mode
#    picklestring = pickle.dump(data, f)   # serialize and save object
#    print("pkl files saved !")



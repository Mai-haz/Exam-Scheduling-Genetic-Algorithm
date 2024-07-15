#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rnd


# In[2]:


import prettytable as prettytable
import random as rnd
from random import choice
import numpy as np
import pandas as pd 

ESchedules = 2
mutation = 0.1
randomSelection = 3
populationSize = 6


# In[3]:


class InputData:
    def __init__(self):    
        
        self._examTime = ['9:00-11:00','12:00-2:00']
        self._days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        self._numofclasses = 10
        self._StudentsPerClass = 15
        self._examDur = 2
        self._teachers  = ['Mayhan', 'Sara', 'Ilham' , 'sadia' , 'iqra' , 'ali' , 'farah']

        #...............store Students and their respective Courses in Student Class Object.................
        
        self._student=['arsalan', 'jahan', 'tamorr' , 'zakir' , 'nadir' , 'sobia' , 'kaneez' , 'aleena' , 'nory' , 'Jay']
        self._sCourse=['Maths', 'English', 'Science' , 'history' , 'Biology' , 'physics' , 'geology' , 'chemistry' , 'cs' , 'css']
        self._Student = []
        for i in range (0,10):
            self._Student.append(Student(self._student[i],self._sCourse[i]))
   
        #................store Course, its respective Code and room in Course Class Object.................
        self._rooms = ['C401', 'C402', 'C403' , 'C404' , 'A301' , 'A302' , 'A303' , 'B201' , 'B202' , 'B203']
        self._course = ['Maths', 'MathsAdvance', 'Science', 'Scientology', 'Ediology', 'fermentology', 'Gestronomy', 'HPChemistry', 'Advancedjet', 'Aerodynamics']
        self._courseCode = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']
        self._Course = []
        for i in range(0, 10):
            room = self._rooms[rnd.randrange(0, len(self._rooms))]
            self._Course.append(Course(self._course[i], self._courseCode[i], room))
 
                   
    def getDay(self):
        return self._days
    def getRoom(self):
        room = self._rooms[rnd.randrange(0, len(self._rooms))]
        return room
    def getTeacher(self):
        teach = self._teachers[rnd.randrange(0, len(self._teachers))]
        return teach
    def getCourse(self):
        return self._Course
    def getExamTime(self):
        time = self._examTime[rnd.randrange(0, len(self._examTime))]
        return time
    def getnumofclasses(self):
        return self._numofclasses
    def getStudent(self):
        return self._Student
    def getsCourse(self):
        return self._sCourse


# In[4]:


class Schedule:
    def __init__(self):
        self._data = data
        self._exams = []
        self._conflicting = 0
        self._fitness = -1
        self._Noexam = 0
        self._FitnessChanged = True
        self._sorted = []
    def getExam(self):
        self._FitnessChanged = True
        return self._exams
    def getConflict(self):
        return self._conflicting
    
    #check if fitness has changed
    def getFitness(self):
        if (self._FitnessChanged == True):
            self._fitness = self.calculateFitness()
            self._FitnessChanged = False
        return self._fitness
    
    #Initialize Exam
    def initialize(self):
        days = self._data.getDay()
        for i in range(0, len(days)):
            timeSlot = self._data.getExamTime()
            courses = self._data.getCourse()
            for j in range(0, len(timeSlot)):
                temp = rnd.randrange(0, len(courses))
                NExam = Exam(self._Noexam, courses[temp] , courses[temp]._code)
                self._Noexam += 1
                NExam.setDay(days[rnd.randrange(0,len(days))])
                NExam.setExamTime(data.getExamTime())
                NExam.setRoom(courses[j].getFreeRoom()[rnd.randrange(0, len(courses[j].getFreeRoom()))]) 
                self._exams.append(NExam)
        return self
    
    #.............sorting exams according to time and day................
    def sortDays(self):
        exams = self.getExam()
        
        firstHour = []
        secondHour = []
        thirdHour=[]
        
        Tmonday =[]
        Ttuesday = []
        Twednesday = []
        Tthursday = []
        Tfriday = []
        
        #...............seperating shifts of exams ................
        
        for i in range(0, len(exams)):
            if exams[i].getExamTime() == '9:00-11:00':
                firstHour.append(exams[i])
            if exams[i].getExamTime() == '12:00-2:00':
                secondHour.append(exams[i])
            elif exams[i].getExamTime() == '3:00-5:00':
                thirdHour.append(exams[i])
        
        #..............First Hour...............
        
        for i in range(0, len(firstHour)):
            if firstHour[i].getDay() == 'Monday':
                Tmonday.append(firstHour[i])
            elif firstHour[i].getDay() == 'Tuesday':
                Ttuesday.append(firstHour[i])
            elif firstHour[i].getDay() == 'Wednesday':
                Twednesday.append(firstHour[i])
            elif firstHour[i].getDay() == 'Thursday':
                Tthursday.append(firstHour[i])
            elif firstHour[i].getDay() == 'Friday':
                Tfriday.append(firstHour[i])
          
        #..............Second Hour...............
        
        for i in range(0, len(secondHour)):
            if secondHour[i].getDay() == 'Monday':
                Tmonday.append(secondHour[i])
            elif secondHour[i].getDay() == 'Tuesday':
                Ttuesday.append(secondHour[i])
            elif secondHour[i].getDay() == 'Wednesday':
                Twednesday.append(secondHour[i])
            elif secondHour[i].getDay() == 'Thursday':
                Tthursday.append(secondHour[i])
            elif secondHour[i].getDay() == 'Friday':
                Tfriday.append(secondHour[i])
                
        #..............Third Hour...............

 
        self._sorted = [Tmonday, Ttuesday, Twednesday, Tthursday, Tfriday]
        return self   
    
    def getSorted(self):
        return self._sorted
    
    #...................checking if a student has 2 exams at the same time and day......................
    def examConflict(self):
        stud= data.getStudent()
        exam = self.getExam()
        brk1=0
        brk2=0
        for i in range(0, len(exam)):
            for j in range(i+1, len(exam)):
                if exam[i].getDay()==exam[j].getDay() and exam[i].getExamTime() == exam[j].getExamTime():
                    if(brk1==0):
                        for k in range (0 , len(stud)):
                            if stud[k].getCourse()== exam[i].getcourseCode():
                                for l in range (k+1 , len(stud)):
                                    if stud[l].getCourse()== exam[j].getcourseCode():
                                        if stud[k].getName()==stud[l].getName() and stud[k].getCourse()!=stud[l].getCourse():
                                            if(brk2==0):
                                                brk1+=1
                                                brk2+=1
                                                return True
        return False
    
    #....................calculating fitness...............................
    def calculateFitness(self):
        self.sortDays()
        self._conflicts = 0
        fl = 0
        exams = self.getExam()
        for i in range(0, len(exams)):
            if self.examConflict() == True:
                if fl==0:
                    self._conflicts += 0.5
                    fl+=1
            for j in range(0, len(exams)):
                if (j >= i):
                    
                    #.teacher check
                    
                    if ((exams[i].getExamTime() == exams[j].getExamTime() and exams[i].getDay() == exams[j].getDay()) and exams[i].getID() != exams[j].getID()):
                        if exams[i].getTeachers() == exams[j].getTeachers():
                            self._conflicts += 1
                            
                    #.teacher consec check
                    
                    if ((exams[i].getExamTime() != exams[j].getExamTime() and exams[i].getDay() == exams[j].getDay()) and exams[i].getID() != exams[j].getID()):
                        if exams[i].getTeachers() == exams[j].getTeachers():
                            self._conflicts += 1
        if self._conflicts==0.4:
            self._conflicts=0
        return 1 / (1.0*self._conflicts + 1)

    
    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._exams)-1):
            returnValue += str(self._exams[i]) + ", "
        returnValue += str(self._exams[len(self._exams) - 1])
        return returnValue


# In[5]:


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedule = []
        for i in range(0, size):
            self._schedule.append(Schedule().initialize())
    def getSchedules(self):
        return self._schedule


# In[6]:


class GeneticAlgorithm:
    def evolving(self, population):
        return self.mutatePopulation(self.crossoverPopulation(population))

    #..............crossover .....................
    def crossoverPopulation(self, pop):
        crossoverPop = Population(0)
        for i in range(ESchedules):
            crossoverPop.getSchedules().append(pop.getSchedules()[i])
        i = ESchedules
        while i < populationSize:
            schedule1 = self.randomPopulation(pop).getSchedules()[0]
            schedule2 = self.randomPopulation(pop).getSchedules()[0]
            crossoverPop.getSchedules().append(self.crossoverSchedule(schedule1, schedule2))
            i += 1
        return crossoverPop

    #..............performing mutation on population.....................
    def mutatePopulation(self, population):
        for i in range(ESchedules, populationSize):
            self.mutateSchedule(population.getSchedules()[i])
        return population

    #..............performing crossover on population.....................
    def crossoverSchedule(self, schedule1, schedule2):
        crossoverSch = Schedule().initialize()
        for i in range(0, min(len(crossoverSch.getExam()) , len(schedule1.getExam()) , len(schedule2.getExam()))):
            if (rnd.random() > 0.5):
                crossoverSch.getExam()[i] = schedule1.getExam()[i]
            else:
                crossoverSch.getExam()[i] = schedule2.getExam()[i]
        return crossoverSch

    #..............performing mutation on population.....................
    def mutateSchedule(self, mSchedule):
        schedule = Schedule().initialize()
        for i in range(0, min(len(mSchedule.getExam()),len(schedule.getExam()) )):
            if (rnd.random() < mutation):
                mSchedule.getExam()[i] = schedule.getExam()[i]
        return mSchedule

    #..............roulette population.....................
    def randomPopulation(self, pop):
        randomPop = Population(0)
        sch = pop.getSchedules()
        sum = 0
        for i in range(0, len(sch)):
            sum += sch[i].getFitness()
        pickChoice    = rnd.uniform(0, sum)
        choice = 0
        j = 0
        for i in range(0, len(sch)):
            choice += sch[i].getFitness()
            if choice > pickChoice and j < randomSelection:
                randomPop.getSchedules().append(pop.getSchedules()[i])
                j += 1
        randomPop.getSchedules().sort(key=lambda x: x.getFitness(), reverse = True)
        return randomPop


# In[7]:


class Student:
    def __init__(self, name, course):
        self._name = name
        self._course = course   
    def getName(self):
        return self._name
    def getCourse(self):
        return self._course


# In[8]:


class Exam:
    def __init__(self, id, course,courseCode):
        self._course = course
        self.courseCode = courseCode
        self._id = id
        self._day = None
        self._examTime = None
        self._room = None
    def getCourse(self):
        return self._course
    def getcourseCode(self):
        return self.courseCode
    def getID(self):
        return self._id   
    def getTeachers(self):
        return data.getTeacher()
    def getStudent(self):
        return data.getStudent()
    def getExamTime(self):
        return self._examTime
    def getRoom(self):
        return data.getRoom()
    def getDay(self):
        return self._day
    def setExamTime(self, examTime):
        self._examTime = examTime
    def setRoom(self, room):
        self._room = room
    def setDay(self, day):
        self._day = day
    def __str__(self):
        return self._name


# In[9]:


class Course:
    def __init__(self, name, code, freeRoom):
        self._name = name
        self._code = code
        self._freeRoom = freeRoom
        
    def getName(self):
        return self._name
    def getCode(self):
        return self._code
    def getFreeRoom(self):
        return self._freeRoom
    def __str__(self):
        return self._name


# In[ ]:


class Displaying:
    def printData(self):
        print ("available data")
        self.printInpData()
        
    #..................printing input data in pretty table.....................
    def printInpData(self):
        student = data.getStudent()
        k = 1
        
        inpDataTable = prettytable.PrettyTable(['Student', 'Course', 'Exam #', 'Duration', 'Teacher', 'Classroom'])
        for i in range(0, len(student)):
            courses = student[i].getCourse()
            course = data.getCourse()
            for j in range(0, len(courses)):
                if courses== course[j].getCode():
                    
                    inpDataTable.add_row([student[i].getName(),courses,str(k),'2 hrs',data.getTeacher(),course[j].getFreeRoom(),] )
                    k+=1
        print(inpDataTable)
 
    #..................printing generations in pretty tables...................
    def printGen(self, population):
        schedule = population.getSchedules()
        students =data.getStudent()
        for i in range(0, len(schedule)):
            print("\nChromosome ", i+1, " Fitness: ", round(schedule[i].getFitness(), 3), " Conflicting: ", schedule[i].getConflict())
            table1 = prettytable.PrettyTable(['Day', 'Time', 'Course', 'Teacher', 'Room'])
            table1 = prettytable.PrettyTable(['Teacher', 'Course', 'Day', 'Time', 'Room'])
            schedule[i].sortDays()
            sortedDays = schedule[i].getSorted()
            for j in range(0, len(sortedDays)):
                exams = sortedDays[j]
                for k in range(0, len(exams)):
                    #,exams[k].getStudent()[k].getName() 
                    table1.add_row([exams[k].getTeachers(),exams[k].getCourse(),exams[k].getDay(),exams[k].getExamTime(),exams[k].getRoom()])
            print(table1)

#...................Driver Code....................
data = InputData()
displaying = Displaying()
displaying.printData()
generationNumber = 0
print ("\n Generation No. " + str(generationNumber))
population = Population(populationSize)
population.getSchedules().sort(key=lambda x: x.getFitness(), reverse = True)
displaying.printGen(population)
geneticAlgo = GeneticAlgorithm()
while (population.getSchedules()[0].getFitness() != 1.0 or population.getSchedules()[0].getConflict != 0):
    if population.getSchedules()[0].getFitness() == 1.0 or population.getSchedules()[0].getConflict == 0:
        print ("\n Generation # " + str(generationNumber+1))
        displaying.printGen(population)
        break
        
    generationNumber += 1
    print ("\n Generation No. " + str(generationNumber))
    population = geneticAlgo.evolving(population)
    population.getSchedules().sort(key=lambda x: x.getFitness(), reverse = True)
    displaying.printGen(population)


# In[ ]:





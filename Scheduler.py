import sys

class Task:
	def __init__(self, taskName, compTime, dueDate):
		self.taskName = taskName
		self.compTime = compTime
		self.dueDate = dueDate

def userInput(tasks):	
	while(True):
		proceed = raw_input("Type 'A' to add a task to your schedule and 'F' if you are finished.\n")
		proceed.strip()
		proceed = proceed.lower()
		while(proceed != "f" and proceed != "a"):
			proceed = raw_input("Sorry, input does not match the desired format, Type 'A' or 'F'.\n")
			proceed.strip()
			proceed = proceed.lower()
		if proceed == "f":
			break
		taskName = raw_input("What is the name of your task?\n")
		taskName.strip()
		compTime = input("How many hours will your task take?\n")
		while(compTime > 24 or compTime<1):
			compTime = input("Enter a valid time between 1-24 hours\n")
		pm = raw_input("Is your task due in the afternoon? Type 'AM' or 'PM'.\n")
		pm.strip()
		pm = pm.lower()
		while(pm != "pm" and pm != "am"):
			pm = raw_input("Sorry, type 'AM' or 'PM'\n")
			pm.strip()
			pm = pm.lower()
		dueDate = input("What hour is it due?\n")
		while(dueDate > 12 or dueDate <1 ):
			dueDate = input("Enter a valid hour between 1 and 12, Thanks!\n")		
		if pm == "pm":
			dueDate += 12
		task = Task(taskName, compTime, dueDate)
		tasks.append(task)
		
def orderTasks(tasks):
	change = True
	while(change):
		change = False
		i = 0
		while (i < len(tasks)-1):
			if tasks[i].dueDate > tasks[i+1].dueDate:
				swap = tasks[i]
				tasks[i] = tasks[i+1]
				tasks[i+1] = swap
				change = True
			i+=1

def schedTest(tasks, start):
	schedulable = True
	i = 0
	while i < len(tasks):
		c = start
		k = i
		while(k >= 0):
			c = c + tasks[k].compTime
			k = k - 1
		if(c > tasks[i].dueDate):
			schedulable = False
		i +=1
	return schedulable
		

def main():
	schedulable = False
	while(schedulable == False):
		tasks = []
		userInput(tasks)
		orderTasks(tasks)
		start = input("When do you want to start your day?\n")
		while(start <1 or start>12):
			start = input("You can not be awake during the time you entered, please choose a time between 1-12!\n")
		schedulable = schedTest(tasks, start)

		if(schedulable):
			print("Here is the order you should complete your tasks to finish on time")
			c=start
			for task in tasks:
				print("start " + task.taskName +" at "+ str(c))
				c+=task.compTime
		else:
			print("Sorry, you cannot complete all your tasks today")
			print("If you would like, you can enter your task set again")
			print("With less tasks or less completition time to produce")
			print("a doable schedule.  If you do not want to do this type")
			cont = raw_input("'break' to exit.  Otherwise press any key to continue\n")
			cont.strip()
			cont = cont.lower()
			if cont == "break":
				schedulable = True
main()

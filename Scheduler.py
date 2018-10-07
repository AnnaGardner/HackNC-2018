import sys

class Task:
	def __init__(self, taskName, compTime, dueDate):
		self.taskName = taskName
		self.compTime = compTime
		self.dueDate = dueDate

def userInput(tasks):	
	while(True):
		proceed = raw_input("Type A to add a task to your schedule and F if you are finished\n")
		proceed.strip()
		if proceed == "F":
			break
		taskName = raw_input("What is the name of your task?\n")
		taskName.strip()
		compTime = input("How many hours will your task take?\n")
		dueDate = input("What hour is it due?\n")
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
	tasks = []
	userInput(tasks)
	orderTasks(tasks)
	start = input("When do you want to start your day?\n")
	schedulable = schedTest(tasks, start)

	if(schedulable):
		print("Here is the order you should complete your tasks to finish on time")
		for task in tasks:
			print(task.taskName)
	else:
		print("Sorry, you cannot complete all your tasks today\n")
main()

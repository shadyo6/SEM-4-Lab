MAX = 3

def enQueue(Queue):
	if (len(Queue) == MAX):
		print("Queue overflow")
	else:
		item = int(input("Enter item to enqueue: "))	
		Queue.append(item)

def dispQueue(Queue):
	if(len(Queue) == 0):
		print("Queue Empty")
	else:
		for item in Queue:
			print(item, end='\t')

def deQueue(Queue):
	if(len(Queue) == 0):
		print("Queue Underflow")
	else:
		return Queue.pop(0)

def qFront(Queue):
	if(len(Queue) == 0):
		print("Queue Empty")
	else:
		return Queue[0]

def qRear(Queue):
	if(len(Queue) == 0):
		print("Queue Empty")
	else:
		return Queue[len(Queue)-1]

def main():
	Queue=[]
	while True:
		print("1.EnQueue\t2.DeQueue\t3.DispQueue\t4.QFront\t5.QRear    \t6.Exit")
		ch = int(input("Enter your choice: "))

		if(ch == 1):
			enQueue(Queue)
		elif(ch == 2):
			print("Dequeued item is: ", deQueue(Queue))
		elif(ch == 3):
			dispQueue(Queue)
		elif(ch == 4):
			print("Queue front is: ", qFront(Queue))
		elif(ch == 5):
			print("Queue rear is: ", qRear(Queue))
		elif(ch == 6):
			exit()
		else:
			print("Invalid input, please try again")

if __name__=="__main__":
	main()

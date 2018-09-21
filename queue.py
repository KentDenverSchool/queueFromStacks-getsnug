class Node:
	def __init__(self, newData, pointer):
		self.pointer = pointer
		self.data = newData
	def getData(self):
		return self.data
	def changeData(self, data):
		self.data = data
	def addNode(self, newNode):
		self.pointer = newNode
	def rmNode(self, index):
		del self.pointer
	def getNode(self):
		return self.pointer
class Stack:
	def __init__(self):
		self.topNode = None
		self.sizeVar = 0
	def size(self):
		return(self.sizeVar)
	def push(self, newData):
		self.sizeVar += 1
		self.topNode = Node(newData, self.topNode)
	def peek(self):
		if(self.topNode!=None):
			return(self.topNode.getData())
		else:
			return None
	def isEmpty(self):
		if(self.sizeVar==0):
			return True
		return False
	def pop(self):
		if(self.topNode!=None):
			self.sizeVar -= 1
			temp = self.topNode.getData()
			self.topNode = self.topNode.getNode()
			return(temp)
		else:
			return None
class Queue:
	def __init__(self):
		self.inbox = Stack()
		self.outbox = Stack()
	def size(self):
		return self.outbox.size()+self.inbox.size()
	def isEmpty(self):
		return self.outbox.isEmpty and self.inbox.isEmpty()
	def enqueue(self, item):
		self.inbox.push(item)
	def peek(self):
		if self.outbox.size()==0:
			transfer=self.inbox.pop()
			while transfer!=None:
				self.outbox.push(transfer)
				transfer=self.inbox.pop()
		return self.outbox.peek()

	def dequeue(self):
		elem=self.peek()
		self.outbox.pop()
		return elem

queue = Queue()
print(queue.size())
queue.enqueue("element")
print(queue.size())
queue.enqueue("element2")
queue.enqueue("element3")
print(queue.size())
print(queue.dequeue())
print(queue.size())
print(queue.peek())
print(queue.size())
print(queue.dequeue())
print(queue.size())
print(queue.dequeue())
print(queue.size())
print(queue.dequeue())
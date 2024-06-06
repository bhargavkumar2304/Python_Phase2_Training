#problem 1 expand string
"""
g=input()
for i in range(1,len(g),2):
    print(g[i]*int(g[i-1]),end="")    
"""
#problem 2 decomposing a string
"""
g = input()
s=[]
i=0
while i < len(g):
    num_str = ""
    while i < len(g) and g[i].isdigit():
        num_str += g[i]
        i += 1
        
    if num_str:  
        count = int(num_str)
        if i < len(g):
            char = g[i]
            s.append(char * count)
            i += 1
    
print(''.join(s))
"""
#aschii value of string
"""
s=input()
asciivalue=0
for i in s:
    print(i,"\t",ord(i))
    asciivalue+=ord(i)
print(asciivalue)
"""
#recusrsive function to find factorial
"""
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))
"""
#recusrsive function to print nth fibonacci number
"""
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

n=int(input())
print(fibonacci(n))
"""
#print fibonacci series
"""
n=int(input())
a=0
b=1
print("0 1",end=" ")
for i in range(n):
   c=a+b
   print(c,end=" ")
   a=b
   b=c
"""
#recusrsive function to print fibonacci series upto n
"""
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        print(fib(n-1)+fib(n-2))
n=int(input())
fib(n)
print("0 1",end=" ")
"""
#stack
"""
class Stack:
    def __init__(self):
        self.stack=[]
        self.size=5
        self.top=-1

    def push(self,data):
        if self.top==self.size:
            print("Stack overflow")
        else:
            self.stack.append(data)
            self.top+=1

    def pop(self):
        if self.top==-1:
            print("Stack is underflow")
        else:
            self.stack.remove(self.stack(self.top))
            
    def peek(self):
        if self.top==-1:
            print("Stack is underflow")
        else:
            print(self.stack(self.top))
    def display(self):
        if self.top==-1:
            print("Stack is underflow")
        else:
            for i in range(0,self.top+1):
                print(self.stack(i),end=" ")

obj=Stack()
obj.push(5)
obj.push(6)
obj.push(7)
obj.pop()
obj.peek()
obj.display()
"""

#Queue
"""
class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print("Queue is empty")

    def display(self):
        if self.queue:
            for i in self.queue:
                print(i,end=" ")
        else:
            print("Queue is empty")

obj=Queue()
obj.dequeue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.display()
obj.dequeue()
obj.display()
"""
#factorial using stack

class Stack:
    def __init__(self):
        self.stack=[]
        self.size=5
        self.top=-1

    def push(self,data):
        if self.top==self.size:
            print("Stack overflow")
        else:
            self.stack.append(data)
            self.top+=1

    def display(self):
        if self.top==-1:
            print("Stack is underflow")
        else:
            for i in range(0,self.top+1):
                print(self.stack[i],end=" ")
            
n=int(input())
if n==0 or n==1:
    print("1")
obj=Stack()
res=1
for i in range(1,n+1):
    obj.push(i)
obj.display()
for i in obj.stack:
    res*=i
print("\n",res)

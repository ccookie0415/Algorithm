

def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

queue =[0] * 10
front = -1
rear = -1

enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())

print(queue)

q = []
q.append(10)
q.append(20)
q.append(30)
print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
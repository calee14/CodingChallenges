class Stack(object):

    def __init__(self):
        self.stack = []

    def __repr__(self):
        """Defining a __repr__ function will enable us to print the
        stack contents, and facilitate debugging."""
        return repr(self.stack) # Good enough.

    def push(self, x):
        """The "top" of the stack is the end of the list."""
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if len(self.stack) > 0 else None

    def isempty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)
    
    def __iter__(self):
        for el in self.stack:
            yield el
            
    def __getitem__(self, i):
        return self.stack[i]
    
    def __contains__(self, x):
        return x in self.stack
    
s = Stack()
    
print(s.pop())
s.push('a')
s.push('b')
print(s.pop())
print(s.pop())
print(s.pop())

class Queue(object):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        """Defining a __repr__ function will enable us to print the
        queue contents, and facilitate debugging."""
        return repr(self.queue) # Good enough.

    def add(self, x):
        self.queue.append(x)

    def get(self):
        # This is the only difference compared to the stack above.
        return self.queue.pop(0) if len(self.queue) > 0 else None

    def isempty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)
    
    def __iter__(self):
        for el in self.queue:
            yield el
            
    def __getitem__(self, i):
        return self.queue[i]
    
    def __contains__(self, x):
        return x in self.queue
        
s = Queue()
print(s.get())
s.add('a')
s.add('b')
print(s.get())
print(s.get())
print(s.get())

class CountingQueue(object):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return repr(self.queue)

    def add(self, x, count=1):
        # If the element is the same as the last element, we simply
        # increment the count.  This assumes we can test equality of
        # elements.
        if len(self.queue) > 0:
            xx, cc = self.queue[-1]
            if xx == x:
                self.queue[-1] = (xx, cc + count)
            else:
                self.queue.append((x, count))
        else:
            self.queue = [(x, count)]

    def get(self):
        if len(self.queue) == 0:
            return None
        x, c = self.queue[0]
        if c == 1:
            self.queue.pop(0)
            return x
        else:
            self.queue[0] = (x, c - 1)
            return x

    def isempty(self):
        # Since the count of an element is never 0, we can just check
        # whether the queue is empty.
        return len(self.queue) == 0
    
q = CountingQueue()
q.add('a')
print(q)
q.add('b', count=5)
print(q)
q.add('c', count=2)
print(q)
while not q.isempty():
    print(q.get())
    print(q)
    
q = CountingQueue()
for i in range(10):
    q.add('a')
q.add('b')
for i in range(3):
    q.add('c', count=2)
print(q)

def counting_queue_peek(self):
    if len(self.queue) == 0:
        return None
    el, _ = self.queue[0]
    return el

CountingQueue.peek = counting_queue_peek

q = CountingQueue()
q.add("cat")
q.add("dog")
q.peek()

def counting_queue_len(self):
    ### YOUR CODE HERE
    count = 0;
    for q in self.queue:
      count += q[1]
    return count; 
CountingQueue.__len__ = counting_queue_len

# 5 points.  Simple tests

q = CountingQueue()
assert len(q) == 0
q.add("cat")
q.add("dog")
assert len(q) == 2

def counting_queue_iter(self):
    ### YOUR CODE HERE
    for i in self.queue:
        for _ in range(i[1]):
            yield i[0]
CountingQueue.__iter__ = counting_queue_iter

# 5 points.  Simple tests. 

q = CountingQueue()
q.add("cat", count=2)
q.add("dog", count=3)
assert [x for x in q] == ["cat"] * 2 + ["dog"] * 3

def counting_queue_in(self, el):
    ### YOUR CODE HERE
    for e in self.queue:
      if e[0] == el:
        return True
    return False 
CountingQueue.__in__ = counting_queue_in


q = CountingQueue()
assert "cat" not in q
q.add("cat", count=2)
assert "cat" in q
assert "dog" not in q
q.add("dog")
assert "cat" in q
assert "dog" in q
q.get()
assert "cat" in q
assert "dog" in q
q.get()
assert "cat" not in q
assert "dog" in q
q.get()
assert "cat" not in q
assert "dog" not in q

def counting_queue_getitem(self, n):
    ### YOUR CODE HERE
    if n >= len(self) or n < 0:
      raise IndexError

    ref = 0
    for e in self.queue:
      ref += e[1]
      if n < ref:
        return e[0]
    
CountingQueue.__getitem__ = counting_queue_getitem

# 5 points: simple tests. 

q = CountingQueue()
q.add("cat", count=2)
q.add("dog", count=3)
q.add("bird", count=4)
els = [q[i] for i in range(9)]

assert els == ['cat'] * 2 + ['dog'] * 3 + ['bird'] * 4
# Let's do it again. 
els = [q[i] for i in range(9)]
assert els == ['cat'] * 2 + ['dog'] * 3 + ['bird'] * 4

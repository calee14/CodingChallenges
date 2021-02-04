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


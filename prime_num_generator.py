def prime_number_generator():
    """This generator returns all prime numbers."""
    i = 2
    while True:
        prime = True
        for a in range(2, int(i**0.5)+1):
            if i % a == 0:
                prime = False
                break
        if prime == True:
          yield i    
        i+=1
        
for i in prime_number_generator():
  print(i)
  if i > 1000:
    break
    
print(range(2, int(4**0.5)+1))
for i in range(2, 2):
  print(i)

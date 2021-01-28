def subsets(s):
  if len(s) == 0:
    yield set()
  else:
    ss = set(s)
    x = ss.pop()
    # print('hello ' + str(ss))
    for t in subsets(ss):
      print('bye ' + str(ss))
      print('t' + str(t))
      print('x' + str(t | {x}))
      yield t
      yield t | {x}
      
      
for s in subsets([1, 3, 2]):
  # print(s)
  pass
  
def constant_sum_subsets(values, total):
  if len(values) == 0 and total == 0:
    yield set()
  if len(values) == 0:
    pass
  elif total >= 0:
    ss = set(values)
    x = ss.pop()
    for t in constant_sum_subsets(ss, total-x):
      if sum(t | {x}) == total:
        yield t | {x}
    for t in constant_sum_subsets(ss, total):
      if sum(t) == total:
        yield t

 for i in constant_sum_subsets([1, 2, 3, 4, 5], 6):
   print(i)
   
 ### Advanced test. 10 points. 

# This test fails if you are not smart about using the fact that values are all non-negatives. 
values = set(range(10000, 10100))
num = 0
for _ in constant_sum_subsets(values, 2000):
    num += 1
print(num) # 0

values = set(range(10000, 10100))
num = 0
for _ in constant_sum_subsets(values, 20020):
    num += 1
print(num) # 10

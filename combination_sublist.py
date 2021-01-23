def nondecsub(l, threshold=None):
  if len(l) == 0:
    return [[]]
  else:
    first = l[0] # the first element in list
    rest = l[1:] # the rest of the elements in list
    comb_wo_first = nondecsub(rest) # recursion: get all combinations without first index
    combs_w_first = [] 
    for comb in comb_wo_first:
      # print(first)
      comb_w_first = [first] + [c for c in comb] # add the first element to combs without first
      if sorted(comb_w_first) == comb_w_first:
        combs_w_first.append(comb_w_first)
  total_comb = combs_w_first + comb_wo_first # returns a 2d list
  return total_comb # add both combs with and without first element

def normalize(ll):
  s = set()
  for l in ll:
    s.add(tuple(l))
  return s

def n(l):
  return normalize(nondecsub(l, threshold=None))
 
nondecsub([-1, 0, 3, 4, 3, 5])

n([-1, 0, 3, 4, 3, 5]) == normalize([(3, 4, 5), (0, 4, 5), (-1, 0), (-1, 0, 3, 3, 5), (-1, 0, 3, 4), 
    (-1,), (-1, 5), (0, 3), (3, 3), (-1, 3, 3), (3,), (-1, 3, 4), 
    (3, 3, 5), (-1, 4, 5), (-1, 0, 3, 4, 5), (-1, 0, 3, 5), 
    (-1, 3, 3, 5), (-1, 3, 5), (0, 4), (5,), (-1, 0, 3, 3), 
    (-1, 0, 3), (0, 3, 3), (0, 3, 3, 5), (-1, 0, 4, 5), (4, 5), (-1, 0, 5), 
    (0, 5), (-1, 0, 4), (3, 5), (0,), (0, 3, 4), (-1, 3), (0, 3, 5), (4,), 
    (), (0, 3, 4, 5), (-1, 3, 4, 5), (-1, 4), (3, 4)])

first_walker = 0
second_walker = 102
walking = True

while walking:
  if first_walker != second_walker:
    print "Still walking! On mile {}".format(first_walker)
    first_walker += 2
    second_walker-= 1
  else:
    walking = False
print first_walker
print "Hello there fellow walker!"
    
    
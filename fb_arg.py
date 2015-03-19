import sys
length = len(sys.argv)
script = sys.argv[0]

if len(sys.argv) == 1:
  print "You supplied %d arguments at run time exclusively consisting of %s" % (length, script)
  user_n = int(raw_input("Please enter a max limit: "))
else:
  user_n = int(sys.argv[1])
  print "You supplied {} arguments at run time".format(len(sys.argv))
  
fizzbuzz = 0
count = True

while fizzbuzz <= user_n:
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print "Fizz Buzz"
    fizzbuzz += 1
  elif fizzbuzz % 3 == 0:
    print "Fizz"
    fizzbuzz += 1
  elif fizzbuzz % 5 == 0:
    print "Buzz"
    fizzbuzz += 1
  else:
    print fizzbuzz
    fizzbuzz += 1
    

    

    
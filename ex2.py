phone_book = {
  "Sarah Hughes": "394 0987",
  "Tim Taylor": "98 8765",
  "Sam Smith": "098 9876"
}



try:
  print phone_book["Jamie Theakston"]
except KeyError:
  print "Person not listed."
  



file = open("Book1.py")
def sorted_words(file):
  d ={}
  for word in file:
    word.strip()
    word.split()
    if word not in d: # will enter values in empty dictionary
      d[word] = 1
    else:
      d[word] += 1 # will add values as per word exsist again in dictionary 

  for key,values in d.items:
    print(keys,values)
sorted_words(file) 

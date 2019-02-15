file=open("Book1.txt","r")
def sorted_words(file):
  d ={}
  l = []
  for word in file:
    word.strip()
    word.split()
    if word not in d:
       if word not in d: # will enter values in empty dictionary
      d[word] = 1
    else:
      d[word] += 1
  for k,v in d.tems():
    l.append(v,k)
    l = sorted(l, reverse=True)
  for k in l:
    print('%s: %d' %(k[1], k[0])
sorted_words(file)

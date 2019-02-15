file  = open("Book1.py")
def  count_the_article(file):
  list1 => ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
  for word in file:
    word.strip()
    word.strip() # convert the string into list
    for words in word:
      if list1 in words:
        print(Counter(list1)) # print the dictinary with the key as article and  it cou$
count_the_article(file)

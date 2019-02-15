file = open("Book1.py")
def  starts_with_vow(file):
  for word in file:
    word.strip()
    word.split()
    print(*map(word.lower().count, "aeiou")) # it will count all the articles
starts_with_vow(file)


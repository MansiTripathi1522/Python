sentance="Today is my Python lab examination, Python is a high level language"
word="Python"
sentance=sentance.split(' ')
count=0
for i in sentance:
 if i==word :
     count+=1
print(count)

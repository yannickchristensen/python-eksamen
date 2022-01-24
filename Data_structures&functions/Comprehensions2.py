import re

with open("/Users/yannickchristensen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python Exam/Data_structures&functions/shakespeare.txt", "r") as f:
    shakespeare = f.read()

shakespeare = shakespeare.split()

#shakespeare = shakespeare.lower().split()

#shakespeare = re.sub(r'[^A-Za-z ]+', '', shakespeare).split()

#shakespeare = [word for word in re.sub(r'[^A-Za-z0-9 ]+', '', shakespeare).split() if word[0]=="y"]

#shakespeare = [word for word in re.sub(r'[^A-Za-z0-9 ]+', '', shakespeare).split() if word[0]=="y" and word not in ['you','yes','your','yours','yourself']]

#shakespeare = {word for word in re.sub(r'[^A-Za-z0-9 ]+', '', shakespeare).split() if word[0]=="y" and word not in ['you','yes','your','yours','yourself']}

#shakespeare = {word for word in re.sub(r'[^A-Za-z0-9 ]+', '', shakespeare).split() if word[0]=="y" and word not in ['you','yes','your','yours','yourself'] and len(word) > 9}

#shakespeare = {word[::-1] for word in re.sub(r'[^A-Za-z0-9 ]+', '', shakespeare).split() if word[0]=="y" and word not in ['you','yes','your','yours','yourself'] and len(word) > 9}



print(shakespeare)
print(len(shakespeare))


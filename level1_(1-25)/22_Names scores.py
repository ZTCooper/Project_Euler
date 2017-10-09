with open('22_names.txt') as f:
    names = f.read()
x = eval('['+names+']')     #trans into list
x.sort()

score = 0
i = 1
for name in x:
    score += sum([(ord(letter)-64) for letter in name])*i
    i += 1
print(score)

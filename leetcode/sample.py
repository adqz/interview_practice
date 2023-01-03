# 3. Debugging loops
names = ['David Wallace', 'Jim Halpert', 'Michael Scott', 'Dwight K. Schrute']
numSpaces = 0

for i in range(len(names)):
  name = names[i]
  for char in name:
    if char == ' ':
      numSpaces += 1
      names = []
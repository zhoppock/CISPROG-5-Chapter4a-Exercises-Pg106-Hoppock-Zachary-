print("Exercise 1")
data = "myprogram.exe"
print(" > String:", data)
#a
print(data[2])
#b
print(data[-1])
#c
print(len(data))
#d
print(data[0:8])

print("\nExercise 2")
data = "myprogram.exe"
print(" > String:", data)
#a
print(data[5:9])
#b
print(data[-4:])
#c
print(data[6])

print("\nExercise 3")
myString = "Open sesame"
print(" > String:", myString)
for index in range(len(myString)):
  print(10-index, myString[-1-index])

print("\nExercise 4")
myString = "Jake Gyllenhaal"
print(" > String:", myString)
reversedString = ""
for index in range(len(myString)):
  reversedString += myString[-1-index]
print("Reversed string:", reversedString)
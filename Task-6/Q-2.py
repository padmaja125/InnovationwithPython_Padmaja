students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dictc = {x:y for (x,y) in zip(students,subjects)}
print("Using Dict Comprehension",dictc)

# using for loop
res = {} 
for key in students: 
    for value in subjects: 
        res[key] = value 
        subjects.remove(value) 
        break 

print("Using For loop", res)

task_list = [
    'Design Database',
    'Set up Dev Environment',
    ['Implement Feature A', 'Write Unit Tests'],
    'Code Review',
    ['Deploy to Staging', 'Test Staging']
]

print(task_list)

# a: Make a shallow copy of the task list
dev_task_list = task_list.copy()

# b: Modify the shallow copy for development tasks
dev_task_list[1] = 'Set up Dev Environment (Complete)'
dev_task_list[2][1] = 'Write Unit Tests (In Progress)'

# c: Print both task lists
print("Original task list:", task_list)
#print("Development task list:", dev_task_list)

import copy

# Step 1: Make a deep copy of the task list
baseline_task_list = copy.deepcopy(task_list)

# Step 2: Modify the deep copy for the baseline project plan
baseline_task_list[4][0] = 'Deploy to Staging (Pending Review)'
baseline_task_list.append('Prepare Documentation')

# Step 3: Print both task lists
print("Original task list:", task_list)
print("Baseline task list:", baseline_task_list)



grades = [85, 92, 76, 81, 99, 67, 74, 88]
print(grades)

# Filter
good_grades = [grade for grade in grades if grade >= 80]
print("Good grades: ", good_grades)

# Transform
student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
student_names_upper_case = [name.upper() for name in student_names]
print("Student names in uppercase: ", student_names_upper_case)

# Mapping
letter_grades = [
    'A' if grade >= 80 else
    'B' if grade >= 70 else
    'C' if grade >= 60 else
    'D' if grade >= 50 else
    'F'
    for grade in grades
]
print(letter_grades)
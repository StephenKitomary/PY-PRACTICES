
task_list = [
    'Design Database',
    'Set up Dev Environment',
    ['Implement Feature A', 'Write Unit Tests'],
    'Code Review',
    ['Deploy to Staging', 'Test Staging']
]


#dev_task_list = task_list[:]
dev_task_list = task_list.copy()

dev_task_list[1]="Set up Dev Environment(Complete)"
print(task_list)
print(dev_task_list)




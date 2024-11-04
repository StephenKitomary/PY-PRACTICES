
task_list = [
    'Design Database',
    'Set up Dev Environment',
    ['Implement Feature A', 'Write Unit Tests'],
    'Code Review',
    ['Deploy to Staging', 'Test Staging']
]


dev_task_list = task_list[:]


dev_task_list[1]="Set up Dev Environment(Complete)"
dev_task_list[2][1] = 'Write Unit Tests (In Progress)'
dev_task_list[4][1] = 'DEPLOY TO STAGING (CHNAGED)'
print(task_list)
print(dev_task_list)



# delete all the digits in text
task_4_text = input('Enter your text: ')
task_4_result = ''
for i in task_4_text:
    task_4_result += '' if i.isdigit() else i
print(task_4_result)

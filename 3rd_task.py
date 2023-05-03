# task 3: change first 3 characters in string if starts with 'abc'
# else: add 'qqq' in the end of string
task_3_text = input('Enter your text: ')
first_3_characters = task_3_text[0:3]
if first_3_characters == 'abc':
    print(task_3_text.replace(first_3_characters, 'www', 1))
else:
    print(task_3_text + 'qqq')

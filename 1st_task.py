# task 1: is word a palindrome
task_1_word = input('Enter your word: ')
reverse_word = task_1_word[::-1]
print('+' if task_1_word == reverse_word else '-')

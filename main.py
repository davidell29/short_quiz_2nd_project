print('----')
print("What's the tallest building in the world?")
print('----')
print("A. Burj Khalifa\nB. Trump's Tower\nC. Palatul Parlamentului")
print('----')


while True:
    user = input('Please choose one of the options above: ').strip().upper()

    if user in ['A']:
        final_answer = user
        break
    elif user in ['B', 'C']:
        print("Wrong answer, bratan. Please try again.")
    else:
        print('Invalid input. Please type A, B or C.')

print('----')
print(f'Great! You chose option {final_answer}.')
print('----')
print('----')
print("Which planet in our solar system has the highest average surface temperature?")
print('----')
print("D. Mercury\nE. Venus\nF. Mars")
print('----')

while True:
    user_two = input(
        'Please choose one of the options above: ').strip().upper()

    if user_two in ['E']:
        final_answer_two = user_two
        break
    elif user_two in ['D', 'F']:
        print("Wrong answer, bratan. Please try again.")
    else:
        print('Invalid input. Please type D, E or F.')

print('----')
print(f'Great! You chose option {final_answer_two}')
print('----')
print('----')

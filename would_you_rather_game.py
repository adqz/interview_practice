import random

def get_question(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    lines_clean = []
    for line in lines:
        try:
            temp = line.split('.')[1].strip()
            lines_clean.append(temp)
        except:
            break

    print('Welcome to "Would you rather"!')
    numbers = range(100)
    while True:
        user_input = input('Enter y for question, anything else to stop: ')
        if user_input.strip().lower() == 'y':
            i = random.sample(numbers, 1)[0]
            print(i)
            print(lines_clean[i])
        else:
            break


if __name__ == "__main__":
    get_question('./game_questions.txt')
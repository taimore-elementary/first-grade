import re
import difflib
from PIL import Image
from pytesseract import image_to_string

# helpers
def cleanup(input_str):
    subbed_input = re.sub('[(){}\|/\]]', ' ', input_str)
    split_input = subbed_input.splitlines()
    cleaned_input = ''
    for line in split_input:
        if(len(line) > 1):
            cleaned_input += re.sub(' +', ' ', line)
            cleaned_input += '\n'
    return cleaned_input

# input pictures of answers & empty
answers = Image.open('images/answers.png', mode='r')
answers_as_string = image_to_string(answers)
cleaned_answers = cleanup(answers_as_string)
print(cleaned_answers)

empty = Image.open('images/empty.png', mode='r')
empty_as_string = image_to_string(empty)
cleaned_empty = cleanup(empty_as_string)
print(cleaned_empty)

# write answers & empty to .txt files
answers_file = open("program-results/program-answers.txt", "w")
answers_file.write(cleaned_answers)
answers_file.close()

empty_file = open("program-results/program-empty.txt", "w")
empty_file.write(cleaned_empty)
empty_file.close()

# diff answers & empty to get num questions & question weight
print('diff')
final_file = open("output/output.txt", "w")

answers_file = open("program-results/program-answers.txt", "r")
empty_file = open("program-results/program-empty.txt", "r")
num_questions_per_assignment = 0

for line1 in answers_file:
    for line2 in empty_file:
        if line1 == line2:
            # Do nothing!
            print
        else:
            print("answer should be: " + line1)
            answers_list = line1.split()
            print("empty says: " + line2)
            empty_list = line2.split()
            num_questions_per_line = len(answers_list) - len(empty_list)
            print('there are ' + str(num_questions_per_line) + ' parts to this question')
            num_questions_per_assignment += num_questions_per_line
        break

answers_file.close()
empty_file.close()
print 
print('total number of questions: ' + str(num_questions_per_assignment))
print('each question is worth ' + str(100/num_questions_per_assignment) + ' points')

# for all submitted assignments, diff vs answers and determine score
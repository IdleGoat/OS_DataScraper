from bs4 import BeautifulSoup
import os

# Define the directory containing the HTML files to be scraped
directory = 'scrape/'
# Create a new text file to save the output
output_file = open('OS.txt', 'w')

question_counter = 1

printed_questions = set()

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)

        # Load the HTML file using requests library
        with open(filepath, "r") as f:
            html_text = f.read()
        soup = BeautifulSoup(html_text, 'html.parser')

        # Extract all question divs
        question_divs = soup.find_all('div', {'class': 'que'})

        # Loop through each question div
        for question_div in question_divs:
            # Extract the question text
            question = question_div.find('div', {'class': 'qtext'}).text.strip()
            # Extract the answer options
            if question in printed_questions:
                continue
            printed_questions.add(question)
            answer_options_div = question_div.find('div', {'class': 'ablock'})
            answer_options = answer_options_div.find_all('div', {'class': ['r0', 'r1']})
            answer_options_text = [option.text.strip()[3:] for option in answer_options]
            # Extract the correct answer
            correct_answer_div = question_div.find('div', {'class': 'rightanswer'})
            correct_answer = correct_answer_div.text.strip()[22:] if correct_answer_div else 'Unknown'
            # Print the extracted information
            print("Question:", question)
            print("Answer options:", answer_options_text)
            print("Correct answer:", correct_answer)
            print("------")
            # Write the extracted information to the output file
            output_file.write('{}. Question : {}\n'.format(question_counter, question))
            for i, option in enumerate(answer_options_text):
                output_file.write('Option {}: {}\n'.format(i + 1, option))
            output_file.write('Answer: {}\n\n'.format(correct_answer))
            # Increment the question counter
            question_counter += 1

output_file.close()
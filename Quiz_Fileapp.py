"""
This is a quiz system that will:

task description:
- read from `Quiz_questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it
    to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum questions respectively
"""

questions = open('Quiz_questions.txt', 'r')
q_list = [q.strip() for q in questions.readlines()]
questions.close()
user_score = 0
for each_q in q_list:
    qstn, ans = each_q.split('=')
    user_ans = input(f'{qstn} = ')
    if user_ans == ans:
        user_score += 1

results = open('Quiz_results.txt','w')
results.write(f'Your final score is {user_score}/{len(q_list)}.')
results.close()
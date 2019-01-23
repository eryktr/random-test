from consts import constants
from dbservice import DBService
from exceptions import NotEnoughClosedQuestionsError, NotEnoughOpenQuestionsError


def delete_command(dbservice: DBService):
    content = input("Content of the question to be deleted: ")
    dbservice.delete_question(content)


def add_open_question_command(dbservice: DBService):
    content = input("Question content: ")
    question = {
        constants['CONTENT_KEY']: content,
        constants['TYPE_KEY']: constants['OPEN_QUESTION_KEY']
    }
    dbservice.insert(question)


def add_closed_question_command(dbservice: DBService):
    content = input("Question content: ")
    num_of_answers = int(input("Number of answers: "))
    answers = []
    for i in range(0, num_of_answers):
        answer = input("answer: ")
        answers.append(answer)
    question = {
        constants['CONTENT_KEY']: content,
        constants['TYPE_KEY']: constants['CLOSED_QUESTION_KEY'],
        constants['ANSWERS_KET']: answers
    }
    dbservice.insert(question)


def illegal_choice_command():
    print("Illegal choice.")


def exit_command():
    print("Goodbye!")
    exit(0)


def add_question_command(dbservice : DBService):
    print("What kind of question would you like to add?")
    print("[1] - Open Question")
    print("[2] - Closed Question")
    choice = input("Choice: ")
    if choice == '1':
        add_open_question_command(dbservice)

    elif choice == '2':
        add_closed_question_command(dbservice)

    else:
        illegal_choice_command()


def create_random_test_command(dbservice : DBService):
    open_questions = dbservice.get_open_questions()
    closed_questions = dbservice.get_closed_questions()
    num_open_questions = int(input("Number of open questions: "))
    num_closed_questions = int(input("Number of closed questions: "))
    if num_open_questions > len(open_questions) : raise NotEnoughOpenQuestionsError
    if num_closed_questions > len(closed_questions) : raise NotEnoughClosedQuestionsError

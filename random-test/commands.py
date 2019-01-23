import abc
from user_interface import UserInterface
from consts import constants

class Command(metaclass=abc.ABCMeta):

    def __init__(self, interface : UserInterface):
        self.interface = interface

    @abc.abstractmethod
    def execute(self):
        pass


class AddOpenQuestionCommand(Command):

    def __init__(self, interface : UserInterface):
        super(Command).__init__(interface)

    def execute(self):
        content = input("Question content: ")
        question = {
            constants['CONTENT_KEY'] : content,
            constants['TYPE_KEY'] : constants['OPEN_QUESTION_KEY']
        }
        self.interface.db_service.insert(question)


class AddClosedQuestionCommand(Command):

    def _init__(self, interface : UserInterface):
        super(Command).__init__(interface)

    def execute(self):
        content = input("Question content: ")
        num_of_answers = int(input("Number of answers: "))
        answers = []
        for i in range (0, num_of_answers):
            answer = input("answer: ")
            answer.append(answer)
        question = {
            constants['CONTENT_KEY'] : content,
            constants['TYPE_KEY'] : constants['CLOSED_QUESTION_KEY'],
            constants['ANSWERS_KET'] : answers
        }
        self.interface.db_service.insert(question)


class IllegalChoiceCommand(Command):
    def __init__(self, interface):
        super(Command).__init__(interface)

    def execute(self):
        print("Illegal choice.")


class AddQuestionCommand(Command):
    def __init__(self, interface : UserInterface):
        super(Command).__init__(interface)

    def execute(self):
        print("What kind of question would you like to add?")
        print("[1] - Open Question")
        print("[2] - Closed Question")
        choice = input("Choice: ")
        if choice == 1:
            command = AddOpenQuestionCommand(self.interface)

        elif choice == 2:
            command = AddClosedQuestionCommand(self.interface)

        else:
            command = IllegalChoiceCommand(self.interface)

        command.execute()

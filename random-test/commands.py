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

    def _init__(selfself, interface : UserInterface):
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


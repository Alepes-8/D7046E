import random


class Questions:
    qs = []
    path_to_questions = ""

    def __init__(self, path_to_questions):
        self.path_to_questions = path_to_questions
        self.__init_qs()

    def __init_qs(self):
        file = open(self.path_to_questions, 'r')
        for line in file.readlines():
            self.qs.append(line.rstrip('\n'))

    def random(self) -> str:  # random questions
        return random.choice(self.qs)

    def random_rm(self) -> str:  # random questions and remove it from possible questions
        if len(self.qs) == 0:
            self.__init_qs()

        q = random.choice(self.qs)
        self.qs.remove(q)
        return q

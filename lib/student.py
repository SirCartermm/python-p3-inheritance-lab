class Student(User):
    def _init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge =[]

    def learn(self, knowledge):
        self.knowlegde.append(knowledge)
        
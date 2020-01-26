class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        res = sum(self.scores)//len(scores)
        if res in range(90, 101):
            return 'O'
        elif res in range(80, 90):
            return 'E'
        elif res in range(70, 80):
            return 'A'
        elif res in range(55, 70):
            return 'P'
        elif res in range(40, 50):
            return 'D'
        else:
            return 'T'
                
line = input().split()

emp_name = [
    "Jim",
    "Deepanshu",
    "Aditya" ,
    "Micheal",
    "Deep",
    "Abhinav"
]

class Student :
    def __init__(self, name, major, gpa): # initial fn which define what entity should be
        self.name = name
        self.major = major
        self.gpa = gpa


class Questn:
    def __init__(self, prompt, ans):
        self.prompt = prompt
        self.ans = ans
        

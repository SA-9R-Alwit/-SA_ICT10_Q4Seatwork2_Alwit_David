from pyscript import display, document


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! My name is {self.name}  and I'm from {self.section} and my favorite subject is {self.favorite_subject}!"


# classmates
classmates = [
    Classmate("David", "Emerald", "Math"),
    Classmate("Lewis", "Emerald", "Math"),
    Classmate("Matt Sky", "Emerald", "Science"),
    Classmate("Sir Nixon Sumaoang", "Emerald", "Filipino"),
    Classmate("BDD", "Emerald", "Science")
]

# add classmates
def add_classmate(e):
    name = document.getElementById("classmate1").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    new_student = Classmate(name, section, subject)
    classmates.append(new_student)

    display(f"{name} added successfully!\n", append=True, target='output')


# show classmates
def show_classmates(e):
    document.getElementById('output').innerHTML = " "

    for student in classmates:
        intro = student.introduce()
        display(intro + "\n", target='output')
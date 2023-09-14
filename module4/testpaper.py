class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, testpaper, answers):
        score = sum(1 for student_ans, correct_ans in zip(answers, testpaper.markscheme) if student_ans == correct_ans)
        percentage = (score / len(testpaper.markscheme)) * 100
        result = "Passed" if percentage >= float(testpaper.pass_mark[:-1]) else "Failed"

        if self.tests_taken == "No tests taken":
            self.tests_taken = {testpaper.subject: f"{result}! ({round(percentage)}%)"}
        else:
            self.tests_taken[testpaper.subject] = f"{result}! ({round(percentage)}%)"


# Creating test papers
paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

# Creating students
student1 = Student()
student2 = Student()

# Taking tests
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])

# Checking test results
print(student1.tests_taken)  # Output: {"Maths": "Passed! (80%)"}
print(student2.tests_taken)  # Output: {"Chemistry": "Failed! (25%)", "Computing": "Failed! (43%)"}






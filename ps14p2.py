class Student:
    def __init__(self, first, last, district_code, enrolled_credits):
        self.first = first
        self.last = last
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == 'I':
            tuition_rate = 250.00
        else:
            tuition_rate = 500.00
        tuition_owed = self.enrolled_credits * tuition_rate
        return tuition_owed

student1 = Student('Konnor', 'Del Mar', 'I', 6)
student2 = Student('Michael', 'Jackson', 'O', 13)

tuition1 = student1.compute_tuition()
tuition2 = student2.compute_tuition()

print(f"{student1.first} {student1.last} (District: {student1.district_code}): Tuition Owed: ${tuition1}")
print(f"{student2.first} {student2.last} (District: {student2.district_code}): Tuition Owed: ${tuition2}")
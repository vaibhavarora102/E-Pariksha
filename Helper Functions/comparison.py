teacher = "answer by teacher"

student = "answer by student"

def arrayGiver(data):
    text = data.split()
    text = set(text)
    num = len(text)
    return text, num

# print(arrayGiver(teacher))

def compare(teacher, student):
    teacher_arr, teacher_length = arrayGiver(teacher)
    student_arr, student_length = arrayGiver(student)
    score = 0
    for word in teacher_arr:
        if word in student_arr:
            score+=1

    percent = (score/teacher_length)*100
    return percent

print(compare(teacher,student))

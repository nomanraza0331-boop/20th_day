

def read_student_data(n):
    student=[]
    for i in range(n):
        student.append(input("enter student name: "))
    return student

def calculate_expances(n):
    expances=[]
    for i in range(n):
        p,q=map(int,input("enter price and qyt").split())
        expances.append(p*q)
    return expances

def greetings():
    print("welcome to the class")
    
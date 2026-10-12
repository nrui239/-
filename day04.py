students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 67},
    {"name": "小李", "score": 76}
]
def get_best_student(students):#students[0]是第一个字典   再用字典的键对应值
    score_max=students[0]["score"]
    best_student=students[0]
    for student in students:#这里的student是字典
        if student["score"]>=score_max:
            score_max=student["score"]#求出最高分  怎么返回学生?
            best_student=student
    return best_student         
best = get_best_student(students)
print(best)

def get_average_score(students):
    num=0
    for student in students:
        num+=student["score"]
    return num/len(students) 

def show_report(students):
    student=get_best_student(students)
    avg_score=get_average_score(students)
    print(f'最高分学生：{student["name"]}\n最高分：{student["score"]}')
    print(f"平均分：{avg_score}")
    
show_report(students)
print (len(students))


    

def get_max(numbers):
    max=numbers[0]
    for number in numbers :
        if number>=max:
            max=number
    return max
def show_result(numbers):
    print(f"最大值是：{get_max(numbers)}")

numbers = [23, 67, 12, 89, 45]
show_result(numbers)

            
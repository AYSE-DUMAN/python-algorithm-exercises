def gradingStudents(grades):
    
    grades_list = []

    for i in grades:
        
        dif = 5 - (i % 5) 
        
        if i < 38 or dif >= 3:
            grades_list.append(i)
        else:
            grades_list.append(i + dif)

    return grades_list            

if __name__ == '__main__':
    

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

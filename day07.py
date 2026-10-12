numbers1 = [10, 20, 30, 40]
numbers2 = []


def get_average(numbers):
    num=0
    for number in numbers:
        num=num+number
    try:    
        avg=num/len(numbers)
    except  ZeroDivisionError:
        return("没有有效数字")
    else:
        return avg

    

def get_max(numbers):
    try:
        maxnumber=numbers[0]
    except:
        return("没有有效数字")  
    else:    
        for number in numbers:
            if number>=maxnumber:
                maxnumber=number
        return maxnumber   
print(get_average(numbers1))
print(get_average(numbers2))

print(get_max(numbers1))
print(get_max(numbers2))    
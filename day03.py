def add(a,b):
    return(a+b)
print(add(2,5))
def is_even(num):
    if num%2==0:
        return True
    else :
        return False
print(is_even(10))
print(is_even(7))    
def get_max(numbers):
    max=numbers[0]
    for a in numbers:
        if(a>=max):
            max=a
    return max
numbers1=[-3, -8, -2, -15, -6]
print(get_max(numbers1))        
def check_password(password):
    if len(password)<6:
        return("密码太短")
    else:
        return("密码正常")
print(check_password("123"))
print(check_password("123456")) 
        
        
    
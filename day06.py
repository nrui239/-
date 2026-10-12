# def get_number():
#     while True:#无限循环  等到return跳出循环
#         try:
#             number=int(input("请输入数字："))#int()转换成整数
#         except ValueError:#不是整数报错  执行
#             print("请输入数字！")
#         else:#正确执行
#             return number
# num=get_number()
# print("你输入的是:",num)


def read_number_file(filename):
    numbers_list=[]
    with open(filename,"r") as file:
        lines_list=file.readlines()#返回列表
    for line in lines_list:
        try:
            number=int(line)#尝试转换成整数
        except ValueError:
            pass#跳过这一行
        else:
            numbers_list.append(number)
    return numbers_list

def get_average(numbers):
    num=0
    for number in numbers:
        num=num+number
    avg=num/len(numbers)
    return avg

def get_max(numbers):
    maxnumber=numbers[0]
    for number in numbers:
        if number>=maxnumber:
            maxnumber=number
    return maxnumber   
 
numbers = read_number_file(r"C:\Users\Rui74\Desktop\numbers.txt")
#做一个菜单   组织程序结构
while True:#input返回字符串
    a=input("===== 数字文件分析器 =====\n1. 显示所有有效数字\n2. 计算平均值\n3. 查找最大值\n4. 退出\n请选择：")
    if a=="4":
        break
    elif a=="1":
        print("有效数字：", numbers)
    elif a=="2":
        print("平均值：", get_average(numbers))
    elif a=="3":
        print("最大值：", get_max(numbers)) 
    else:
        print("输入错误，请重新输入")  








# print("有效数字：", numbers)
# print("平均值：", get_average(numbers))
# print("最大值：", get_max(numbers))     


        


            

# file=open(r"C:\Users\Rui74\Desktop\article.txt","r")
# content=file.read()
with open(r"C:\Users\Rui74\Desktop\article.txt","r") as file: #使用with不需要手动关闭文件
    lines=file.readlines()#读取所有的行
counts={}  

keywords=input("请输入关键词，用空格分隔：")#返回字符串
keywords_list=keywords.split(" ")#分隔出单个单词，返回列表
# words=content.split()#以任意个空格、换行符分割字符串
# print(f"字符数量：{len(content)}")
# print(f"单词数量：{len(words)}")
# print(f'Python出现次数：{content.count("Python")}')
# file.close()
for line in lines:
    for keyword in keywords_list:
        if keyword in line:
            counts[keyword]=counts.get(keyword,0)+1

            
for key in counts:
    print(f"{key}行数:{counts[key]}")



   

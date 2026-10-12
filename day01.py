import os  
path=input("请输入文件夹路径：")
total=0
if not os.path.exists(path):
    print("路径不存在")
else:    
    names=os.listdir(path)
    ext_count={}
    
    for name in names:
        file=os.path.join(path,name)
        if os.path.isfile(file):
            base, ext = os.path.splitext(name)
            total+=1
            if ext in  ext_count:
                ext_count[ext]= ext_count[ext]+1
            else:
                ext_count[ext]=1    
# 排序（降序）
    sorted_items=sorted(ext_count.items(),key=lambda x:x[1],reverse=True) 


    print("统计结果:")
    for a,b in sorted_items:
        print(f"{a} : {b}") 
    print(f"总文件数：{total}")    

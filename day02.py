files = [
    "test.py",
    "main.py",
    "hello.c",
    "data.txt",
    "run.py",
    "index.html",
    "style.css",
    "test.c",
    "readme.md",
    "server.py"
]

def get_python_files(files):
    python=[]
    for file in files:
        name=file.split(".")#返回的是列表
        newname="."+name[-1]#倒数第一个元素
        if newname==".py":
            python.append(file)
    return python      
print(get_python_files(files) )     
        

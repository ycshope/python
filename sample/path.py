from pathlib import Path

#定义一个目录
path = Path("hellow")
if  path.exists():
    print("dir exists")
    path.rmdir()
else:
    path.mkdir()
    
#遍历当前文件中的.py
path = Path()
print(path.glob("*.py"))    #返回的是一个迭代器
for file in path.glob("*.py"):
    print(file)
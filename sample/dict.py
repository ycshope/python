'''字典类似C++的map
    key必须为str类型,value没有关系
'''
My_Dict = {
    "name": "kali",
    "age": 19,
    "is_student": True,
    "family": ["mon", "dad"]
}
print(type(My_Dict))  #<class 'dict'>
print(
    My_Dict
)  #{'name': 'kali', 'age': 19, 'is_student': True, 'family': ['mon', 'dad']}

#等价写法
print(My_Dict["name"])
print(My_Dict.get("age"))

#keys方法可以遍历
print(My_Dict.keys())  #dict_keys(['name', 'age', 'is_student', 'family'])
print(type(My_Dict.keys()))  #<class 'dict_keys'>
My_List = [key for key in My_Dict.keys()]
print(My_List)  #['name', 'age', 'is_student', 'family']  取出所有key

#items可以生成dict的(key,value)元组对
print("+" * 50)
print("items方法可以取出所有的key,vlaue")
print(
    My_Dict.items()
)  #dict_items([('name', 'kali'), ('age', 19), ('is_student', True), ('family', ['mon', 'dad'])])
print(type(My_Dict.items()))  #<class 'dict_items'>

#取出所有的value
print("-" * 50)
print("取出所有的value")
print([t[1] for t in My_Dict.items()])  #t[0]是key,t[1]是value

#更新的两种方法
print("-" * 50)
print("更新的两种方法")
My_Dict["age"] = 20
print("方法1:[]")
print(My_Dict.items())
print("方法2,update.(原则是有就覆盖,没有就新增)")  #也有用于初始化
My_Dict.update({"age": 21, "university": "HIT"})
print(My_Dict.items())

#key的类型
MyNewDict = {1: "int", ("1", 2): "tupe"}  #键只能由数字、字符串、元组等不可变对象组成，不能用列表
print(MyNewDict)

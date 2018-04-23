'''
基本语法
'''
# def area(w,h):
#     return w*h

# print(area(5,4))



'''
需求：函数内部修改全局变量
global 关键字
'''
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num) 
#     num = 123
#     print(num)
# fun1()



'''
如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
'''
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()
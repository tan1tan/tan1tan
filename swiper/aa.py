def outer():
     x = 1
     def inner():
         global x
         print("--------",x)  # 1
     return inner
foo = outer()
print(foo)


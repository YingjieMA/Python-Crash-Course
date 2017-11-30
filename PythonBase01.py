#运算符
arr1 = [1,2,3,4,5]
arr2 = [0,1,2,3]
if 0 in arr1:
    print("yes")
elif 2 in arr1:
    print("in arr2")
else:
    print("none")
#循环，开区间？
for i in range(0,10):
    print(i)
#常量函数
def print_default(s="hello"):
    print (s)
print_default()
print_default("default")
#list中插入data
arr1.insert(2,2.5)
print(arr1)
#类
class Human:
    gender = "male"

class Man(Human):
    def __init__(self,name):
        self.name = name
    def walk(self):
         print(self.name + " is walking")
    pass

human1 = Man("Ben")
print(Man.gender)
print(human1.name)
human1.walk()

# ex1
my_list = ['orange','banana','apple','kiwi']
index = int(input("please enter the index you want"))
if index >= len(my_list):
    print("out of range please choose another index")
    index = int(input("please enter the index you want"))
else:
     my_list.insert(index,"pineapple")
     print(my_list)


# ex2
my_list = []
obj = input("please enter the object you want")
while obj != "stop":
    my_list.append(obj)
    obj = input("please enter the object you want")
print(my_list)

# ex3
count = 0
my_list = ["o","hat","aba","1221","umbrella","pickup","22.3.22"]
for obj in my_list:
    if len(obj) > 1 and obj[0]== obj[len(obj)-1]:
        count +=1
print(count)


# ex4
my_list = [3,5,45,97,32,22,10,19,39,43]
new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x)
print(new_list)


# ex5
import random
my_list = [5,4,8,1]
new_list = []
for obj in my_list:
    index = random.randint(0,len(my_list)-1)
    new_list.insert(index,obj)
print(new_list)

# ex6
my_dict = {"noam":18,"talya": 17, "shir": 16}
print (my_dict)
my_dict["joey"] = 19
print(my_dict["joey"])
print(len(my_dict))
print(my_dict.keys())
my_dict.pop("joey")
print(my_dict)
print("jack in my_dict:",my_dict.get("jack"))
avg = sum(my_dict.values()) / len(my_dict.values())
print(avg)
for num in my_dict:
    if my_dict[num]>18:
        print(num)
my_dict.clear()
print(my_dict)




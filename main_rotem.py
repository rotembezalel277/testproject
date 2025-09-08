import sys
import random
max_num = 0
name_max = ""
name_list = []
list_votes = []
count_list =[]
num = int(input("how many candidates are there"))
if num < 4 or num > 15:
    print("you need to have at least 4 candidate and no more than 15 ")
    sys.exit()
for i in range(1,num+1 ):
    name = input(f'what is the name of candidate {i}' )
    name_list.append(name)
votes = int(input("how many votes are they"))
if votes < 100:
    print("must be at least 100 votes")
    sys.exit()
list_votes = random.choices(name_list, k = votes)
for item in name_list:
        count_of_votes = list_votes.count(item)
        count_list.append(count_of_votes)
        if count_of_votes > max_num:
            max_num = count_of_votes
            name_max = item
print(f'the winner is: {name_max} {max_num}')
for item in list_votes:
        if item ==  name_max:
            list_votes.remove(item)
max_num = 0
name_max = ""
for i in range(len(name_list)-1):
    for item in name_list:
        count_of_votes = list_votes.count(item)
        count_list.append(count_of_votes)
        if count_of_votes > max_num:
            max_num = count_of_votes
            name_max = item
    print(name_max,max_num)
    for item in list_votes:
        if item == name_max:
            list_votes.remove(item)
    max_num = 0
    name_max = ""







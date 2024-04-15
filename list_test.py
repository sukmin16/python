'''
a = [1,2,3,4,5]
print(a)

l = []

singer_list = ["뉴진스", "트와이스"]
print(type(singer_list))
print(singer_list[0])
singer_list.append("아이유")
print(singer_list)
print(singer_list)
singer_list.insert(1,"르세라핌")
print(singer_list)
singer_list.insert(2,"차은우")
print(singer_list)
print(singer_list[1:3])
'''
'''
sports = ["야구", "축구", "농구"]
print("농구" in sports)
print("배구" in sports)
sports.remove("축구")
print(sports)
print(len(sports))
sports[0]="배드민턴"
print(sports)


sports = ["야구", "축구", "농구"]
sports.remove("축구")
sports.append("족구")
print(sports)

del sports[0]
print(sports)
sports.pop()
print(sports)
sports.append("족구")
sports.append("축구")
sports.append("배구")
print(sports)

sports.clear()
print(sports)
'''



fruit=["apple", "banana", "mango"]
food=["떡볶이", "치킨", "피자"]

fruit.append("strawberry")
food.append("족발")
fruit.remove("apple")
food.remove("치킨")
fruit.insert(1, "melon")
print(food)
print(fruit)
fruit.extend(food)
print(food)
print(fruit)

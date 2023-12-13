# # 1
# def example_one():
#     for counter in range(11):
#         print(counter)
# example_one ()

#2
# def example_two():
#     for counter in range (2, 12, +2):
#      print(counter)
# example_two ()

#3
# def example_three():
#     sum = 0
#     for i in range (1, 9, +2):
#         sum += i
#     print(sum)
# example_three()

#4
# def example_four():
#     for counter in range (10, 0, -1):
#         print(counter)
# example_four ()

#5
# def example_five():
#     for i in range (4,21,4):
#         print (i)
# example_five()

#6
# def example_six():
#     product = 1
#     for i in range(1, 6):
#         product*=i
#         print(product)
# example_six()

#7
# def example_seven():
#     for i in range (3, 13):
#         if i % 3 ==0:
#             print(i) 
# example_seven()

#8
# def example_eight():
#     for i in range (5,0,-1):
#         print(i)
#     print("Blast off!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# example_eight ()

#9
# def example_nine():
#     for i in range (1,6):
#         print(i*i)
# example_nine()

#10 
# def factorial(n):
#     for n in range (1,8):
#         product = 1
#     for i in range (n,0,-1):
#         product *= i
#         return product

# for n in range (1,8):
#     print(factorial(n))

#11
# str = "WONDERFUL"
# result = " "
# for i in range (1,len(str),2):
#     result += str[i]
# print(result)

#13
# str = "Computer".lower()
# count = 0
# for index in range (len(str)):
#     if str[index] in ('a', 'e', 'i', 'o', 'u'):
#         count +=1
# print(count)

#14
# str = "RACECAR"
# result = ""
# for i in range(len(str)-1, -1, -1):
#         result += str[i]
#         if result == str:
#             print("racecar is a palindrone")
#         else:
#             print("it is not a palindrone")
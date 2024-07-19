print(list(w:=input())==sorted(w))

# word = input()
# print(True if word == "".join(sorted(word)) else False)

# print(list(a := input()) == sorted(a))
# print(True if list(a := input()) == sorted(a) else False)

# word = input()
# print(word == "".join(sorted(word)))

# print(True if (word := input()) == "".join(sorted(word)) else False)
# print((word := input()) == "".join(sorted(word)))
# print((w:=input())=="".join(sorted(w)))
# print((a:=input()) == sorted(a))
# print((a:=list(input()))==sorted(a))
# print(list(a := input()) == sorted(a))
# print(sorted(a := input() )== list(a))

# def square_digits(num):
#   num = [int(x) for x in str(num)]
#   num = [x**2 for x in num]
#   return (int(''.join([str(x) for x in num])))
# print(square_digits("1234"))

# https://www.codewars.com/kata/514b92a657cdc65150000006
# def solution(number):return sum([n for n in range(1,number) if n%3==0 or n%5==0])
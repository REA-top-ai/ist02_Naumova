def factorial(num):
    res = 1
    for i in range(1, num+1):
        res*=i
    return res

print(factorial(6))

def factorial_recertion(num):
    if num == 1:
        return 1
    return num*factorial_recertion(num-1)

print(factorial_recertion(6))

nums = [1, 2, 3, 4, 5]

def square(nums):
    res = []
    for num in nums:
        res.append(num**2)
    return res

print(square(nums))
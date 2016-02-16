#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(obj):
    objStr = str(obj)
    reverse = objStr[::-1]

    return objStr == reverse

largestProduct = 0

for x in range(100, 999):
    for y in range(100,999):
        product = x*y

        if(isPalindrome(product)):
            largestProduct = max(largestProduct, product)

print(largestProduct)
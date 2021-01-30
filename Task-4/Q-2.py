def casefind(n):
    return "lowercase :" ,sum(map(str.islower, n)),"uppercase :" ,sum(map(str.isupper, n))


a = "abcSdefPghijQkl"
print(casefind(a))
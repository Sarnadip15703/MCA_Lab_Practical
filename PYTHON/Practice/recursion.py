# def fact(n):
#     if n==0:
#       return 1
#     else:
#        return fact (n-1)*n
# n=fact(4)
# print(n)

# def fun(n):
#     if n>1:
#       fun(n-1)
#     print (n)
# fun(4)

def gcd(m,n):
    if m>n:
      if m%n == 0:
         gcd(m,n)
    elif m%n == 0:
        return n
    else:
        gcd(n,m%n)
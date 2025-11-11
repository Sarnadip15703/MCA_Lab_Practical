print("Sarnadip", file=open("myfile.txt","w"))
print("%d %d" % (5, 6))
print("a=%d b=%o c=%0x" % (15, 25, 35))   # o for octal and 0x for hexadecimal
print("a={0} b={1} c={2}".format(5, 6, 8))   # {} are placeholders
s=4
print(s<<2)
print(bin(s))
print(bin(s<<2))
print(bin(s>>2))
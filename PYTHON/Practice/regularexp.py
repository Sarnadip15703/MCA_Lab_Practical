import re
str1="this is 09 first line for the first code "
b="my phone number is 9002174248"
d="mca mba bbbb abbbb bbhgfvb hihjbbh bbbbbb"
match=re.findall("f",str1)
match=re.findall("[b-f]",str1)
match=re.findall("b{2,4}",d)
match=re.findall("b+",d)
print(match)

# import re
# st1="this is 09 first line far of fat code"
# b="my phone number is 8927901178"
# c="My DOB is 05/09/2005"
# d="mca 887 mba mcamca bbb bcbbbbb bbcbbb mba bcabba mcaa"
# e="my email id is nsaha8967@gmail.com"
# #match=re.findall("f",st1)
# #match=re.findall("[b-f]",st1)
# #match=re.findall("b{2,4}",d)  #2,4 also write
# match=re.findall("b+",d)
# print (match)

# #  match=re.search("first",st1)
# #match=re.search("99",b) #b=phone number 99999...
# #match=re.search("[8-9]",st1)
# #match=re.search(".",e)
# #match=re.search("\.",e)
# #match=re.search("^m",e)  #match=re.search("$m",e)
# match=re.search("com$",e)
# match=re.search("[0-9]+",c)
# print (match)
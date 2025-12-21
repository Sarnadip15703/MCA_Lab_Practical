sales= [
    [5, 3, 0, 2],
    [7, 0, 2, 1],
    [0, 1, 4, 0]
]

product1 = 0
product2 = 0
product3 = 0
product4 = 0
max_sales = 0
p_max = ""

for i, x in enumerate(sales):
    print("Day", i+1, ":", end='')
    for j, y in enumerate(x):
        if j == 0:
            product1 += y
        elif j == 1:
            product2 += y
        elif j == 2:
            product3 += y
        elif j == 3:
            product4 += y
        print(" Product", j+1, "sold", y, end='')
    print()

if product1 > max_sales:
    max_sales = product1    
    p_max = "Product 1"
if product2 > max_sales:
    max_sales = product2
    p_max = "Product 2"
if product3 > max_sales:
    max_sales = product3
    p_max = "Product 3"
if product4 > max_sales:
    max_sales = product4
    p_max = "Product 4"

min_sales = product1
p_min = ""

if product1 < min_sales:
    min_sales = product1
    p_min = "Product 1"
if product2 < min_sales: 
    min_sales = product2 
    p_min = "Product 2"
if product3 < min_sales:
    min_sales = product3
    p_min = "Product 3"
if product4 < min_sales:
    min_sales = product4
    p_min = "Product 4"

print("Max Sales: ", p_max)
print("Min Sales: ", p_min) 

print('---SUMMARY---')
print("Sales of Product 1: ", product1)
print("Sales of Product 2: ", product2)
print("Sales of Product 3: ", product3)
print("Sales of Product 4: ", product4)
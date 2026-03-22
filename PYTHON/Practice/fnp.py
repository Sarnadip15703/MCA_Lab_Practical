item=['Rice','sugar','salt','atta','dal','potato']
oty=[5,10,3,5,7,8]
profit=[20,40,15,17,23,30]

profit_peritem={item: oty[i]/profit[i] for i, item in enumerate(item)}
print(profit_peritem)

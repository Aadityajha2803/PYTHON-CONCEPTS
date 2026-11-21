def sales_by_product(sales):
    totals = {}
    for product, amount in sales:
        totals[product] = totals.get(product,0)+amount
    return totals
sales = eval(input())
print(sales_by_product(sales))
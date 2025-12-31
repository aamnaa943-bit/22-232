products = ["Product A", "Product B", "Product C"]
sales = [30, 60, 45]

threshold = 50

if len(sales) == 0:
    print("No sales data available")
else:
    for i in range(len(products)):
        if sales[i] >= threshold:
            print(products[i], "is Best-Selling")
        else:
            print(products[i], "is Not Best-Selling")

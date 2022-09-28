total_prod = int(input("Enter the number of products you want to insert: "))
flag = False
for i in range(0, total_prod):
    if total_prod > 0 :
         flag = True
    else:
        flag = False
        break
productDatalst = []
counter = 0
for i in range(total_prod):
    counter += 1
    products_Data ={
        "product name": input("Enter product's " + str(counter) + " name: "),
        "product qty" : int(input("Enter product's " + str(counter) +" quantity: ")),
        "product's price" : float(input("enter product's " + str(counter) + " price: "))
    }
    productDatalst.append(products_Data)

print(productDatalst)
def find_Products():
    flag = False
    find = input("Enter the number of products you want: ")
    for i in productDatalst:
        if  find  == i["product name"]:
            flag = True
            print(i.values())
            break
        else:
            print("product is not exist")

find_Products()

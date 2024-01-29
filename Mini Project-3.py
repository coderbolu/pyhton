shopping_list = []
for items in range(5):
  items = input("What do you want to buy? ")
  shopping_list.append(items)
  print("shopping_list:", shopping_list)
  if items == 5:
    break

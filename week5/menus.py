menus = ["pizza", "burger", "salad"]
print("Initial foods:", menus)

menus.append("pasta")
print("After adding pasta:", menus)

menus.remove("salad")
print("After removing salad:", menus)

menus.sort()
print("Sorted foods:", menus)

print("Total foods:", len(menus))

name = "john doe"
print("Original name:", name)

name_uppercase = name.upper()
print("Uppercase name:", name_uppercase)

name_counter = len(name.replace(" ", ""))
print("Number of characters:", name_counter)

splitted_name = name.split(" ")
print("First name:", splitted_name[0])
print("Last name:", splitted_name[1])

first_name = splitted_name[0][0]
last_name = splitted_name[1][0]

print(f"Initials: {first_name.upper()}.{last_name.upper()}.")

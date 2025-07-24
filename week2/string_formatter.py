# result = format_strings("Hello", "world", "this", "is", "a", "test")
# print(result)  # Output: "HELLOWORLDTHISISATEST"
# result = format_strings("Python", "is", "fun")
# print(result)  # Output: "PYTHONISFUN"
# result = format_strings("Hello world")
# print(result)  # Output: "HELLO-WORLD"
def format(*args):
    if len(args) == 1:
        return str(args[0]).replace(" ", "-").upper()
    
    return ''.join(args).upper()

result = format("Hello", "world", "this", "is", "a", "test")
print(result)  # Output: "HELLOWORLDTHISISATEST"
result = format("Python", "is", "fun")
print(result)  # Output: "PYTHONISFUN"
result = format("Hello world")
print(result)  # Output: "HELLO-WORLD"

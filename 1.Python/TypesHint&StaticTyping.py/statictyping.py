# Static  type checking means type errors before running the program 

def add(a: int, b: int) -> int:
    return a + b

print(add("20", 20))


# Check type errors
# mypy fileName
# pyright fileName
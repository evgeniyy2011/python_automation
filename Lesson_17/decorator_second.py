def decorator_function(fn):
    def wrapper(*args,**kwargs):
        try:
            data = fn(*args,**kwargs)
            return data
        except Exception as error:
            print(f"error ---> {error}")
    return wrapper

@decorator_function
def divide(a:int, b:int):
    return a / b
print(divide(9,0))

import logging
logging.basicConfig(level=logging.INFO)

def loging_args_and_result(fn):
    def wrapper(*args, **kwargs):
        logging.info(f"function starting with your data {args}")
        data = fn(*args,**kwargs)
        logging.info(f"function take date of birth {data}")
        return data
    return wrapper

@loging_args_and_result
def function(currentl_yyear,date_of_birth):
    res = currentl_yyear - date_of_birth
    return f"You are {res} years"

print(function(2026, 1991))






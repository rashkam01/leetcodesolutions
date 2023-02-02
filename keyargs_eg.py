

def catch_all(*args, **kwargs):
    print("args = ", args)
    print("Keyword args = ", kwargs)

input = (1,2,3)
keywords = {'pi': 3.14}

catch_all(*input, kw =2)
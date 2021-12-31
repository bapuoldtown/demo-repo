"""
Generator function for Git Operations demo
"""
def genfunc(func):
    """
    This is the decorated function
    """
    def inner_fun(*args,**kwargs):
        """
        This inner function is returning the value to the geneartor function
        """
        return "This is a decorated Function "+func(*args,**kwargs)
    return inner_fun


@genfunc
def greet_world(emp_one="Guru Prasad",emp_two="Uddipan Roy"):
    """
    This is an original Function
    """
    return "Hello : {} and {}".format(emp_one,emp_two)

if __name__ == '__main__':
    print(greet_world(emp_one="Guru Prasad",emp_two="Uddipan Roy"))

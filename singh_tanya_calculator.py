#define functions for calculator values
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b        

def modulus(a,b):
    if b == 0:
        raise ValueError("Cannot perform modulus by zero")
    return(a%b)

def power(a,b):
    return a**b

def floor_divide(a,b):
    if b == 0:
        raise ValueError("Cannot do floor division by zero")
    return a // b

def convert(value):
    if '.' in value:
        return float(value)
    else: 
        return int(value)
# converting strings to int or float 

#create dictionary of string to int or float

operators = {
'+' : add,
'-' : subtract,
'*' : multiply,
'/' : divide,
'%' : modulus,
'**': power,
'//': floor_divide
}

op = '//'
opres = operators[op](3,4)
print(opres) 

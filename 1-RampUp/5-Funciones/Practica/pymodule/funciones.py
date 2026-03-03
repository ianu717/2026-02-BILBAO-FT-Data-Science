import math

def s_area(b):
    return b ** 2
    
def t_area(b, h):
    return (b * h) / 2
    
def c_area(r):
    return math.pi * r ** 2
    
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
def to_string(*w):
    return " ".join(w)
    
def mod_list(l, cm, e = None):
    if cm == "add":
        l.append(e) 
    elif cm == "remove":
        l.remove(e)
    return l
    
def l_count_d(s):
    d = {}
    for c in s:
        cl = c.lower()
        if cl in d:
            d[cl] += 1
        else:
            d[cl] = 1
    return d
    
def l_count(t, c):
    return t.lower().count(c.lower())
    
def compare_num(n1, n2):
    if n1 > n2:
        return "n1 > n2"
    if n1 < n2:
        return "n1 < n2"
    return "n1 = n2"
    
def create_pyram(rows):
    for i in range(rows, 0, -1):
        print(*range(i, 0, -1))

def num_to_days(num):
    return ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")[num - 1]
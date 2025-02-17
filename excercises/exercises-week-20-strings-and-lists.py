
def split_join_strings():
    s = "chicken=chicken=cheese"
    # Splits the string by the character in split
    s = s.split("=")
    print(s)
    # Joins the strings together using the character in join
    s = " ".join(s)
    print(s)

# Exercise 1
def chop(t):
    del t[0]
    del t[-1]

def middle(t):
    return t[1:-1]

t = [1, 2, 3, 4, 5]
print(t)
t_middle = middle(t)
print(t_middle)
#chop(t)
#print(t)

# Don't forget that most list methods modify the argument and return None. 
# This is the opposite of the string methods, 
# which return a new string and leave the original alone.
# https://docs.python.org/2/library/stdtypes.html#string-methods
# https://docs.python.org/2/library/stdtypes.html#mutable-sequence-types
# https://books.trinket.io/pfe/08-lists.html#debugging
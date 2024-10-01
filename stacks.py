from collections import deque
class stack:
    def __init__(self):
        self.container=deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return True if len(self.container) == 0 else False
    def size_of(self):
        return len(self.container)
    

def is_match(ch1,ch2):
    match_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    return match_dict[ch1] == ch2
def is_balanced(s):
    c=stack()
    for i in s:
        if i == '(' or i == '[' or i == '{':
            c.push(i)
        if i == ')' or i == ']' or i == '}':
            if c.size_of()==0:
                return False
            if is_match(i,c.pop()):
                return True

    return c.size_of()==0

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))


""" c=stack()
c.is_balanced() """
"""x ='charan'
rev=''
c=stack()
for i in x:
    c.push(i)
for i in x:
    rev+=(c.pop())

print(x)
print(rev)


    



print(x[0]) """
""" c=stack()
c.push()
c.pop()
print(c.is_empty()) """
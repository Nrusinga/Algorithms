""" stock_prices=[]

with open("stock_prices.csv","r") as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        price= int(tokens[1])
        stock_prices.append([day,price])

print(stock_prices)
day_to_find='march 6'
for stock in stock_prices:
    if stock[0] == day_to_find:
        print(f"The price on {day_to_find} is {stock[1]}") """


class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.max
        

    def add(self,key,val):
        hash=self.get_hash(key)
        self.arr[hash]=val

    def get(self,key):
        hash=self.get_hash(key)
        return self.arr[hash]

t=HashTable()
print(t.get_hash('march 6'))
t.add('march 6' , 310)
print(t.get('march 6'))
print(t.arr)
    


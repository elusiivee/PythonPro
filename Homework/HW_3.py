#1
def generator(start,amount, rule):
    i=0
    while i< amount:
        yield start
        start = rule(start)
        i+=1

def rule(n):
    return n*2
    # return n**2               #чому квадрат не працює

funk=generator(1,10,rule)

for element in funk:
    print(element)

#2





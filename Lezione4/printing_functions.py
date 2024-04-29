

def construct_rectangle(area: float) -> list[float]:
    """Calculate rectangle area"""
    height: int = int(area**0.5) 
    
    while area%height != 0:
        height -= 1
    
    base= area // height
    
    return[base, height]

print(construct_rectangle(4))
    
#Fibonacci Sequence
def fibonacci(index: int) -> int:
    """Calculate the value of fibonacci with the index"""
    if index <= 0 :
        return 0
    
    elif index == 1:
        return 1
    
    else:
        return fibonacci(index-1) + fibonacci(index-2)

#print(fibonacci(9))


def is_subsequence(s: str, t: str) -> bool:
    """Check if a string is in another string and retun a Boolean"""
    index = 0
    index2 = 0
    
    while index < len(s) and index2 < len(t):
        
        if s[index] == t[index2]:
            index += 1
        index2 += 1
    
    return index == len(s)

#print(is_subsequence("abc", "ahbgdc"))


def moltiplication(x: float, y: float) -> float:
    """Moltiplication"""
    result: float = x*y
    
    return result



         
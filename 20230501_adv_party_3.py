# Pascal's triangle
def pascal(n):
    # base case
    if n < 1:
        return []
    elif n == 1:
        return [1]
    
    # recursion case
    generation = [1]
    last_generation = pascal(n-1)
    for i in range(1, n-1):
        left = last_generation[i-1]
        right = last_generation[i]
            
        generation.append(left + right)
    
    generation.append(1)
    
    return generation
        
print(pascal(int(input())))

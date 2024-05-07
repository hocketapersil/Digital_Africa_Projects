def anagram(tx1, tx2): 
    tx1 = tx1.replace(' ', '').lower()    
    tx2 = tx2.replace(' ', '').lower()
    
    sorted_tx1 = sorted(tx1)
    sorted_tx2 = sorted(tx2)
    
    return sorted_tx1 == sorted_tx2

# Test the function
print(anagram('listen', 'silent')) # True
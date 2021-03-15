def JumBil (num) :
    numeven = []
    numodd = []
    listbil = []
    even_count = 0
    odd_count = 0
    for i in range (num) :
             
        if i % 2 == 0: 
            even_count += 1
            numeven.append(i)
        else: 
            odd_count += 1
            numodd.append(i)
    listbil.append(numeven)
    listbil.append(numodd)
    return listbil
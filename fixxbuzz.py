for x in list(range(1,11)):
    output = ""
    if(x % 2 == 1):
         output += 'OddNumbers'
    else:
        output += 'EvenNumbers'
    print(output, 'for', x)
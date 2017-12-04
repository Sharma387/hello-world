#for loop

for quant in range(100,0,-1):
    if(quant>0):
        print(quant, " bottle of bear on the wall ", quant, " bottles of bear")
        print("Take one down and pass it around", quant-1, " bottle of bears on the wall")
    else:
        print('no more bears on the wall')

    print('------')
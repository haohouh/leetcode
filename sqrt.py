import math
import decimal
k = decimal.Decimal(3 + math.sqrt(5))
k1 = decimal.Decimal(3 - math.sqrt(5))

res = decimal.Decimal(1)
res1 = decimal.Decimal(1)
for i in range(20):
    res *= k 
    print(res % 10000)
    #print(res + res1)

    
    

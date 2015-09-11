import math
from decimal import *

getcontext().prec = 128

number_raw = raw_input('Fibonacci number: \n')
number = Decimal(number_raw)
GR = (Decimal(1) + Decimal(5).sqrt())/Decimal(2)
#print GR
Fibb = (Decimal(GR)**Decimal(number) - ( Decimal(1) - Decimal(GR))**Decimal(number))/Decimal(5).sqrt()
print "The " + number_raw + "th Fibonacci number is: " + str(Decimal(Fibb).quantize(Decimal('1.')))


import array
import numpy_financial as np

fcf = 123
years = 10
g = 15
wacc = 12

print('Enter FCF(in cr):')
fcf = int(input())
print('Enter years assumed:')
years = int(input())
print('Enter growth:')
g = int(input())
print('Enter WACC:')
wacc = int(input())

w = 1 + wacc/100
i = 1 + g/100

npv_list = []

print(i)
for x in range (0, years+1):
    print("CF for years")
    print(x)
    print(fcf * pow(i, x))
    npv_list.append(fcf * pow(i, x))

print(npv_list)

a =  np.npv(w,npv_list) 
print("Net Present Value(npv) : ", a) 


num1 = int(input('Enter "a" for a*b: '))
num2 = int(input('Enter "b" for a*b: '))

def one_iteration():
    product = num1*num2
    print('one iteration =', product)

one_iteration()

def n_iteration():
    for i in range(1,num1+1):
        for j in range(1, num2+1):
            answer = i*j
    print('n iteration =', answer)        

n_iteration()
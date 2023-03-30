def encryption(e_key,no_of_bits,plain_text_bits):
    c = plain_text_bits ** e_key % no_of_bits
    return c
    
    
def decryption(c ,plain_text_bits, d_key,no_of_bits):
    if plain_text_bits == c ** d_key % no_of_bits:
        print('decrytion is possible')
    else:
        print('wrong key')

p = int(input('enter prime p:'))
q = int(input('enter prime q:'))
no_of_bits = p*q
phi_n = (p-1) * (q-1)
while 1:
    i = 0
    e_key = int(input('enter e_key:'))
    d_key = int(input('enter d_key:'))
    if e_key < phi_n and d_key < phi_n:
        plain_text_bits = int(input('enter plain_text_bits:'))
        x = encryption(e_key,no_of_bits,plain_text_bits)
        print('the c value is:' + str(x))
        decryption(x ,plain_text_bits, d_key,no_of_bits)
        exit()
    else:
        if i==3: 
            raise Exception('Sorry you have tried 3 times therefore we exit for now.')
        print('value of e_key and d_key is greater than phi_n')
        print('Please re-enter values')
        i += 1

        
        
        
        
    
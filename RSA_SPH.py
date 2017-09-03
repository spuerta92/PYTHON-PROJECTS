# RSA PROJECT
# Sebastian Puerta Hincapie

def random_generator(x,y):
    from random import randrange
    return randrange(x,y)

##def prime():
##    # for values greater than 2
##    # this implementation does not handle values less than 3
##    # fixed 3 to n
##    from random import randint
##    n = pow(2,8)
##    while(True):
##        rand = randint(3,n)
##        if(rand < 3 or (rand%2 == 0)): continue
##        elif((rand%2) != 0): break
##    return rand

# more efficient prime function
def rand_prime():
    from random import randrange
    while True:
        p = randrange(101, 1000, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def gcd(x,y):
    from fractions import gcd
    return gcd(x,y)

def egcd(a, b):
    if(a == 0):
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if(g != 1):
        print('modular inverse does not exist')
    else:
        return x % m

def encrypt(message,n,e):
    print("Encrypting message...")
    # initializing strings
    str_ints = ""
    segment_str = ""
    enc_str = ""
    
    # converting char to int to string
    # concatinating in a string variable
    for letter in message:
        str_ints += str(ord(letter))
        str_ints += " "
        
    # converting string of ints to segments of ints
    # encrypting each segment of ints
    # converting back to string and concat. in a string
    for integers in str_ints:
        if(integers != " "):
            segment_str += integers;
        elif(integers == " "):
            segment_int = int(segment_str)
            # resets string 
            segment_str = ""                
            enc = pow(segment_int,e) % n
            enc_str += str(enc)
            enc_str += " "
    return enc_str

def decrypt(encrypted,d,n):
    print("Decrypting message...")
    # initializing strings
    segment_str = ""
    dec_str = ""
    segment_str2 = ""
    message = ""

    # converting string of encrypted ints into segment of ints
    # decrypting segment of ints into a string of (ascii) ints
    # converting ints to chars and concat. in a string
    for integers in encrypted:
        if(integers != " "):
            segment_str += integers
        elif(integers == " "):
            segment_int = int(segment_str)
            # resets string
            segment_str = ""
            dec = pow(segment_int,d) % n
            dec_str += str(dec)
            # resets string 
            dec_str += " "
##    print(dec_str)
    for num in dec_str:
        if(num != " "):
            segment_str2 += num
        elif(num == " "):
            segment_num = int(segment_str2)
            # reserts string
            segment_str2 = ""
            message += chr(segment_num)
    return message

class N(object):
    def __init__(self):
##        self.p = 127
##        self.q = 89
        self.p = rand_prime()
        self.q = rand_prime()
    def get_n(self): return self.p * self.q
    def get_phi(self): return (self.p-1)*(self.q-1)
    
class E(object):
    def __init__(self):
        n_object = N()
        self.e = random_generator(1,n_object.get_phi())
    def get_e(self):
        return self.e

def main():
    print("RSA PROJECT")
    n_object = N()
    e_object = E()
    # n value
    n = n_object.get_n()
    print("n: ",n)
    # phi value 
    phi = n_object.get_phi()
    print("phi: ",phi)
    # e value (random)
    e = e_object.get_e()
    print("e: ",e)
    # gcd (check if 1)
    while(True):
        g = gcd(e,phi)
        if(g != 1):
            e = random_generator(1,phi)
            continue
        else: break
    print("GCD: ",g)
    # d value
    d = int(modinv(e,phi))
    print("d: ",d)
    # string message
    message = input("Enter a message to encrypt: ")
    print("Message Length: ", len(message))
    # encrypted message
    encrypted = encrypt(message,n,e)
    print(encrypted)
    # decrypted message
    decrypted = decrypt(encrypted,d,n)
    print(decrypted)


    print("\n- End of program...")
main()

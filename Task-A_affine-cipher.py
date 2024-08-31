# In order to run this program, you need to install a Python package called egcd which is a basic, efficient, and pure-Python implementation of the extended Euclidean algorithm. Information can be found here: https://egcd.readthedocs.io/en/0.6.0/
# The command to install this package: pip install egcd

import sys
import math
from egcd import egcd
    
#=====================================================
# Please do NOT modify the following code, but you are more than welcome to understand the code in detail

class ExtendedAffineCipher:
    
    def __init__(self, alphabet_start, alphabet_end):
        self.alphabet_start = alphabet_start
        self.ord_start = ord(self.alphabet_start[0])
        self.alphabet_end = alphabet_end
        self.alphabet_size = ord(alphabet_end[0])-ord(alphabet_start[0])+1
    
    
    def get_alphabet_size(self):
        return self.alphabet_size
         
    
    def encrypt(self, plain_text, key_a, key_b):
        
        if None == plain_text:
            sys.exit('No plain text to encrypt!')
        
        # Check if the input is legitimate
        for i in plain_text:
            if self.alphabet_start > i and self.alphabet_end < i:
                sys.exit('Illegimate char in the plain text, check against the alphabet set!')
                
        # Check if key_a is a legitimate key
        if not self.is_coprime(key_a, self.alphabet_size):
            sys.exit('The parameter key_a is not set appropriately. Please select a value co-prime with the alphabet size!')
        else:
            key_a = key_a%self.alphabet_size
            key_b = key_b%self.alphabet_size
        
        cipher_text = ""
        for i in plain_text:
            cipher_text += chr((key_a*(ord(i)-self.ord_start)+key_b)%self.alphabet_size + self.ord_start)
        return cipher_text
    
    
    # We use the analytical way with the extended Euclidean Algorithm (note, an exhaustive way might be also possible)
    def decrypt(self, cipher_text, key_a, key_b):
        
        if None == cipher_text:
            sys.exit('No plain text to encrypt!')
        
        # Check if the input is legitimate
        for i in cipher_text:
            if self.alphabet_start > i and self.alphabet_end < i:
                sys.exit('Illegimate char in the plain text, check against the alphabet set!')
                        
        # Check if key_a is a legitimate key
        if not self.is_coprime(key_a, self.alphabet_size):
            sys.exit('The parameter key_a is not set appropriately. Please select a value co-prime with the alphabet size!')
        else:
            key_a = key_a%self.alphabet_size
            key_b = key_b%self.alphabet_size
        
        plain_text=""
        for i in cipher_text:
            plain_text += chr(self.multiplicative_inverse_with_egcd(key_a, key_b, (ord(i)-self.ord_start), self.alphabet_size) + self.ord_start)
        
        return plain_text

        
    # A function determines if two values are coprime
    def is_coprime(self, a, b):
        
        # Use the greatest common divisor (GCD) for the decision
        return 1 == math.gcd(a, b)
    
    
    # Solve equation: a * x + b = c (mod n)
    def multiplicative_inverse_with_egcd(self, a, b, c, n):
        
        # Solve a * y = 1 (mod n) using EGCD
        y = egcd(a, n)[1]
        
        # Now we have a * y * (c-b) = (c-b) (mod n)
        x = (y*((c-b+n)%n))%n
        
        return x

#=====================================================
# Examples of using the extended affine cipher
# Please do NOT alter this part. In Task A, we will use the same alphabet as in the follow example.

# Define an extended affine cipher where the alphabet set ranges from ' ' to '\x7f' (corresponding the printable characters). Please refer to https://www.ascii-code.com the more details about ASCII code table.
cipher = ExtendedAffineCipher(' ', '\x7f')
print("Alphabet size is: ", cipher.get_alphabet_size())

# Encrypt a plain text with the key pair (11, 10)
cipher_text = cipher.encrypt("Hello World, COMP2300/6300!", 11, 10)
print("The example cipher text is: ", cipher_text)

# Decrypt the cipher text generated above
plain_text = cipher.decrypt(cipher_text, 11, 10)
print("The example plain text is: ", plain_text)
print("")

#=====================================================
# Following area is for you to write or complete the code to achieve the answers to Task A


# Subtask A.1 (2 marks): Calculate the number of all the appropriate key pairs and choose a pair of appropriate keys (different from the one used in the example above) to encrypt the plain text "Hello World, COMP2300/6300!". 
# Report (1) the number of all propriate key pairs, (2) the chosen key pair, and the corresponding cipher text as the answers of Task A.1 in the assignment answer template.

plain_text_A_1 = "Hello everyone, welcome to COMP2300/6300!"

# TODO: Your code
# Calculate the number of appropriate key pairs
# Select an appropriate key pair and encrypt the message
# key_a_A_1 = ?
# key_b_A_1 = ?
# cipher_text_A_1 = ?
# Print the cipher text



# Subtask A.2 (3 marks): Now, you are given a piece of cipher text "uA,)V,X)<.,%)Hk)n<w5p.V)W+G)H.)5A,).5<%,k5)(e)U9999999})pk%)5A,)V,X)<.,%)Hk)n<w5p.V)W+N)H.)Xr<')rJk).5<%,k5)(e+", but the key pair is missing.
# Your task is to figure out the key pair and decrypt the cipher text. The corresponding plain text is a meaningful piece of text which offers important information the Task B and Task C.
# To facilitate your cryptanalysis, we have the following plaintext-ciphertext pair: 
#    Plaintext:  Hellow World!
#    Ciphertext: !,]]rJ)*r']%0
# There are two options to achieve this subtask, BUT you just need to choose one to complete. 
# Option 1 is to use analytical analysis with solving a system of equations, which would be more advanced and efficient.
# Option 2 is to use the exhaustive method to try all the possible keys (simple but needs more computation), and check if the deciphered text is meaningful. If you follow this option, you are required to MINIMISE the number of possible keys to attempt. 
# Report (1) For Option 1: descibe the system of equations and how you build it,
#            For Option 2: the number of possible keys you have tried (with justification on if this is the minimal number of attempts),
# (2) the identified key pair, and (3) the corresponding plain text as the answers of Task A.2 in the assignment answer template.

cipher_text_A_2 = "uA,)V,X)<.,%)Hk)n<w5p.V)W+G)H.)5A,).5<%,k5)(e)U9999999})pk%)5A,)V,X)<.,%)Hk)n<w5p.V)W+N)H.)Xr<')rJk).5<%,k5)(e+"

# TODO: Your code to decrypt the cipher text
# Option 1: Analytical inference


# Option 2: A loop can be used to search the key pairs in an exhaustive way.

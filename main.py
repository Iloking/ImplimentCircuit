a = 10
b = 8

print("Binary representation:")
print("a =", bin(a), "b =", bin(b))

xor_result = a ^ b
print("XOR result (a ^ b):", xor_result)
print("Binary (a ^ b):", bin(xor_result))

print("Left shift (a << 1):", a << 1) 

print("Binary (a << 1):", bin(a << 1))
print("Right shift (a >> 1):", a >> 1)  

print("Binary (a >> 1):", bin(a >> 1))

def circuit_logic(A, B, C):
   
    term1 = A & B       
    term2 = B & C       
    term3 = B & ~C & 1  

    Q = term1 | term2 | term3
    return Q

A, B, C = 1, 1, 0
output = circuit_logic(A, B, C)

print("\nCircuit Inputs:")
print("A =", A, "B =", B, "C =", C)
print("Circuit Output Q =", output)
print("Binary Q:", bin(output))

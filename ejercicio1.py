abecedario = [chr(i) for i in range(ord('a'), ord('z')+1)]
abecedario = [letra for i, letra in enumerate(abecedario) if (i+1) % 4!= 0]
print(abecedario)
def keyGeneration(x, privateKey, P):
    return (x**privateKey)%P

if __name__ == "__main__":
    # P and G are a public key that is known to the public
    P, G = 23, 9
    # alice and bob decide on a private key that is not know to anyone other than themselves
    privateKeyAlice = 4
    privateKeyBob = 3
    # generate a key each using the public key P and G and their private keys
    aliceKey = keyGeneration(G, privateKeyAlice, P)
    bobKey = keyGeneration(G, privateKeyBob, P)
    # alice and bob swap these keys and repeat previous process, replacing G with the others generated key
    aliceSecretKey = keyGeneration(bobKey, privateKeyAlice, P)
    bobSecretKey = keyGeneration(aliceKey, privateKeyBob, P)
    # the secret key generated by alice and bob should be the same
    print("alice key:", aliceSecretKey)
    print("bob key:", bobSecretKey)

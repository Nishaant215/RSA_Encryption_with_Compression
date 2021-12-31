#Nishaant Goswamy
import cryptAlg as crypt
from CompressDecompress import CompressEncodedText, Print_Encrypted_Decrypt_Stmt

print("This is RSA Encryption and Decryption")
p = int(input("Enter a prime value for p: "))
q = int(input("Enter a prime value for q: "))

if crypt.primeCheck(p) == True and crypt.primeCheck(q) == True:
    print("Success P and Q are prime numbers")

    n = p * q
    totient = crypt.Totient(p, q)
    print(" n = ", n)
    print("ϕ(n) = ", totient)

    e_key = crypt.Coprime(totient)
    # e_key = 53
    print("e value: ", e_key)  # smallest e value coprime to ϕ(n):

    d_key = crypt.Inverse_Mod(e_key, totient)
    print("d value [de ≡ 1 (mod ϕ(n)))]: ", d_key)  # The d value for

    msg = (input("Enter the message string: "))
    compressNumsList, size = CompressEncodedText(msg)

    decryptedNumList = []
    encryptedNumList = []
    for num in compressNumsList:
        num = int(num)

        if num > n:
            print("Msg_Num bigger than n. Abort")
            quit()

        print("Encrypting the compressed num: ", num)
        # CipherNum = (num ** e_key) % n
        CipherNum = crypt.Square_And_Multiply(num, e_key, n)
        print("Ciphertext of compressed num: ", CipherNum)
        encryptedNumList.append(str(CipherNum).zfill(size))

        # DecryptNum = CipherNum ** d_key % n
        DecryptNum = crypt.Square_And_Multiply(CipherNum, d_key, n)

        print("Decrypted Ciphertext of compressed num: ", DecryptNum)
        decryptedNumList.append(str(DecryptNum).zfill(size))

        if num == DecryptNum:
            print("Success!! The Decrypted Number matches the Original Number\n")

        else:
            print("Decrypted Number does not equal Original Number \n")

    Print_Encrypted_Decrypt_Stmt(encryptedNumList, decryptedNumList, msg)

else:
    print("P and Q not Prime. Function exited")
    quit()



import pyAesCrypt
import string_generator as generator
from os import stat, remove

BUFFER_SIZE = 64*1024


def startCrypt(arguments):
    result = None
    if arguments.e:
        print("Action.encryption.started")
        result = encrypt(arguments.e)
        print("Action.encryption.finished")
    elif arguments.d and arguments.s:
        print("Action.decription.started")
        result = decrypt(arguments.d, arguments.s)
        print("Action.decription.finished")
    return result


def encrypt(file):
    password = generator.generateString(20)
    with open(file, "rb") as fIn:
        with open(file + ".enc", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, BUFFER_SIZE)

    remove(file)
    print("Please, save this key for next time decryption as a (-s) parameter :")
    return password


def decrypt(file, secret):
    file_size = stat(file).st_size
    with open(file, "rb") as fIn:
        out_file = file[0:len(file)-4]
        print(out_file)
        try:
            with open(out_file, "wb") as fOut:
                pyAesCrypt.decryptStream(
                    fIn, fOut, secret, BUFFER_SIZE, file_size)

            remove(file)
            return out_file + " : " + str(file_size)
        except ValueError:
            remove(out_file)

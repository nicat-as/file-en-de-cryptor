import pyAesCrypt
import string_generator as generator
from os import stat, remove

BUFFER_SIZE = 64*1024


def startCrypt(arguments):
    if arguments.e:
        return encrypt(arguments.e)
    elif arguments.d and arguments.s:
        return decrypt(arguments.d, arguments.s)


def encrypt(file):
    password = generator.generateString(20)
    with open(file, "rb") as fIn:
        with open(file + ".enc", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, BUFFER_SIZE)

    remove(file)

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
        return out_file + " : " + file_size
    except ValueError:
        remove(out_file)


#vVoseCGJ38nBZwcRTa2O
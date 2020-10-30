import argparse as arg


def parseArguments():
    parser = arg.ArgumentParser(
        description="For encrypting and decrypting files")

    parser.add_argument("-e", type=str, help="Input file for encryption")
    parser.add_argument("-d", type=str, help="Input file for decryption")
    parser.add_argument("-s", type=str, help="Secret for decryption")

    arguments = parser.parse_args()

    return arguments
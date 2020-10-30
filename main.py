import argument_parser as ap
import file_encryptor as fe

if __name__ == "__main__":
    parsed_arguments = ap.parseArguments()
    result = fe.startCrypt(parsed_arguments)
    print(result)
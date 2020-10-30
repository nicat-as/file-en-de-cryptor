# file-en-de-cryptor

## Description
This script is helping user encrypt important file which contains confedential information. When encrypt your file you'll get file with this ending `yourFile.enc` and secret. When decrypt you'll use `.enc` file and **secret**. After decryption you'll get your file and `.enc` file will be removed. This mean secret key is for one time decryption.   

## How to run?
For running application use following arguments with `python3 main.py`:

- `-e` - Add file for encryption. Example `python3 main.py -e my.txt`
- `-s` - Secret for decryption. After encrypting file secret is generating and printing. Save it in somewhere.  
- `-d` - Add file for decryption. You should use this with `-s`. For example,  `python3 main.py -d my.txt.enc -s mysecret`




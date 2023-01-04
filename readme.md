# BIP 39 protocol implementation

This project is a Python implementation of the BIP39 (Bitcoin Improvement Proposal 39) specification. BIP39 is a standardized way of generating a mnemonic phrase that can be used as a seed for generating the private keys of a cryptocurrency wallet. This implementation allows users to generate a mnemonic phrase and use it to create a cryptocurrency wallet using the BIP39 specification

# Inspiration
The idea for this project came from reading the book "Mastering Ethereum" by Andreas M. Antonopoulos and Dr. Gavin Woods.
## dependencies
To install the required dependencies for this project, run the following command:

```
pip install -r requirements.txt
```



# Running the code
To generate a word list using the BIP39 specification, pass the desired entropy size as the last argument when running the code. 
The entropy size must be a multiple of 32 and must be within the range of 128 to 256 bits. For example:
```sh
python main.py 128
```

The above command will generate a 128-bit strength word list.
### entropy size
Entropy size can be divisible of 32 in range 128<=entropy<=256

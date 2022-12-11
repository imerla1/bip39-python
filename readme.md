# BIP 39 protocol implementation

This project is a Python implementation of the BIP39 (Bitcoin Improvement Proposal 39) specification. BIP39 is a standardized way of generating a mnemonic phrase that can be used as a seed for generating the private keys of a cryptocurrency wallet. This implementation allows users to generate a mnemonic phrase and use it to create a cryptocurrency wallet using the BIP39 specification

# Inspiration
While i was reading `Andreas M. Antonopoulos` and Dr. `Dr. Gavin Woods` genious book `Mastering Ethereum` i Came up with the idea to implemented BIP-39 Protocol

## dependences

# install dependences
```
pip install -r requirements.txt
```



# Run the code
we need to pass only one command line argument to the code to run 
- entropy size
- Generate word list given the strength (128 - 256):
entropy size must be pass as the last parameter
```sh
python main.py 128
```

given example will generate 128 bit strength word list
### entropy size
Entropy size can be divisible of 32 in range 128<=entropy<=256

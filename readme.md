# BIP 39 Protocol Implementation

This project provides a Python implementation of the [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) (Bitcoin Improvement Proposal 39) specification. BIP39 defines a standardized method for generating a mnemonic phrase that can be used as a seed to generate the private keys of a cryptocurrency wallet. This implementation allows users to generate a mnemonic phrase and use it to create a cryptocurrency wallet, fully compliant with the BIP39 specification.

## Inspiration

The idea for this project was inspired by the book *Mastering Ethereum* by Andreas M. Antonopoulos and Dr. Gavin Woods.

## Dependencies

To install the required dependencies for this project, run the following command:

```sh
pip install -r requirements.txt
```

## Running the Code

To generate a word list using the BIP39 specification, specify the desired entropy size as the last argument when running the script. The entropy size must be a multiple of 32 and fall within the range of 128 to 256 bits. For example:

```sh
python main.py 128
```

This will generate a 128-bit strength word list. 

### Entropy Size

The entropy size should be a multiple of 32, and the value must be within the range of **128** to **256** (inclusive). 
!

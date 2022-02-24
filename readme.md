# BIP 39 protocol implementation

Python implementation of BIP39: Mnemonic code for generating deterministic keys

# Inspiration
While i was reading `Andreas M. Antonopoulos` and Dr. `Dr. Gavin Woods` genious book `Mastering Ethereum` i Came up with the idea to implemented BIP-39 Protocol

## dependences

only `python` Version >= `3.6`
all used modules are part of standard library so we don't need to install any additional dependences.

# Configuration File
there is one main configuration file called `config.yaml`
there are 2 main configurations
 - TestConfig
 - ProductionConfig

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
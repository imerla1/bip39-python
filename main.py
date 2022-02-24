import hashlib
import random
import secrets
import sys
import binascii
import textwrap
import os
import sys

class EntropyRangeError(Exception):
	# Custom exception
	pass

entropy_bits = sys.argv[-1]
print(f"Entropy length = {entropy_bits} bits")
'''
As defined in BIP39, the entropy must be a multiple of 32 bits, and its size must be between 128 and 256 bits.
Therefore the possible values for `strength` are 128, 160, 192, 224 and 256.
'''
# check entropy range
if not int(entropy_bits) >= 128 <= 256:
	raise EntropyRangeError("Entropy size must be between 128 and 256 bits") 
# Check if entropy is a multiple of 32 
if int(entropy_bits) % 32 != 0:
	raise TypeError("Entropy Must be a multiple of 32")


def generate_rand_bits(n=128):
	# Generates sequence from 128 to 256 bits
	if not isinstance(n, int):
		raise TypeError("n Must be interger")
	seq = secrets.randbits(n)
	rand_bin = bin(seq)
	return rand_bin[2:].zfill(n) # To avoid 0b at the begging 


entropy = generate_rand_bits(int(entropy_bits))
print(f"Entropy = {entropy}")


'''
In sha256 the hash is calculated wrongly. No Utf8 encoding may be performed. 
Instead, the entropy must be represented as a byte array.
'''
def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def calculate_checksum(entropy):
	# Calculateing checksum 
	entropy_hash = hashlib.sha256(bitstring_to_bytes(entropy)).hexdigest()

	# We will extract first n bits to calculate Checksum
	entropy_hash_to_binary = bin(int(entropy_hash, base=16)).lstrip('0b').zfill(256) 

	checksum_bits = int(entropy_bits) // 32
	print(f"Checksum length = {checksum_bits} bits")
	checksum = entropy_hash_to_binary[:checksum_bits]
	return checksum

checksum = calculate_checksum(entropy)
print(f"Checksum = {checksum}")

# Entropy + checksum
whole_entropy = entropy + checksum
print(f"Entropy + Checksum = {whole_entropy}")

def divide_whole_entropy_to_sections(entropy):
	# We have to divide the entropy + checksum into sections of 11 bits
	# return array of 11 bit sections
	return textwrap.wrap(entropy, 11)

eleven_bit_sections = divide_whole_entropy_to_sections(whole_entropy)
print(f"11 bit Sections, {eleven_bit_sections}")


def get_mnemonic_words(filename="words.txt"):
	try:
		with open(filename) as fr:
			words = fr.read().splitlines()
			return words

	except FileNotFoundError:
		print(f"File {filename} doesn't exist please check the directory")
		sys.exit()

# All 2048 words list
mnemonic_words_list = get_mnemonic_words()

res_words = [] # initialize empty list later we will store 12 mneumonic words here
word_indexes = []

for section_bits in eleven_bit_sections:
	section_decimal_value = int(section_bits, 2)
	word = mnemonic_words_list[section_decimal_value]
	word_indexes.append(section_decimal_value)
	res_words.append(word)
print(f"Word Indexes {word_indexes}")
print("Generated Mnemonic Words")
print(res_words)

# GOSH we implement BIP39 Protocolo well done george well done 👏 👏 👏 







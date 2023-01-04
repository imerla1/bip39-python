import hashlib
import secrets
import textwrap
import sys
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.text import Text


class EntropyRangeError(Exception):
    # Custom exception
    pass


console = Console()
table = Table(title="basic data")
table.add_column("entropy length", style="cyan")
table.add_column("Checksum length", style="magenta")
table.add_column("checksum", style="red")

try:
    entropy_bits = int(sys.argv[-1])
except ValueError:
    console.print(
        "Entropy bits must be multiple of 32 bits in range 128<=entropy<=256")
    sys.exit()

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


def generate_rand_bits(n: int = 128) -> str:
    # Generates sequence from 128 to 256 bits
    if not isinstance(n, int):
        raise TypeError("n Must be integer")
    seq = secrets.randbits(n)
    rand_bin = bin(seq)
    return rand_bin[2:].zfill(n)  # To avoid 0b at the begging


_entropy = generate_rand_bits(int(entropy_bits))
# print(f"Entropy = {entropy}")
panel = Panel(Text(f"Entropy: \n{_entropy}", justify="left", style="cyan bold"))
print(panel)

'''
In sha256 the hash is calculated wrongly. No Utf8 encoding may be performed. 
Instead, the entropy must be represented as a byte array.
'''


def bitstring_to_bytes(s: str) -> bytes:
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


def calculate_checksum(entropy: str) -> str:
    # Calculating checksum
    entropy_hash = hashlib.sha256(bitstring_to_bytes(entropy)).hexdigest()

    # We will extract first n bits to calculate Checksum
    entropy_hash_to_binary = bin(
        int(entropy_hash, base=16)).lstrip('0b').zfill(256)

    checksum_bits = int(entropy_bits) // 32
    checksum = entropy_hash_to_binary[:checksum_bits]
    return checksum


calculated_checksum = calculate_checksum(_entropy)
table.add_row(
    f"{entropy_bits} bits", f"{entropy_bits // 32} bits", calculated_checksum
)
console.print(table)

# Entropy + checksum
whole_entropy = _entropy + calculated_checksum

entropy_checksum_panel = Panel(Text(
    f"Entropy + Checksum: \n{whole_entropy}", justify="left", style="cyan bold"))
print(entropy_checksum_panel)


def divide_whole_entropy_to_sections(entropy: str) -> list:
    # We have to divide the entropy + checksum into sections of 11 bits
    # return array of 11 bit sections
    return textwrap.wrap(entropy, 11)


eleven_bit_sections = divide_whole_entropy_to_sections(whole_entropy)
print(f"Eleven bit sections: total={len(whole_entropy) // 11} sections")
print(eleven_bit_sections)

words_table = Table(title="generated mnemonic words")
words_table.add_column("word index", style="green bold")
words_table.add_column("word", style="cyan")


def get_mnemonic_words(filename: str = "words.txt") -> list:
    try:
        with open(filename) as fr:
            words = fr.read().splitlines()
            return words

    except FileNotFoundError:
        print(f"File {filename} doesn't exist please check the directory")
        sys.exit()


# All 2048 words list
mnemonic_words_list = get_mnemonic_words()

res_words = []  # initialize empty list later we will store 12 mnemonic words here
word_indexes = []

for section_bits in eleven_bit_sections:
    section_decimal_value = int(section_bits, 2)
    word = mnemonic_words_list[section_decimal_value]
    word_indexes.append(section_decimal_value)
    res_words.append(word)
    words_table.add_row(str(section_decimal_value), str(word))
console.print(words_table)
console.print("whole data as json:", style="red underline")
whole_data_json = {
    "entropy": {
        "entropy_bits": entropy_bits,
        "entropy": _entropy
    },
    "checksum_length": f"{entropy_bits // 32} bits",
    "checksum": calculated_checksum,
    "entropyAndChecksum": whole_entropy,
    "eleven_bit_sections_count": f"{len(whole_entropy) // 11} sections",
    "eleven_bit_sections_array": eleven_bit_sections,
    "mnemonic word indexes": word_indexes,
    "mnemonic words": res_words

}
print(whole_data_json)



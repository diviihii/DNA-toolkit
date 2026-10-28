import os

# Lookup table: codon -> amino acid (one-letter code, * = stop)
BASES = "TCAG"
AMINO_ACIDS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE = {}
i = 0
for b1 in BASES:
    for b2 in BASES:
        for b3 in BASES:
            CODON_TABLE[b1 + b2 + b3] = AMINO_ACIDS[i]
            i += 1

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def clean_sequence(raw):
    """Removes spaces/newlines and converts to uppercase."""
    return raw.replace(" ", "").replace("\n", "").upper()


def is_valid_dna(seq):
    """Returns True if the sequence only has A, T, G, C."""
    return len(seq) > 0 and all(base in "ATGC" for base in seq)


def count_bases(seq):
    """Counts each base in the sequence."""
    return {base: seq.count(base) for base in "ATGC"}


def gc_content(seq):
    """Percentage of G and C bases."""
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def reverse_complement(seq):
    """Returns the opposite DNA strand, read 5' to 3'."""
    return "".join(COMPLEMENT[base] for base in reversed(seq))


def transcribe(seq):
    """DNA -> RNA (T becomes U)."""
    return seq.replace("T", "U")


def translate(seq):
    """DNA -> protein, reading 3 bases at a time."""
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        protein += CODON_TABLE[seq[i:i + 3]]
    return protein


def get_sequence():
    """Keeps asking until the user enters a valid DNA sequence."""
    while True:
        seq = clean_sequence(input("Enter a DNA sequence (A, T, G, C only): "))
        if is_valid_dna(seq):
            return seq
        print("Invalid sequence. Use only A, T, G, C.\n")


def main():
    clear_screen()
    print("🧬 Welcome to DNA Toolkit")
    print("-" * 40)

    try:
        seq = get_sequence()
        clear_screen()
        print(f"Sequence : {seq}")
        print(f"Length   : {len(seq)} bases")
        print(f"Counts   : {count_bases(seq)}")
        print(f"GC %     : {gc_content(seq):.2f}")
        print(f"Rev Comp : {reverse_complement(seq)}")
        print(f"RNA      : {transcribe(seq)}")
        print(f"Protein  : {translate(seq)}  (* = stop codon)")
        print("\nPress Ctrl+C anytime to stop.\n")

    except KeyboardInterrupt:
        # Graceful exit if the user stops the script early
        clear_screen()
        print("\nSession ended early. Goodbye! 🧬\n")


if __name__ == "__main__":
    main()

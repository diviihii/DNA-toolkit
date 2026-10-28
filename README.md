# 🧬 dna-cli

> Analyze a DNA sequence right from your terminal.

Biology students often need to quickly check a sequence's GC content,
reverse complement, or protein translation. **dna-cli** is a
zero-dependency Python script that does all of this in one run.

## ✨ Features

- **Zero Dependencies:** Built entirely with Python's standard library. No `pip install` required.
- **Base Counts:** Counts A, T, G and C in your sequence.
- **GC Content:** Calculates the percentage of G and C bases.
- **Reverse Complement:** Gives the opposite DNA strand.
- **Transcription & Translation:** DNA → RNA → protein using the codon table.
- **Input Validation:** Rejects anything that isn't A, T, G or C.

## 🚀 Quickstart

1. Clone the repository:

   ```
   git clone https://github.com/YOUR-USERNAME/dna-cli.git
   cd dna-cli
   ```

2. Run it:

   ```
   python dna_toolkit.py
   ```

3. Enter a DNA sequence when asked, for example:

   ```
   ATGGCCATTGTAATGGGCCGCTGA
   ```

## 📸 Example Output

```
Sequence : ATGGCCATTGTAATGGGCCGCTGA
Length   : 24 bases
Counts   : {'A': 5, 'T': 6, 'G': 8, 'C': 5}
GC %     : 54.17
Rev Comp : TCAGCGGCCCATTACAATGGCCAT
RNA      : AUGGCCAUUGUAAUGGGCCGCUGA
Protein  : MAIVMGR*  (* = stop codon)
```

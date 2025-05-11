## RENAME this file YourLastName_OOP_FinalProject_2025.py
## by Alannah Harnden

##Assignment: Add to the constructor and methods of a parent class and child classes
##            which inherit the base class properties. NOTE: You are not allowed
##            to import any specialized libraries for this project (e.g., no Biopython)
##            The idea is for you to write these methods from scratch.

## Begin with the parent Seq class and the child DNA class we created in lecture below.
## 


### Seq Class
#
#  Constructor:
#  (1) Use the string functions upper and strip to clean up self.sequence.
#  (2) Add a variable self.kmers to the constructor and make it equal to an empty list.

#  Methods:
#  (1) Add a method called make_kmers that makes overlapping kmers of a given length from self.sequence
#      appends these to self.kmers. Default kmer parameter=3.
#  (2) Add a method called fasta that returns a fasta formatted string like this:
#      >species gene
#      AGATTGATAGATAGATAT


### DNA Class: INHERITS Seq class
#   
#  Constructor:
#  Use re.sub to change any non nucleotide characters in self.sequence into an 'N'.
#      re.sub('[^ATGCU]','N',sequence) will change any character that is not a
#      capital A, T, G, C or U into an N. (Seq already uppercases and strips.)

#  Methods:
#  (1) Add a method called print_info that is like print_record, but adds gene_id and an
#      empty space to the beginning of the string.
#  (2) Add a method called reverse_complement that returns the reverse complement of
#      self.sequence
#  (3) Add a method called six_frames that returns all 6 frames of self.sequence
#      This include the 3 forward frames, and the 3 reverse complement frames
                

### RNA Class:  INHERITS DNA class
#  
#  Construtor:
#  Use the super() function (see DNA Class example).
#  (1) Automatically change all Ts to Us in self.sequence. 
#  (2) Add self.codons equals to an empty list

#  Methods:
#  (1) Add make_codons which breaks the self.sequence into 3 letter codons
#      and appends these codons to self.codons unless they are less than 3 letters long.
#  (2) Add translate which uses the Global Variable standard_code below to
#      translate the codons in self.codons and returns a protein sequence.


### Protein Class: INHERITS Seq class
#
#  Construtor:
#  Use the super() function (see DNA Class example).
#  Use re.sub to change any non LETTER characters in self.sequence into an 'X'.

#  Methods:
#  The next 2 methods use a kyte_doolittle and the aa_mol_weights dictionaries.
#  (2) Add total_hydro, which return the sum of the total hydrophobicity of a self.sequence
#  (3) Add mol_weight, which returns the total molecular weight of the protein
#      sequence assigned to the protein object.


### Instance examples to attempt for various classes:

#x=DNA("G","tmp","m",000)


#pro=Protein(" WCVALKKKCCYhhhhh-yyyrsQ\t","my_protein","D. melanogaster", "56008009")
#print(pro)
#print(pro.fasta())
#print(pro.kmers)
#pro.kmers = []
#pro.make_kmers(5)
#print(pro.kmers)

#testp=Protein('VIKING','test','unknown','999')
#print(testp)
#testp.make_kmers(2)
#print(testp.kmers)
#x=testp.total_hydro()
#print(x)
#m=testp.mol_weight()
#print(m)

#pro=Protein(" WCVALKKKCCYhhhhh-yyyrsQ\t","my_protein","D. melanogaster", "56008009")
#print(pro)
#print(pro.fasta())
#print(pro.kmers)
#pro.kmers = []
#pro.make_kmers(5)
#print(pro.kmers)

### End of examples of instances

import re

standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

kyte_doolittle={'A':1.8,'C':2.5,'D':-3.5,'E':-3.5,'F':2.8,'G':-0.4,'H':-3.2,'I':4.5,'K':-3.9,'L':3.8,
                'M':1.9,'N':-3.5,'P':-1.6,'Q':-3.5,'R':-4.5,'S':-0.8,'T':-0.7,'V':4.2,'W':-0.9,'X':0,'Y':-1.3}

aa_mol_weights={'A':89.09,'C':121.15,'D':133.1,'E':147.13,'F':165.19,
                'G':75.07,'H':155.16,'I':131.17,'K':146.19,'L':131.17,
                'M':149.21,'N':132.12,'P':115.13,'Q':146.15,'R':174.2,
                'S':105.09,'T':119.12,'V':117.15,'W':204.23,'X':0,'Y':181.19}
    



#Seq Class.

class Seq:
    def __init__(self, sequence, gene, species):
        self.sequence = sequence.upper().strip()
        self.gene = gene
        self.species = species
        self.kmers = []

    def print_record(self):
        """This function returns the self.sequence as a string
        >>> zak = Seq("CATAGAA", "zakis_gene", "Vombatus ursinus")
        >>> print(zak.print_record())
        CATAGAA
        """
        
        return self.sequence

   def __str__(self):
        return self.species + ", " + self.gene + ": " + self.sequence

    def make_kmers(self, k=3):
        """This function creates kmers from the provided sequence, with a length
            of three each, moving by one, and appending them to a list self.kmers,
            a parameter within the constructor. It ends when there is no further 3-unit
            kmers to form of the sequence.
        >>> khers = Seq("ACTAACCACA", "khers_gene", "Ursus arctos")
        >>> print(khers.make_kmers())
        ['ACT', 'CTA', 'TAA', 'AAC', 'ACC', 'CCA', 'CAC', 'ACA']
        """
        
        self.kmers=[]
        for i in range(0, len(self.sequence), 1):
            kmer = self.sequence[i:i+k]
            if len(kmer) == k:
                self.kmers.append(kmer)
        else:
            pass
        return self.kmers

    def fasta(self):
        """This function returns the fasta title format of self.species, self.gene, followed
        by self.sequence, as a string.
        >>> asb = Seq("ACCATAAT", "asb_gene", "Equus caballus")
        >>> print(asb.fasta())
        >Equus caballus asb_gene
        ACCATAAT
        """
        
        fasta_title = ">" + self.species + " " + self.gene + "\n" + self.sequence
        return fasta_title
    

#DNA Class.
    
class DNA(Seq):
    def __init__(self, sequence, gene, species, gene_id, **kwargs):
        super().__init__(sequence, gene, species)
        self.gene_id = gene_id
        self.sequence = re.sub('[^ATGCU]','N',self.sequence)

   def analysis(self):
        """This function returns the count of Gs and Cs within a given DNA sequence, as
        an integer.
        >>> ghul = DNA("GCGCAAACGCG", "ghul_gene", "Chinese hibiscus", "CHB")
        >>> print(ghul.analysis())
        8
        """
        
        gc_count = 0
        for base in self.sequence:
            if base == 'G' or base == 'C':
                gc_count+=1
        return gc_count

    def print_info(self):
        """This function returns a string entry of printed information, including the gene id
        followed by the sequence.
        >>> ghul = DNA("GCGCAAACGCG", "ghul_gene", "Chinese hibiscus", "CHB")
        >>> print(ghul.print_info())
         CHB GCGCAAACGCG
        """
        
        return  " " + self.gene_id +" " + self.sequence

    def reverse_complement(self):
        """This function reverses the sequence to generate a reverse complement, as a string.
        It first reverses the sequence and then replaces all U's with T's, as to clean up the
        DNA sequence. It then converts each base to its complement nucleotide.
        >>> ordaak = DNA("UACTAC", "ordaak_gene", "Anas platyrhynchos", "ANPLA")
        >>> print(ordaak.reverse_complement())
        CATCAT
        """
        
        self.sequence = self.sequence[::-1]
        self.sequence = self.sequence.replace('U','T')
        for base in self.sequence:
            if base == 'G':
                self.sequence.replace('G','C')
            elif base == 'C':
                self.sequence.replace('C','G')
            elif base == 'A':
                self.sequence.replace('A','T')
            elif base == 'T':
                self.sequence.replace('T', 'A')
        return self.sequence

def six_frames(self):
        """This function returns the first six frames of the sequence -- the first three
        being in the 5'3 direction, and the last 3 in the 3'5 direction. These are returned
        as a list of strings.
        >>> bezorg = DNA("ACCNUATTGCAAAA", "big_gene", "Bezorgious bezo", "BZ")
        >>> print(bezorg.six_frames())
        ['ACCNUATTGCAAAA', 'CCNUATTGCAAAA', 'CNUATTGCAAAA', 'AAAACGTTATNCCA', 'AAACGTTATNCCA', 'AACGTTATNCCA']
        """
        
        frames = []
        f_frame_count = 0  
        for i in range(3):
            frame = self.sequence[i:]
            frames.append(frame)

        self.sequence = self.sequence[::-1]
        self.sequence = self.sequence.replace('U','T')
        for base in self.sequence:
            frame = self.sequence[i:]
            if base == 'G':
                self.sequence.replace('G','C')
            elif base == 'C':
                self.sequence.replace('C','G')
            elif base == 'A':
                self.sequence.replace('A','T')
            elif base == 'T':
                self.sequence.replace('T', 'A')
        for i in range(3):
            frame = self.sequence[i:]
            frames.append(frame)
        return frames

#RNA Class.

class RNA(DNA):
    def __init__(self, sequence, gene, species, gene_id, codons = [], **kwargs,):
        super().__init__(sequence, gene, species, gene_id)
        self.sequence = re.sub('T','U',self.sequence)
        self.codons = codons

    def make_codons(self):
        """This function creates a list of a string of 3-base codons of a provided string RNA
        sequence.
        >>> parwana = RNA("TACACACAT", "parwana_gene", "Morpho menelaus", "MM")
        >>> print(parwana.make_codons())
        ['UAC', 'ACA', 'CAU']
        """
        
        self.codons=[]
        for i in range(0,len(self.sequence),3):
            codon = self.sequence[i:i+3]
            if len(codon) == 3:
                self.codons.append(codon)
            else:
                pass
        return self.codons

    def translate(self):
        """This function translates the list of codons, previously generated from make_codons,
        into a single protein string. It decodes the protein string utilizing the standard_code
        dictionary to find the encoded amino acids.
        >>> parwana = RNA("TACACACAT", "parwana_gene", "Morpho menelaus", "MM")
        >>> parwana.make_codons()
        ['UAC', 'ACA', 'CAU']
        >>> print(parwana.translate())
        YTH
        """
        
        self.codons = self.codons
        protein=''
        for codon in self.codons:
            try: aa = standard_code[codon]
            except: aa = "?"
            protein+= aa
        return protein

  #Protein Class.
    
class Protein(Seq):
    def __init__(self, sequence, gene, species, gene_id):
        super().__init__(sequence, gene, species)
        self.sequence = re.sub('[^A-Za-z]','X',self.sequence)


    def total_hydro(self):
        """This function calculates the hydrophobicity score for a given protein sequence. Pulls
        individual hydrophobiicty scores per amino acids from the Kyle Doolittle dictionary. Returns
        an entire string 'Hyrophobicity score:' followed by the string format of the integer score.
        >>> ghalb = Protein("AXMRIQAIWAFBZA", "ghalb_gene", "Dicentra formosa", "DF")
        >>> ghalb.total_hydro()
        'Hydrophobicity score: 17.6'
        """
        
        total_score = 0
        for i in self.sequence:
            try:hydro_score = kyte_doolittle[i]
            except: "?"
            total_score+= hydro_score
        return "Hydrophobicity score:" + " " +str(total_score)

    def mol_weight(self):
        """This function computes the molecular weight of a provided protein sequence. Similarly,
        it utilizes a dictionary, but of molecular weights per amino acid compounds. The function
        sums up these indivdual weights to calculate overall molecular weight. Returns a single
        line, as a string "Total molecular weight:" followed by the value of the molecular weight
        as a string.
        >>> ghalb = Protein("AXMRIQAIWAFBZA", "ghalb_gene", "Dicentra formosa", "DF")
        >>> ghalb.mol_weight()
        'Total molecular weight: 1788.06'
        """
        
        total_weight = 0
        for i in self.sequence:
            try:weight = aa_mol_weights[i]
            except: "X"
            total_weight+= weight
        return "Total molecular weight:" + " " +str(total_weight)



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

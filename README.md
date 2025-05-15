# Python Project - BIOL668
## Description
This is a completed Python and Biopython project for the BIOL 668 course taught by Dr. Scott Kelley at San Diego State. Through these exercises, students become familar with object-oriented proramming and gain experience with Biopython.
- Required data and files:
  - KRAS.fasta
  - Kras_genbank.gb
  - opuntia.dnd
  - SeqRecord.py
  - 04A_Biopython_Tutorial_LSH-1.ipny
  - OOPTestProject2025.pdf
    

## Instructions (OOP Project)
Download the necessary files, as included in this repository.

Create subclasses from a parent class, ``Seq``, including DNA, RNA, and Protein. Within each subclass, various related functions will be created.

Since DNA, RNA, and Protein will inherit the Seq class, consider using wisely the ``super().__init__``. This is illustrated below with the DNA class, as in the completed file: 

```
class DNA(Seq):
    def __init__(self, sequence, gene, species, gene_id, **kwargs):
        super().__init__(sequence, gene, species)
```

Utilize the OOPTestProject2025 pdf for examples of instances you can make, and what the respective outputs should look like.

To increase the efficiency and accuracy of your code, as included in the provided, complete code, incorporate the ``doctest()`` at the bottom of the file. 

```
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

Recall that proper functioning of the ``doctest()`` requires docstrings per function that you'd like to test. These are comments within """ to describe the expected outcome of an instance utilizing the function at hand. Within the docstring, you should include an instance, to test working program. For example:

```
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
```

## Instructions (Biopython with Jupytr Notebook)

Download the necessary files, as included in this repository. This is all files besides the OOPTestProject2025.pdf.

You will follow the tutorial in the Jupytr Notebook, 04A_Biopython_Tutorial_LSH-1.ipny, designed by Dr. Laura Sisk-Hackworth, learning how to use parts of the Biopython toolset. Really, it demonstrates how modules from Biopython facilitate the process of using different functions related to DNA, without having to generate them yourself. 

You can open this notebook by accessing Jupytr Notebook online, at Project Jupytr (https://jupyter.org/try).

The tutorial frequently refers to the Biopython Tutorial and Cookbook page (https://biopython.org/wiki/Seq).

The variabilty with using Biopython introduces seq feature objects. Additionally, annotations and the methods of extracting them, are provided.

Significantly, the tutorial demonstrates how the ``Phylo`` module can be used to generate phylogenies, and further drawn out with ``ascii``.

```
Phylo.draw_ascii(tree)
```

Those who engage until the end of the tutorial will unveil methods to further analyze constructed phylogenetic trees.

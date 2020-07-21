import mod
from mod import *
#HOW TO VISULAIZE MOLECULES WITH MOD:


            #MOLECULUE,  NAME
mol = smiles("C#N",name="HCN") # # MEANS TRIPLE BOND
mol.print()

mol = smiles("CC#N",name="H3CCN") # # MEANS TRIPLE BOND
mol.print()

# A CARBON SMILES IN [] MEANS IT DONES NOT HAVE HYDROGENS BOUNDED

mol = smiles("[C]#N",name="HN") # # MEANS TRIPLE BOND
mol.print()


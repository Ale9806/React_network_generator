# IMPORT LIBRARIES
from rdkit import Chem #The majority of the basic molecular functionality is here
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit import DataStructs
import numpy as np

a = smiles("CCO")
a.print()

mol  = Chem.MolFromSmiles('CCCC')
smiles = Chem.MolToSmiles(mol) #Convert MOlECULE back to SMILES
print(smiles)
print(" IT DOES WORK WITH RDKIT")


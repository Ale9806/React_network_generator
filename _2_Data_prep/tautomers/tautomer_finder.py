from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.MolStandardize import rdMolStandardize
from rdkit.Chem.Descriptors import ExactMolWt
enumerator = rdMolStandardize.TautomerEnumerator()
def get_canonical_molecules(network):
    """ Gets the canonical SMILES strings and Molecule objects of tautomers  in a Network """
        # BASIC NOTATION
    # name  == SMILES string list
    # name_molecule == Molecule object list

    tautomer_molecules =[] # a list that will hold the most stable tautomer
    tautomer = []
    for i in range(0,len(network)):

        mol = Chem.MolFromSmiles(network[i])         # conver to mol object
        can = Chem.MolToSmiles(mol)                  # back to smiles (this will creat canonical strings)
        can_mol=Chem.MolFromSmiles(can)              # convert back to molto see if there are in fact canonical

        taut_mol = enumerator.Canonicalize(can_mol)  # get tautomer (it only works with molecule objects)
        tautomer_molecules.append(taut_mol)          # append to tuatomer_molecules list
        taut = Chem.MolToSmiles(mol)                 # convert to smiles
        tautomer.append(taut)                        # append to tuatomer (SMILES)list

    return (tautomer,tautomer_molecules)

def get_canonical_strings(tautomer,tautomer_molecules):
    A = [] #list of sets
    B = [] #list of sets
    canonical_tautomer = [] #list that will have the final output

    for mi in tautomer_molecules:
        A.append(mi.GetNumAtoms()) # Give A a property
        B.append(ExactMolWt(mi))   # Give B a property

    set_A = list(set(A)) # Get the set of A
    set_B = list(set(B)) # Get the set of B
    assert(len(set_A)==len(set_B))
    num_of_taut = len(set_A)  # Get the number of tautomer (According to set)
    master = {}  # complex stuff

    for i in range(0,num_of_taut): # more complex stuff (based on Neural Net Weight initalization strategy)
        master['t' + str(i)]="NONE"


    for i in range(0,num_of_taut): #iterate over the numer of tautomers
        for a,b,c in zip(A,B,tautomer):            # zip A,B to iterate
            if  a == set_A[i]  and b == set_B[i]:  # If a & b belong to subset
                if master['t' + str(i)] == "NONE": # and there is no registration
                    master['t' + str(i)] = c       # create registration
                    canonical_tautomer.append(c)   #  append registration
                else:
                    canonical_tautomer.append(master['t' + str(i)]) # if not new append old registration
    return (canonical_tautomer,num_of_taut)

def get_canonical_stringsv2(tautomer,tautomer_molecules):
    A = [] #list of sets
    canonical_tautomer = [] #list that will have the final output

    for mi in tautomer_molecules:
        A.append(mi.GetNumAtoms()) # Give A a property

    set_A = list(set(A)) # Get the set of A
    num_of_taut = len(set_A)  # Get the number of tautomer (According to set)
    master = {}  # complex stuff

    for i in range(0,num_of_taut): # more complex stuff (based on Neural Net Weight initalization strategy)
        master['t' + str(i)]="NONE"

    for i in range(0,num_of_taut): #iterate over the numer of tautomers
        for a,c in zip(A,tautomer):            # zip A,B to iterate
            if  a == set_A[i]:  # If a & b belong to subset
                if master['t' + str(i)] == "NONE": # and there is no registration
                    master['t' + str(i)] = c       # create registration
                    canonical_tautomer.append(c)   #  append registration
                else:
                    canonical_tautomer.append(master['t' + str(i)]) # if not new append old registration
    return (canonical_tautomer,num_of_taut)

def get_canonical_stringsv3(tautomer,tautomer_molecules):
    A = [] #list of sets
    B = [] #list of sets
    canonical_tautomer = [] #list that will have the final output

    for mi in tautomer_molecules:
        A.append(mi.GetNumAtoms()) # Give A a property
        B.append(isring(mi))   # Give B a property

    set_A = list(set(A)) # Get the set of A
    set_B = list(set(B)) # Get the set of B
    #assert(len(set_A)==len(set_B))
    num_of_taut = len(set_A)  # Get the number of tautomer (According to set)
    master = {}  # complex stuff

    for i in range(0,num_of_taut*2): # more complex stuff (based on Neural Net Weight initalization strategy)
        master['t' + str(i)]="NONE"


    for i in range(0,num_of_taut): #iterate over the numer of tautomers
        for a,b,c in zip(A,B,tautomer):
            if  a == set_A[i]  and b == 1:  # If a & b belong to subset
                if master['t' + str(i)] == "NONE": # and there is no registration
                    master['t' + str(i)] = c       # create registration
                    canonical_tautomer.append(c)   #  append registration
                else:
                    canonical_tautomer.append(master['t' + str(i)]) # if not new append old registration

            if  a == set_A[i]  and b == 0:  # If a & b belong to subset
                if master['t' + str(i)] == "NONE": # and there is no registration
                    master['t' + str(i)] = c       # create registration
                    canonical_tautomer.append(c)   #  append registration
                else:
                    canonical_tautomer.append(master['t' + str(i)]) # if not new append old registration

    return (canonical_tautomer,num_of_taut)

def plot_molecules(tautomer_molecules,c=4):
    """ prints the canonical molecule objects (intened to be a visual aid) """
    #just a test to see if wee chose the correct type of input
    if str(type(tautomer_molecules[0])) == "<class 'rdkit.Chem.rdchem.Mol'>":
        pass
    else:
        return

    #LEGEND GENERATOR
    legend_list=[]
    for i in range(1,len(tautomer_molecules)+1):
        if  i== 1:
            dummie="st"
        elif i == 2:
            dummie="nd"
        elif i== 3:
                dummie="rd"
        else:
            dummie="th"
        legend_list.append(str(i)+ dummie + " Moluecule")

    # Some visual settings
    tab="\t\t\t      " #adds tabs
    print("\033[1m" + tab +"TAUTOMR MOLECULES:" + "\033[0m") # title in bold
    img = Draw.MolsToGridImage(tautomer_molecules,molsPerRow =c,legends=legend_list)

    return img

def plot_smiles(network,c=4,title="INPUT Molecules"):
    mols = []
    for i in range(0,len(network)):
        mol = Chem.MolFromSmiles(network[i])
        mols.append(mol)
    legend_list=[]
    for i in range(1,len(mols)+1): # len +1 because for loop starts from 1
        if  i== 1:
            dummie="st"
        elif i == 2:
            dummie="nd"
        elif i== 3:
            dummie="rd"
        else:
            dummie="th"
        legend_list.append(str(i)+ dummie + " Moluecule")

    # Some visual settings
    tab="\t\t\t      " #adds tabs
    print("\033[1m" + tab +title+ "\033[0m")
    img = Draw.MolsToGridImage(mols,molsPerRow =c,legends=legend_list)
    return (mols,img)

def isring(mol):
    isring = 0
    a =mol.GetRingInfo()
    for i in range(mol.GetNumAtoms()):
        if  a.NumAtomRings(i) == 1:
            isring = 1
        else:
            pass
    return isring

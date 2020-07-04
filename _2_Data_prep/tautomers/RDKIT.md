# RDKIT
To clean the data I used RDKIT canonical function. It is important to keep in mind that RDKIT transforms smiles strings
into multidimensional arrays that are stored as Molecule Objects, this objects are quite usfule, you can store information in them to ahive different task such as: 
<br><br>
**Hilgiht atoms** <br>
**Add indicies** <br>
**Add text**    <br>
**...** <br>
<br>
RDKIT's MOl object is able to get the canonical representation of a Smiles String, but it's not able to obtain the canoncial represenation of tautomers.
For this we can use mod's canonical tautomer represenation, but keep in mind that it gives the representation according to how the molecule was fed to the function.
This means that if a molecule is rotated, RDKIT is going to output 2 "different" smiles (this smiles are just rotated) this is an issue that we have to keep in mind.
Throught the code there are parts that seem to be repetitive, this parts are **NOT REPETEITVE** and are essential for the code to work.

# Video time 2:00:00

# The only problem with this method is that we cannont use the same molecule more the once
# in order to encode another reaction (this will generated an error due to the fact that it 
# detecets isomorphism

dg = DG()
with dg.build() as b:
    d = Derivation()
    d.left = [smiles("O"),smiles("CO")]
    d.right = [smiles("[Au]")]
    b.addDerivation(d)

    d = Derivation()
    d.left = [smiles("cccc"),smiles("CCC")]
    d.right = [smiles("CCCCCC")]
    b.addDerivation(d)
  

dg.print()

dg = DG()
A = smiles("O")
with dg.build() as b:
    b.addAbstract("""
 A +B -> C  
 C -> B 
A + D +C -> B """)
  

dg.print()


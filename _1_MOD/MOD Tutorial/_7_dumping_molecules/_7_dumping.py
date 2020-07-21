# time: 1:19:00 at video
# In this file we'll learn how to dump molecules
# into a file

include("rules.py") # mod way of importing files

postSection("Input Rules")
for a in inputRules:
    a.print()

postSection("Input Graphs (Molecules)")
for a in inputGraphs:
    a.print()

dg = DG(graphDatabase=inputGraphs)

def pred(derivation):
    for p in derivation.right:
        if p.exactMass > 200:
            return False
        return True 

with dg.build() as b:
    b.execute(
            addSubset(formaldehyde, glycolaldehyde)
            >> rightPredicate[pred](repeat(inputRules) )
        )
dg.print()

# creates a dg file in out (usaually called 059_DG.dg)

f = dg.dump()
print("Dump file:", f)


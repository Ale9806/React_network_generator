# time: 1:10:00 at video
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
        numCs = 0
        for v in p.vertices:
            if v.stringLabel == "C":
                numCs += 1
        if numCs > 6:
            return False

        return True 

with dg.build() as b:
    b.execute(
            addSubset(formaldehyde, glycolaldehyde)
            >> rightPredicate[pred](repeat(inputRules) )
        )
dg.print()



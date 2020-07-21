# time: 1:20:00
include("rules.py")

# lets read the date we dumped 
# We also did cp out/059_DG.dg Network.dg to optain a copy in the root directory

#read
dg = dgDump(inputGraphs,inputRules, "Network.dg")

# say we want to go througj all of the molecuel s(vertices) on the network
for v in dg.vertices:
    v.graph.print()
#say we also want to print the grahp (molecule ) name and smiles strings
    print(v.graph.name,v.graph.smiles)

for e in dg.edges:
    for v in e.sources:
        if v.graph == formaldehyde:
            e.print()



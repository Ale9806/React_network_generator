import mod
from mod import *
#HOW TO VISULAIZE MOLECULES WITH MOD:
   
   
                          #MOLECULUE,  NAME
glycolaldehyde = smiles("OCC=O","glycolaldehyde")

ketoEnol = ruleGMLString("""
rule[

    left [
    edge [source 1 target 2 label "-"]
    edge [source 1 target 4 label "-"]
    edge [source 2 target 3 label "="]
    ]

    context[
    node [id 1 label "C"]
    node [id 2 label "C"]
    node [id 3 label "O"]
    node [id 4 label "H"]
    node [id 5 label "H"]
    edge [source 2 target 5 label "-"]
    ]

    right[
    edge [source 1 target 2 label "="]
    edge [source 3 target 4 label "-"]
    edge [source 2 target 3 label "-"]
    ]
]

""")

ketoEnol.name = "Keto-enol" #Gives number to rule
enolKeto   = ketoEnol.makeInverse() #creates an inverse rule of the original rule

p = GraphPrinter()
p.withIndex = True #adds the indexing we initaily set

#instead of printing rule by rule there is a variable that stores all rules
# but it does not take into account ivnerse ruleso we need to append that

inputRules.append(enolKeto)
print(inputRules) 

# Now we can print all inpuntRules
#kenolKeto.print(p) # prints the inverse rule we defined
postSection("Input Rules") #creats a section 
for a in inputRules:
    a.print(p)

# Similarly thre is a variable called inputGraphs
postSection("Input Molecules") 
for a in inputGraphs:
    a.print()

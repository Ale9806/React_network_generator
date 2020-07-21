SHELL=/bin/bash
summary/all.tex: gen
	echo '\summaryRule{Keto-enol}{\summaryRuleSpan{out/001_r_0_10300010}{out/001\_r\_0\_10300010}}{}{\summaryRuleCombined{out/002_r_0_combined}{out/002\_r\_0\_combined}}{out/003_r_0_constraints.tex}' >> summary/all.tex
	echo '\summaryRule{Keto-enol, inverse}{\summaryRuleSpan{out/005_r_1_10300010}{out/005\_r\_1\_10300010}}{}{\summaryRuleCombined{out/006_r_1_combined}{out/006\_r\_1\_combined}}{out/007_r_1_constraints.tex}' >> summary/all.tex
summary.pdf: summary/all.tex
	/usr/local/bin/../bin/mod_post --mode compileSummary
include summary/MakefileImpl
include summary/MakefileDep
include summary/MakefileAllTarget
include summary/MakefileClean

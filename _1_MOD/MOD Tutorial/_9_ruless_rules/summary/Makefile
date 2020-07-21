SHELL=/bin/bash
summary/all.tex: gen
	echo '\summaryDGHyper{\texttt{dg\_0}}{out/007_dg_0_11100}{\texttt{out/007\_dg\_0\_11100}}' >> summary/all.tex
	echo '\summaryDGHyper{\texttt{dg\_1}}{out/013_dg_1_11100}{\texttt{out/013\_dg\_1\_11100}}' >> summary/all.tex
summary.pdf: summary/all.tex
	/usr/local/bin/../bin/mod_post --mode compileSummary
include summary/MakefileImpl
include summary/MakefileDep
include summary/MakefileAllTarget
include summary/MakefileClean

SHELL=/bin/bash
summary/all.tex: gen
	echo -n '\summaryGraph' >> summary/all.tex
	echo '{\texttt{g\_\{0\}}}{\summaryGraphFile{out/000_g_0_10300000}{\texttt{out/000\_g\_0\_10300000}}}{\summaryGraphFile{out/000_g_0_11310100}{\texttt{out/000\_g\_0\_11310100}}}' >> summary/all.tex
summary.pdf: summary/all.tex
	/usr/local/bin/../bin/mod_post --mode compileSummary
include summary/MakefileImpl
include summary/MakefileDep
include summary/MakefileAllTarget
include summary/MakefileClean

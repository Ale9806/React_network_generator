SHELL=/bin/bash
summary/all.tex: gen
	echo -n '\summaryGraph' >> summary/all.tex
	echo '{\texttt{HCN}}{\summaryGraphFile{out/000_g_0_10300000}{\texttt{out/000\_g\_0\_10300000}}}{\summaryGraphFile{out/000_g_0_11310100}{\texttt{out/000\_g\_0\_11310100}}}' >> summary/all.tex
	echo -n '\summaryGraph' >> summary/all.tex
	echo '{\texttt{H3CHCN}}{\summaryGraphFile{out/001_g_1_10300000}{\texttt{out/001\_g\_1\_10300000}}}{\summaryGraphFile{out/001_g_1_11310100}{\texttt{out/001\_g\_1\_11310100}}}' >> summary/all.tex
	echo -n '\summaryGraph' >> summary/all.tex
	echo '{\texttt{HN}}{\summaryGraphFile{out/002_g_2_10300000}{\texttt{out/002\_g\_2\_10300000}}}{\summaryGraphFile{out/002_g_2_11310100}{\texttt{out/002\_g\_2\_11310100}}}' >> summary/all.tex
summary.pdf: summary/all.tex
	/usr/local/bin/../bin/mod_post --mode compileSummary
include summary/MakefileImpl
include summary/MakefileDep
include summary/MakefileAllTarget
include summary/MakefileClean

rule [
	ruleID "r_{9}"
	labelType "string"
	left [
		edge [ source 1 target 0 label "=" ]
		edge [ source 5 target 7 label "=" ]
		edge [ source 7 target 9 label "-" ]
		edge [ source 9 target 10 label "-" ]
	]
	context [
		node [ id 0 label "C" ]
		node [ id 1 label "O" ]
		node [ id 2 label "H" ]
		node [ id 3 label "H" ]
		node [ id 4 label "O" ]
		node [ id 5 label "C" ]
		node [ id 6 label "H" ]
		node [ id 7 label "C" ]
		node [ id 8 label "H" ]
		node [ id 9 label "O" ]
		node [ id 10 label "H" ]
		node [ id 11 label "H" ]
		edge [ source 2 target 0 label "-" ]
		edge [ source 3 target 0 label "-" ]
		edge [ source 5 target 6 label "-" ]
		edge [ source 4 target 5 label "-" ]
		edge [ source 7 target 8 label "-" ]
		edge [ source 4 target 11 label "-" ]
	]
	right [
		edge [ source 1 target 0 label "-" ]
		edge [ source 5 target 7 label "-" ]
		edge [ source 7 target 9 label "=" ]
		edge [ source 0 target 5 label "-" ]
		edge [ source 1 target 10 label "-" ]
	]
]
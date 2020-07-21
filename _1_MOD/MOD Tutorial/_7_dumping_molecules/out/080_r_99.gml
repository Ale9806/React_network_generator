rule [
	ruleID "r_{99}"
	labelType "string"
	left [
		edge [ source 1 target 0 label "=" ]
		edge [ source 11 target 12 label "=" ]
		edge [ source 11 target 20 label "-" ]
		edge [ source 20 target 21 label "-" ]
	]
	context [
		node [ id 0 label "C" ]
		node [ id 1 label "O" ]
		node [ id 2 label "H" ]
		node [ id 3 label "H" ]
		node [ id 4 label "C" ]
		node [ id 5 label "H" ]
		node [ id 6 label "H" ]
		node [ id 7 label "C" ]
		node [ id 8 label "H" ]
		node [ id 9 label "O" ]
		node [ id 10 label "H" ]
		node [ id 11 label "C" ]
		node [ id 12 label "C" ]
		node [ id 13 label "C" ]
		node [ id 14 label "O" ]
		node [ id 15 label "H" ]
		node [ id 16 label "H" ]
		node [ id 17 label "H" ]
		node [ id 18 label "O" ]
		node [ id 19 label "H" ]
		node [ id 20 label "O" ]
		node [ id 21 label "H" ]
		node [ id 22 label "O" ]
		node [ id 23 label "H" ]
		edge [ source 2 target 0 label "-" ]
		edge [ source 3 target 0 label "-" ]
		edge [ source 4 target 5 label "-" ]
		edge [ source 4 target 6 label "-" ]
		edge [ source 7 target 8 label "-" ]
		edge [ source 7 target 9 label "-" ]
		edge [ source 9 target 10 label "-" ]
		edge [ source 4 target 7 label "-" ]
		edge [ source 13 target 14 label "-" ]
		edge [ source 14 target 15 label "-" ]
		edge [ source 13 target 16 label "-" ]
		edge [ source 12 target 13 label "-" ]
		edge [ source 13 target 17 label "-" ]
		edge [ source 12 target 18 label "-" ]
		edge [ source 18 target 19 label "-" ]
		edge [ source 7 target 11 label "-" ]
		edge [ source 4 target 22 label "-" ]
		edge [ source 22 target 23 label "-" ]
	]
	right [
		edge [ source 1 target 0 label "-" ]
		edge [ source 11 target 12 label "-" ]
		edge [ source 11 target 20 label "=" ]
		edge [ source 0 target 12 label "-" ]
		edge [ source 1 target 21 label "-" ]
	]
]
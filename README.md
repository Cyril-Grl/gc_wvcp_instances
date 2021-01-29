# gc_wvcp_instances

instances for graph coloring and weighted vertex coloring problem

origine of files :
	
	- wvcp_original : http://www.info.univ-angers.fr/pub/hao/wvcp.html
	- graph_coloring : DIMACS Challenge II 
	- bandwidth_multicoloring_instances : https://mat.gsia.cmu.edu/COLOR04/

wvcp directory contains all graphs gathered and their weights, you can find three types of files :
	
	- .col files from DIMACS Challenge
	- .edgelist files : each line is an edge between two nodes
	- .col.w files : line 1 is the weight of the node 0, line 2 the weight of the node 1 ...

You can find the currents best score (probably not updated) for the wvcp coloring problem in the file best_scores_wvcp.txt, 0 mean no best score known.

Files may have been modified to suppress lines, weights at the end of .col file supressed to generate .col.w file for exemple, but all graphs remain the same (number of nodes and edges, ...)

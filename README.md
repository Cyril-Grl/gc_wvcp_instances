# instances for graph coloring and weighted vertex coloring problem

origine of files :
	
	- wvcp_original : http://www.info.univ-angers.fr/pub/hao/wvcp.html
	- graph_coloring : DIMACS Challenge II 
	- bandwidth_multicoloring_instances : https://mat.gsia.cmu.edu/COLOR04/

wvcp directory contains all graphs gathered and their weights, you can find three types of files :

	- .col files from DIMACS Challenge (vertices numbers start at 1)
	- .edgelist files : each line is an edge between two nodes (vertices number start at 0)
	- .col.w files : line 1 is the weight of the node 0, line 2 the weight of the node 1 ...
	- .wcol files : DIMACS Challenge files + v lines with the weights of each vertices (vertices numbers start at 1)

Files may have been modified to suppress lines, weights at the end of .col file supressed to generate .col.w file for exemple, but all graphs remain the same (number of nodes and edges, ...) if you find any mistake please inform us.

You can find the currents best score (known from Nogueira, Bruno, Eduardo Tavares, et Paulo Maciel. «Iterated Local Search with Tabu Search for the Weighted Vertex Coloring Problem». Computers & Operations Research 125 (1 janvier 2021): 105087. https://doi.org/10.1016/j.cor.2020.105087.) for the wvcp coloring problem in the file best_scores_wvcp.txt, * mean optimal score and - mean best current score (maybe optimal but not proved). You can also find all scores from the article in sota_wvcp.ods .


To add theses instances to your project :

	git submodule add https://github.com/Cyril-Grl/gc_wvcp_instances.git instances

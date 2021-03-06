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

Files may have been modified to suppress lines, weights at the end of .col file suppressed to generate .col.w file for exemple, but all graphs remain the same (number of nodes and edges, weights,...) if you find any mistake please inform us.

You can find the currents best score (known from Nogueira, Bruno, Eduardo Tavares, et Paulo Maciel. «Iterated Local Search with Tabu Search for the Weighted Vertex Coloring Problem». Computers & Operations Research 125 (1 janvier 2021): 105087. https://doi.org/10.1016/j.cor.2020.105087.) for the wvcp coloring problem in the file best_scores_wvcp.txt, * mean optimal score and - mean best current score (maybe optimal but not proved). You can also find all scores from the article in sota_wvcp.ods .


The repertory cliques contains all cliques for each graph, computed with igraph,  https://igraph.org/, except for the following graphes where you can find only a part of the cliques, computed with the output of mnts, http://www.info.univ-angers.fr/%7Ehao/clique.html :

	- DSJC500.5 (file to big, only 1000000 first biggest cliques)
	- R75_9gb (file to big, only 1000000 first biggest cliques)
	- R75_9g (file to big, only 1000000 first biggest cliques)
	- flat1000_50_0
	- flat1000_60_0
	- flat1000_76_0
	- DSJC1000.5
	- C2000.5
	- latin_square_10
	- DSJC250.9
	- R100_9g
	- R100_9gb
	- DSJC125.9g
	- DSJC125.9gb
	- DSJC1000.9
	- C2000.9
	- DSJC500.9


The repertory reduction contains for each graph all vertices that can be delete from the graph because they have no impact on the problem (low weight/degree).

The repertory reduction_n2 contains for each graph all vertices that can be delete from the graph because their neighbors share the same neighbor and its weight is equal or higher (first number is the vertex that can be deleted because it can take the color of the second number/vertex without impacting the score or the coloring or other vertices)

To add theses instances to your project :

	git submodule add https://github.com/Cyril-Grl/gc_wvcp_instances.git instances

To update :

	cd instances/
	git pull origin main
	cd ..
	git add instances/
	git commit -m "submodule instance updated"
	git push
	
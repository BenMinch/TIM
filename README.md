# TIM - Taxon Interaction Mapper
TIM detects and maps interactions between organisms onto a phylogenetic tree of a target group of organisms.<br />
Interactions are predicted from a species co-occurence-based network (such as one generated by FlashWeave).<br />

TIM assumes that evolutionarily related organisms (refer to as ```query```) interact with evolutionary related organisms (```subject```) (The reciprocal is not true).<br />

#### Nota bene:
TIM was developed and first applied to infer host group of marine eukaryotic viruses (see references).<br />
TIM tests for enrichement of connection between query and subject at the order level (hard-coded for now).<br />

## Prerequisites
* [ETE3 v3](http://etetoolkit.org/download/) 
* [Python 2.7.11 or greater](https://www.python.org/downloads/release/python-2711/)
* [R](https://www.r-project.org/)

## Usage
TIM runs in two main steps: <br />
```main.py tree.nwk connections.tsv [ALL, POS, NEG]``` <br />
```downstream.py``` <br />

## Input files
* A phylogenetic tree (newick formated) for the ```query``` <br /> 
* A table file containing network connections between ```query``` and ```subject``` with follwing tab separated columns: <br />
&nbsp;&nbsp;Query ID (must be the same as leaves's names in the tree) <br />
&nbsp;&nbsp;Subject ID <br />
&nbsp;&nbsp;Direction of connections (typically the weight, positive or neagtive, in a co-occurence-based network) <br />
&nbsp;&nbsp;P-value (facultative can be NA if you pre-filtred the connections) <br />
&nbsp;&nbsp;Genealogy of the subject ID (Must be NCBI taxonomic terms. If a taxomic name is not found the tool will report it) <br />

#### Example of input files: <br />
```Picornavirales.nwk``` a phylogenetic tree for Picornavirales viruses containing Tara Oceans and reference sequences <br />
```connections.txt```FlashWeave Inferred associations between Picornavirales and Eukaryotes based on Tara Oceans samples<br />

## Output files
Results are in the directory ```myTIMrun``` <br />
For ```main.py```:<br />
&nbsp;&nbsp;```allNodesCounts.txt```: Contains count of connections for a given ```subject``` and ```query``` at a given node. <br />
&nbsp;&nbsp;```taxaNotInNCBI.txt``` : list of taxa's name in your connection file that were not found in the NCBI taxonomy <br />
&nbsp;&nbsp;```NODES``` contains details for ecach visited node. <br />
For ```downstream.py```:  <br />
In ```myTIMrun/downstream```: <br />
&nbsp;&nbsp;The two following files belwo can be use to visualize TIM results on ITOL:<br />
&nbsp;&nbsp;&nbsp;&nbsp;```PIECHART_ITOL.txt```: node with enriched connections towards a group of organism (Q<0.05 by default).<br />
&nbsp;&nbsp;&nbsp;&nbsp;```treeWithNodeID_forItolPlot.nwk```: the tree you input with node ID added.<br />

## Scripts
| Filename | Description |
| ---- | :--- |
|```main.py```|report number of connections between leaves in the tree and a taxonomic group (NCBI order rank) |
|```downstream.py```|filters out the output of ```main.py``` and prepare files for visualization with iTOL|
|```filt_form.R```|used by ```downstream.py``` for filtering and files formating|
|```formatForItolPieChart.py```|formats files to plot results on iTOL|
|```addFeaturesToTreeNode.py```|add node ID to the tree for iTOL visualization|

## Contact
* **Romain Blanc-Mathieu**  - romain.blancmathieu[@]gmail.com

## References
Blanc-Mathieu R*, Kaneko H*, Endo H, Chaffron S, Hernández-Velázquez R, Nguyen CH, Mamitsuka H, Henry N, Vargas C de, Sullivan MB, et al. 2019. Viruses of the eukaryotic plankton are predicted to increase carbon export efficiency in the global sunlit ocean. bioRxiv:710228.
https://www.biorxiv.org/content/10.1101/710228v1.full


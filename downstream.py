#!/Users/romain/anaconda_ete/bin/python
from __future__ import division
import os
import sys
import random

def moulinette(METHOD):
	os.system("scripts/filt_form.R %s" % METHOD)
	os.system("python scripts/formatForItolPieChart.py")
	os.system("mkdir myTIMrun/downstream")
	os.system("mkdir myTIMrun/downstream/others")
	os.system("mv PIECHART_ITOL.txt myTIMrun/downstream/.")
	os.system("mv correctedPvalues.txt plotItol_node_* itol_node_* myTIMrun/downstream/others/.")
	os.system("rm inputForPieChart.txt tmpHeaderItol.txt")
	os.system("python scripts/addFeaturesToTreeNode.py Picornavirales.nwk")
	os.system("mv treeWithNodeID_forItolPlot.nwk myTIMrun/downstream/.")
moulinette("BH")

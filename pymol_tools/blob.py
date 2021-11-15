'''

##############################################################
This script creates map and isosurface objects for each chain of a specified object or objects in PyMOL. To use:
	1. Load the script in the PyMOL command line: load /path/to/blob.py
	2. Run in the PyMOL command line: blob protein_to_blob
		2a. PyMOL can understand regular expressions, so e.g running "blob *" will blob all objects

This script will take a bit of time to run but the output blobs are nicely low in detail for clear images of low-resolution shape.

Script written by Robby Divine, borrowing heavily from Will Sheffler
##############################################################

'''

from pymol import cmd
import glob

def blob(designs):
	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")

	designs = cmd.get_object_list(designs)
	for design_name in designs:
		print(design_name)
		for chain_id in cmd.get_chains(design_name):
			#cmd.do("create copy_" + chain_id + ", " + design_name + " and chain " + chain_id)
			cmd.do("map_new map_{chain_id}_{design_name}, gaussian, 1, ({design_name} and chain {chain_id} and name CA), 10".format(chain_id=chain_id, design_name=design_name))
			cmd.do("isosurface blob_{chain_id}_{design_name}, map_{chain_id}_{design_name}".format(chain_id=chain_id, design_name=design_name))



cmd.extend( "blob", blob )
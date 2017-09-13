###############################################################################
#                                                                             #
# Copyright (C) 2004-2005,2008,2017 Edward d'Auvergne                         #
#                                                                             #
# This file is part of the program relax (http://www.nmr-relax.com).          #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by        #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
###############################################################################

"""Script for calculating NOEs."""


# Python module imports.
from time import asctime, localtime

# relax module imports.
from auto_analyses.noe import NOE_calc


# Create the data pipe.
pipe_bundle = "noe (%s)" % asctime(localtime())
pipe.create(pipe_name='NOE', pipe_type='noe', bundle=pipe_bundle)

# Load the sequence.
sequence.read(file='Ap4Aase.seq', dir='..', res_num_col=1, res_name_col=2)

# Name the spins so they can be matched to the assignments.
spin.name(name='N')

# Add the Trp 40 indole spin.
spin.create(res_num=40, spin_name='NE1')

# Load the reference spectrum and saturated spectrum peak intensities.
spectrum.read_intensities(file='ref_ave.list', dir='..', spectrum_id='ref_ave')
spectrum.read_intensities(file='sat_ave.list', dir='..', spectrum_id='sat_ave')

# Set the spectrum types.
noe.spectrum_type('ref', 'ref_ave')
noe.spectrum_type('sat', 'sat_ave')

# Set the errors.
spectrum.baseplane_rmsd(error=3200, spectrum_id='ref_ave')
spectrum.baseplane_rmsd(error=2600, spectrum_id='sat_ave')

# Individual residue errors.
spectrum.baseplane_rmsd(error=15000, spectrum_id='ref_ave', spin_id=":114")
spectrum.baseplane_rmsd(error=2400, spectrum_id='sat_ave', spin_id=":114")

# Deselect unresolved residues.
deselect.read(file='unresolved', dir='..', res_num_col=1)

# Execute the auto-analysis.
NOE_calc(pipe_name='NOE', pipe_bundle=pipe_bundle, file_root='noe', results_dir='.', save_state=True)

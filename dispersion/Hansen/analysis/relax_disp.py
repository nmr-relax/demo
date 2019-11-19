###############################################################################
#                                                                             #
# Copyright (C) 2013 Edward d'Auvergne                                        #
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

# Module docstring.
"""Script for CPMG relaxation dispersion curve fitting using Dr. Flemming Hansen's data from http://dx.doi.org/10.1021/jp074793o."""


# Python module imports.
from os import sep

# relax module imports.
from auto_analyses.relax_disp import Relax_disp
from data_store import Relax_data_store; ds = Relax_data_store()
from status import Status; status = Status()


# The dispersion models.
MODELS = ['R2eff', 'No Rex', 'LM63', 'LM63 3-site', 'CR72', 'CR72 full', 'IT99', 'NS CPMG 2-site 3D', 'NS CPMG 2-site expanded', 'NS CPMG 2-site star', 'MMQ CR72']

# The grid search size (the number of increments per dimension).
GRID_INC = 11

# The number of Monte Carlo simulations to be used for error analysis at the end of the analysis.
MC_NUM = 50

# The results directory.
RESULTS_DIR = '.'

# The model selection technique to use.
MODSEL = 'AIC'

# The flag for only using numeric models in the final model selection.
NUMERIC_ONLY = False

# The R2eff value in rad/s by which to judge insignificance.  If the maximum difference between two points on all dispersion curves for a spin is less than this value, that spin will be deselected.
INSIGNIFICANCE = 0.0



# Set up the data pipe.
#######################

# Create the data pipe.
pipe_name = 'base pipe'
pipe_bundle = 'relax_disp'
pipe.create(pipe_name=pipe_name, bundle=pipe_bundle, pipe_type='relax_disp')

# Load the sequence.
sequence.read('fake_sequence.in', dir='..', res_num_col=1, res_name_col=2)

# Name the spins so they can be matched to the assignments.
spin.name(name='N')

# Define the isotope type.
spin.isotope('15N')

# The spectral data - spectrum ID, peak list file name, CPMG frequency (Hz), spectrometer frequency in Hertz.
data = [
    ['500_reference.in',    '500_MHz'+sep+'reference.in',           None,  500e6],
    ['500_66.667.in',       '500_MHz'+sep+'66.667.in',           66.6666,  500e6],
    ['500_133.33.in',       '500_MHz'+sep+'133.33.in',          133.3333,  500e6],
    ['500_133.33.in.bis',   '500_MHz'+sep+'133.33.in.bis',      133.3333,  500e6],
    ['500_200.in',          '500_MHz'+sep+'200.in',             200.0000,  500e6],
    ['500_266.67.in',       '500_MHz'+sep+'266.67.in',          266.6666,  500e6],
    ['500_333.33.in',       '500_MHz'+sep+'333.33.in',          333.3333,  500e6],
    ['500_400.in',          '500_MHz'+sep+'400.in',             400.0000,  500e6],
    ['500_466.67.in',       '500_MHz'+sep+'466.67.in',          466.6666,  500e6],
    ['500_533.33.in',       '500_MHz'+sep+'533.33.in',          533.3333,  500e6],
    ['500_533.33.in.bis',   '500_MHz'+sep+'533.33.in.bis',      533.3333,  500e6],
    ['500_600.in',          '500_MHz'+sep+'600.in',             600.0000,  500e6],
    ['500_666.67.in',       '500_MHz'+sep+'666.67.in',          666.6666,  500e6],
    ['500_733.33.in',       '500_MHz'+sep+'733.33.in',          733.3333,  500e6],
    ['500_800.in',          '500_MHz'+sep+'800.in',             800.0000,  500e6],
    ['500_866.67.in',       '500_MHz'+sep+'866.67.in',          866.6666,  500e6],
    ['500_933.33.in',       '500_MHz'+sep+'933.33.in',          933.3333,  500e6],
    ['500_933.33.in.bis',   '500_MHz'+sep+'933.33.in.bis',      933.3333,  500e6],
    ['500_1000.in',         '500_MHz'+sep+'1000.in',           1000.0000,  500e6],
    ['800_reference.in',    '800_MHz'+sep+'reference.in',           None,  800e6],
    ['800_66.667.in',       '800_MHz'+sep+'66.667.in',           66.6666,  800e6],
    ['800_133.33.in',       '800_MHz'+sep+'133.33.in',          133.3333,  800e6],
    ['800_133.33.in.bis',   '800_MHz'+sep+'133.33.in.bis',      133.3333,  800e6],
    ['800_200.in',          '800_MHz'+sep+'200.in',             200.0000,  800e6],
    ['800_266.67.in',       '800_MHz'+sep+'266.67.in',          266.6666,  800e6],
    ['800_333.33.in',       '800_MHz'+sep+'333.33.in',          333.3333,  800e6],
    ['800_400.in',          '800_MHz'+sep+'400.in',             400.0000,  800e6],
    ['800_466.67.in',       '800_MHz'+sep+'466.67.in',          466.6666,  800e6],
    ['800_533.33.in',       '800_MHz'+sep+'533.33.in',          533.3333,  800e6],
    ['800_533.33.in.bis',   '800_MHz'+sep+'533.33.in.bis',      533.3333,  800e6],
    ['800_600.in',          '800_MHz'+sep+'600.in',             600.0000,  800e6],
    ['800_666.67.in',       '800_MHz'+sep+'666.67.in',          666.6666,  800e6],
    ['800_733.33.in',       '800_MHz'+sep+'733.33.in',          733.3333,  800e6],
    ['800_800.in',          '800_MHz'+sep+'800.in',             800.0000,  800e6],
    ['800_866.67.in',       '800_MHz'+sep+'866.67.in',          866.6666,  800e6],
    ['800_933.33.in',       '800_MHz'+sep+'933.33.in',          933.3333,  800e6],
    ['800_933.33.in.bis',   '800_MHz'+sep+'933.33.in.bis',      933.3333,  800e6],
    ['800_1000.in',         '800_MHz'+sep+'1000.in',           1000.0000,  800e6]
]

# Loop over the spectra.
for id, file, cpmg_frq, H_frq in data:
    # Load the peak intensities.
    spectrum.read_intensities(file=file, dir='..', spectrum_id=id, int_method='height', int_col=2, res_num_col=1)

    # Set the relaxation dispersion experiment type.
    relax_disp.exp_type(spectrum_id=id, exp_type='SQ CPMG')

    # Set the relaxation dispersion CPMG frequencies.
    relax_disp.cpmg_setup(spectrum_id=id, cpmg_frq=cpmg_frq)

    # Set the NMR field strength of the spectrum.
    spectrometer.frequency(id=id, frq=H_frq)

    # Relaxation dispersion CPMG constant time delay T (in s).
    relax_disp.relax_time(spectrum_id=id, time=0.030)

# Specify the duplicated spectra.
spectrum.replicated(spectrum_ids=['500_133.33.in', '500_133.33.in.bis'])
spectrum.replicated(spectrum_ids=['500_533.33.in', '500_533.33.in.bis'])
spectrum.replicated(spectrum_ids=['500_933.33.in', '500_933.33.in.bis'])
spectrum.replicated(spectrum_ids=['800_133.33.in', '800_133.33.in.bis'])
spectrum.replicated(spectrum_ids=['800_533.33.in', '800_533.33.in.bis'])
spectrum.replicated(spectrum_ids=['800_933.33.in', '800_933.33.in.bis'])

# Deselect unresolved spins.
deselect.read(file='unresolved', dir='..'+sep+'500_MHz', res_num_col=1)
deselect.read(file='unresolved', dir='..'+sep+'800_MHz', res_num_col=1)


# Auto-analysis execution.
##########################

# Do not change!
Relax_disp(pipe_name=pipe_name, pipe_bundle=pipe_bundle, results_dir=RESULTS_DIR, models=MODELS, grid_inc=GRID_INC, mc_sim_num=MC_NUM, modsel=MODSEL, insignificance=INSIGNIFICANCE, numeric_only=NUMERIC_ONLY, eliminate=False)
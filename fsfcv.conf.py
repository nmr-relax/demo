###############################################################################
#                                                                             #
# Copyright (C) 2017 Edward d'Auvergne                                        #
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
"""Configuration file for the FSF Copyright Notice Validation script.

This configuration file uses the concept of a commit ID, which is generated as the first line of the commit message followed by the ISO date in brackets.
"""


# The significant number of new lines of code added.
SIG_CODE = 8

# The repository checkout copies, to allow for repository migrations, ordered by date from oldest to newest.
# The data consists of:
#       0 - The repository path.
#       1 - The repository type (either "svn" or "git").
#       2 - The start date.
#       3 - The end date.
#       4 - The optional HEAD directory for svn.
# Type:  list of [str, str, int, int, str or None]
REPOS = [
    [".", "git", 2017, 2050, None],
]

# README file creation variables, for appending copyright notices to README files.
README_APPEND_NOTICE = False
README_COMMITTER = "Edward d'Auvergne"

# The committer name translation table.
# This is for mapping the name in the copyright notice to the committers real name (e.g. handling non-ASCII characters, or different naming conventions).
# Desc:  The key is the internally consistent name and the value is the name of the committer in the repository.
# Type:  dict of str
COMMITTERS = {
    "Edward d'Auvergne": "Edward d'Auvergne",
}

# Alternative names for the committers.
# Desc:  The key is the alternative committer name in the copyright notice and the value is the name of the committer in the repository.
# Type:  dict of str
COMMITTER_ALT = {
}

# Blacklisted files to avoid checking.
# Type:  list of str
BLACKLISTED_FILES = [
]

# Directories to skip.
# Type:  list of str
DIR_SKIP = [
    '.git',
]

# Add some new mimetypes.
# Desc:  The list elements consist of the mimetype name and the file extension.
# Type:  list of [str, str]
NEW_MIMETYPES = [
]

# Specify binary mimetypes.
# Type:  list of str.
BINARY_MIMETYPES = [
]

# Binary files (for those without a mimetype or extension).
# Desc:  The values are the file names.
# Type:  list of str
BINARY_FILES = [
]

# Stop incorrect svn history by specifying the first commit key of a file (i.e. svn copy but then a complete file replacement).
# Desc:  The key is the file name and the value is the commit ID.
# Type:  dict of str
SVN_START = {
}

# Stop incorrect git history by specifying the first commit key of a misidentified file.
# Desc:  The key is the file name and the value is the commit ID.
# Type:  dict of str
GIT_START = {
    'R2/Ap4Aase/analysis/relax_fit.py':
        "Added pre-calculated relax results and logs for the Ap4Aase R2 relaxation curve-fitting analysis. (2017-09-14 09:11:52 +0200)",
}

# Additional copyright notices that are not present in the git log.
# Desc:  The key is the file and the value is a list of copyright statements.
# Type:  dict of list of str
ADDITIONAL_COPYRIGHT = {
}

# Additional copyright years and authors to add to the list.
# Desc:  The key is the file and the value is a list of lists of the year as an int and the author name as a string.
# Type:  dict of list of [int, str]
ADDITIONAL_COPYRIGHT_YEARS = {
    'NOE/Ap4Aase/Ap4Aase.seq':                                          [[2006, "Edward d'Auvergne"]],
    'NOE/Ap4Aase/ref_ave.list':                                         [[2006, "Edward d'Auvergne"]],
    'NOE/Ap4Aase/sat_ave.list':                                         [[2006, "Edward d'Auvergne"]],
    'NOE/Ap4Aase/unresolved':                                           [[2006, "Edward d'Auvergne"]],
    'NOE/Ap4Aase/analysis/noe.py':                                      [[[2004, 2005, 2008], "Edward d'Auvergne"]],
    'NOE/Ap4Aase/analysis/grace/grace2images.py':                       [[2013, "Troels E. Linnet"], [2013, "Edward d'Auvergne"]],
    'model_free/OMP/1F35_H.pdb':                                        [[2006, "Edward d'Auvergne"]],
    'model_free/OMP/rates.txt':                                         [[2006, "Edward d'Auvergne"]],
    'model_free/OMP/analysis/dauvergne_protocol.py':                    [[[2003, 2004, 2005, 2006, 2007, 2008, 2009, 2011, 2012], "Edward d'Auvergne"], [2008, "Sebastien Morin"]],
    'R2/Ap4Aase/Ap4Aase_new_3.pdb':                                     [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc11_ave.list':                                    [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc11b_ave.list':                                   [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc1_ave.list':                                     [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc1b_ave.list':                                    [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc2_ave.list':                                     [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc4_ave.list':                                     [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc4b_ave.list':                                    [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc6_ave.list':                                     [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc9_ave.list':                                     [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc9b_ave.list':                                    [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc1_ave.list':                                     [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/unresolved':                                            [[2006, "Edward d'Auvergne"]],
    'R2/Ap4Aase/analysis/relax_fit.py':                                 [[[2004, 2006, 2007, 2008], "Edward d'Auvergne"]],
    'R2/Ap4Aase/analysis/grace/grace2images.py':                        [[2013, "Troels E. Linnet"], [2013, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/1000.in':                                [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/133.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/133.33.in.bis':                          [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/200.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/266.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/333.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/400.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/466.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/533.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/533.33.in.bis':                          [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/600.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/66.667.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/666.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/733.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/800.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/866.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/933.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/933.33.in.bis':                          [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/reference.in':                           [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/500_MHz/unresolved':                             [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/1000.in':                                [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/133.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/133.33.in.bis':                          [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/200.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/266.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/333.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/400.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/466.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/533.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/533.33.in.bis':                          [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/600.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/66.667.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/666.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/733.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/800.in':                                 [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/866.67.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/933.33.in':                              [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/933.33.in.bis':                          [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/reference.in':                           [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/800_MHz/unresolved':                             [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/README':                                         [[2009, "Sebastien Morin"], [2013, "Edward d'Auvergne"]],
    'dispersion/Hansen/fake_sequence.in':                               [[2009, "Sebastien Morin"]],
    'dispersion/Hansen/load_data.py':                                   [[2013, "Edward d'Auvergne"]],
}

# False positives (copyright notices in files to ignore, as they are not in the git log).
# Desc:  The key is the file and the value is the list of copyright statements to ignore.
# Type:  dict of list of str
FALSE_POS = {
    'fsfcv.conf.py':                                                    ["Copyright (C) year1, year2, year3 copyright-holder"],
}

# False negatives (significant git log commits which do not imply copyright ownership).
# Desc:  The key is the file and the value is the copyright statement.
# Type:  dict of str
FALSE_NEG = {
}

# False negatives (significant git log commits which do not imply copyright ownership).
# Desc:  The key is the file and the value is a list of lists of the year as an int and the author name as a string.
# Type:  dict of list of [int, str]
FALSE_NEG_YEARS = {
    'NOE/Ap4Aase/Ap4Aase.seq':                                          [[2017, "Edward d'Auvergne"]],
    'NOE/Ap4Aase/ref_ave.list':                                         [[2017, "Edward d'Auvergne"]],
    'NOE/Ap4Aase/sat_ave.list':                                         [[2017, "Edward d'Auvergne"]],
    'NOE/Ap4Aase/unresolved':                                           [[2017, "Edward d'Auvergne"]],
    'model_free/OMP/1F35_H.pdb':                                        [[2017, "Edward d'Auvergne"]],
    'model_free/OMP/rates.txt':                                         [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/Ap4Aase_new_3.pdb':                                     [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc11_ave.list':                                    [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc11b_ave.list':                                   [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc1_ave.list':                                     [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc1b_ave.list':                                    [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc2_ave.list':                                     [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc4_ave.list':                                     [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc4b_ave.list':                                    [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc6_ave.list':                                     [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc9_ave.list':                                     [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc9b_ave.list':                                    [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/T2_ncyc1_ave.list':                                     [[2017, "Edward d'Auvergne"]],
    'R2/Ap4Aase/unresolved':                                            [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/1000.in':                                [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/133.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/133.33.in.bis':                          [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/200.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/266.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/333.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/400.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/466.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/533.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/533.33.in.bis':                          [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/600.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/66.667.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/666.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/733.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/800.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/866.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/933.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/933.33.in.bis':                          [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/reference.in':                           [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/500_MHz/unresolved':                             [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/1000.in':                                [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/133.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/133.33.in.bis':                          [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/200.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/266.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/333.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/400.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/466.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/533.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/533.33.in.bis':                          [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/600.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/66.667.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/666.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/733.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/800.in':                                 [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/866.67.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/933.33.in':                              [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/933.33.in.bis':                          [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/reference.in':                           [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/800_MHz/unresolved':                             [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/fake_sequence.in':                               [[2017, "Edward d'Auvergne"]],
    'dispersion/Hansen/load_data.py':                                   [[2017, "Edward d'Auvergne"]],
}

# Commits to exclude as a list of commit IDs.
# Desc:  The list items are the commit IDs.
# Type:  list of str
EXCLUDE = [
]

# Commits to switch authorship of (e.g. if someone commits someone else's code).
# The data consists of:
#       0 - The comitter's name.
#       1 - The real author.
#       2 - The commit key, consisting of the first line of the commit message followed by the ISO date in brackets.
# Type:  list of [str, str, str]
AUTHOR_SWITCH = [
]

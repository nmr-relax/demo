#!/usr/bin/env python3

###############################################################################
#                                                                             #
# Copyright (C) 2013 Troels E. Linnet                                         #
# Copyright (C) 2013,2017 Edward d'Auvergne                                   #
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

# Script docstring.
"""Scripted conversion of Grace *.agr graphs into vector or bitmap graphics files.

This script is used to batch convert the Grace *.agr files into graphics bitmap files using the Grace program itself.  Therefore you will need to install grace on your system using one of the programs:
    Xmgrace - http://plasma-gate.weizmann.ac.il/Grace/,
    qtgrace - http://sourceforge.net/projects/qtgrace/,
    gracegtk - http://sourceforge.net/projects/gracegtk/.
"""

# Python module imports.
from argparse import Action, ArgumentParser
import sys
from os import getcwd, listdir, path
import shlex, subprocess


# Define a callback class for handling the multiple input of PNG, EPS, SVG, etc.
class SplitFormats(Action):
     def __call__(self, parser, namespace, values, option_string=None):
         setattr(namespace, self.dest, values.split(','))


# Add script argument parsing.
parser = ArgumentParser(description="Scripted conversion of Grace *.agr graphs into vector or bitmap graphics files.")

# Add the script arguments.
parser.add_argument('types', action=SplitFormats, nargs='?', default='EPS', help="The different image types to convert to.  E.g. execute script with: %s -t JPG,EPS,SVG,PNG ..." % (sys.argv[0]))
parser.add_argument('-g', action='store_true', dest='relax_gui', default=False, help="Allow the script to be run through the relax GUI via the 'User-functions -> script' submenu, by only allowing for PNG conversions.")

# Parse the arguments.
args = parser.parse_args()

# If we run through the GUI we cannot pass input arguments so we fall back to EPS-only conversion.
if args.relax_gui:
    args.types = ['EPS']

# For PNG conversion, several parameters can be passed to xmgrace.  These can be altered later and the script rerun.
# The option for transparency is good for poster or insertion in color backgrounds.  This ability depends on the Grace compilation.
if "PNG" in args.types:
    pngpar = "png.par"
    if not path.isfile(pngpar):
        wpngpar = open(pngpar, "w")
        wpngpar.write("DEVICE \"PNG\" FONT ANTIALIASING on\n")
        wpngpar.write("DEVICE \"PNG\" OP \"transparent:off\"\n")
        wpngpar.write("DEVICE \"PNG\" OP \"compression:9\"\n")
        wpngpar.close()

# Convert the different possible graphics type options into Grace format.
types = []
text = []
ext = []
param = []
for type in args.types:
    # PNG bitmap graphics.
    if type in ["PNG", ".PNG", "png", ".png"]:
        types.append("PNG")
        text.append("portable network graphics (PNG)")
        ext.append("png")
        param.append(pngpar)

    # Encapsulated postscript vector graphics.
    elif type in ["EPS", ".EPS", "eps", ".eps"]:
        types.append("EPS")
        text.append("encapsulated postscript (EPS)")
        ext.append("eps")
        param.append(None)

    # JPG bitmap graphics.
    elif type in ["JPG", ".JPG", "jpg", ".jpg", "JPEG", ".JPEG", "jpeg", ".jpeg"]:
        types.append("JPEG")
        text.append("JPEG")
        ext.append("jpg")
        param.append(None)

    # Scalable vector graphics.
    elif type in ["SVG", ".SVG", "svg", ".svg"]:
        types.append("SVG")
        text.append("scalable vector graphics (SVG)")
        ext.append("svg")
        param.append(None)

    # Unknown graphic.
    else:
        print("Unknown graphic type '%s', skipping the format." % type)
        continue

# Loop over all files in the current directory.
for filename in listdir(getcwd()):
    # Skip non-Grace files.
    if not filename.endswith(".agr"):
        continue

    # Get the filename without extension.
    basename = path.splitext(filename)[0]

    # Loop over each output format.
    for i in range(len(types)):
        im_args = r"xmgrace -hdevice %s -hardcopy" % types[i]
        if param[i]:
            im_args += r" -param %s" % param[i]
        im_args += r" -printfile %s.%s %s" % (basename, ext[i], filename)

        # Split the arguments the right way to call xmgrace.
        im_args = shlex.split(im_args)

        # Generate the graphic.
        print("Converting '%s' into a %s graphic." % (filename, text[i]))
        return_code = subprocess.call(im_args)

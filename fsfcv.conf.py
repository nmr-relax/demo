#! /usr/bin/env python3

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

"""Recursively check all files for FSF copyright notice compliance.

This standard is from https://www.gnu.org/prep/maintain/html_node/Copyright-Notices.html, and
reproduced here for a permanent record:

6.5 Copyright Notices
=====================

You should maintain a proper copyright notice and a license notice in each nontrivial file in the
package. (Any file more than ten lines long is nontrivial for this purpose.) This includes header
files and interface definitions for building or running the program, documentation files, and any
supporting files. If a file has been explicitly placed in the public domain, then instead of a
copyright notice, it should have a notice saying explicitly that it is in the public domain.

Even image files and sound files should contain copyright notices and license notices, if their
format permits. Some formats do not have room for textual annotations; for these files, state the
copyright and copying permissions in a README file in the same directory.

Change log files should have a copyright notice and license notice at the end, since new material is
added at the beginning but the end remains the end.

When a file is automatically generated from some other file in the distribution, it is useful for
the automatic procedure to copy the copyright notice and permission notice of the file it is
generated from, if possible. Alternatively, put a notice at the beginning saying which file it is
generated from.

A copyright notice looks like this:

Copyright (C) year1, year2, year3 copyright-holder

The word 'Copyright' must always be in English, by international convention.

The copyright-holder may be the Free Software Foundation, Inc., or someone else; you should know who
is the copyright holder for your package.

Replace the '(C)' with a C-in-a-circle symbol if it is available. For example, use '@copyright{}' in
a Texinfo file. However, stick with parenthesized 'C' unless you know that C-in-a-circle will work.
For example, a program's standard --version message should use parenthesized 'C' by default, though
message translations may use C-in-a-circle in locales where that symbol is known to work.
Alternatively, the '(C)' or C-in-a-circle can be omitted entirely; the word 'Copyright' suffices.

To update the list of year numbers, add each year in which you have made nontrivial changes to the
package. (Here we assume you're using a publicly accessible revision control server, so that every
revision installed is also immediately and automatically published.) When you add the new year, it
is not required to keep track of which files have seen significant changes in the new year and which
have not. It is recommended and simpler to add the new year to all files in the package, and be done
with it for the rest of the year.

Don't delete old year numbers, though; they are significant since they indicate when older versions
might theoretically go into the public domain, if the movie companies don't continue buying laws to
further extend copyright. If you copy a file into the package from some other program, keep the
copyright years that come with the file.

You can use a range ('2008-2010') instead of listing individual years ('2008, 2009, 2010') if and
only if: 1) every year in the range, inclusive, really is a "copyrightable" year that would be
listed individually; and 2) you make an explicit statement in a README file about this usage.

For files which are regularly copied from another project (such as 'gnulib'), leave the copyright
notice as it is in the original.

The copyright statement may be split across multiple lines, both in source files and in any
generated output. This often happens for files with a long history, having many different years of
publication.

For an FSF-copyrighted package, if you have followed the procedures to obtain legal papers, each
file should have just one copyright holder: the Free Software Foundation, Inc. You should edit the
file's copyright notice to list that name and only that name.

But if contributors are not all assigning their copyrights to a single copyright holder, it can
easily happen that one file has several copyright holders. Each contributor of nontrivial text is a
copyright holder.

In that case, you should always include a copyright notice in the name of main copyright holder of
the file. You can also include copyright notices for other copyright holders as well, and this is a
good idea for those who have contributed a large amount and for those who specifically ask for
notices in their names. (Sometimes the license on code that you copy in may require preserving
certain copyright notices.) But you don't have to include a notice for everyone who contributed to
the file (which would be rather inconvenient).

Sometimes a program has an overall copyright notice that refers to the whole program. It might be in
the README file, or it might be displayed when the program starts up. This copyright notice should
mention the year of completion of the most recent major version; it can mention years of completion
of previous major versions, but that is optional.


SVN archive
===========

Both the svn and git histories for relax are incomplete.  For example the git repository finds
history within branches that the svn history misses.  And the git history is quite wrong for a
number of files.  Therefore both a svn repository and git repository should be used with this
script.

Firstly download the whole SVN archive repository with:

$ rsync -av --delete svn.code.sf.net::p/nmr-relax/code-svn-archive/ relax_sf_svn_repo

Then check out a local copy:

$ svn co file://$PWD/relax_sf_svn_repo/trunk relax_sf_svn_archive

Having a copy of the entire repository on a local hard disk allows this script to complete within a
reasonable time frame.
"""

# Python module imports.
import bz2
from datetime import date, datetime
import gzip
import mimetypes
from os import F_OK, access, getcwd, path, sep, walk
from pytz import utc
from re import search
from subprocess import PIPE, Popen
import sys


# Debugging modes.
DEBUG = False

# The significant number of new lines of code added.
SIG_CODE = 8

# The repository checkout copies, to allow for repository migrations, ordered by date from oldest to newest.
# The data consists of:
#       0 - The repository path.
#       1 - The repository type (either "svn" or "git").
#       2 - The start date.
#       3 - The end date.
#       4 - The optional HEAD directory for svn.
REPOS = [
    [".", "git", 2017, 2050, None],
]

# README file creation variables, for appending copyright notices to README files.
README_APPEND_NOTICE = False
README_COMMITTER = "Edward d'Auvergne"

# The committer name translation table.
COMMITTERS = {
    "Edward d'Auvergne": "Edward d'Auvergne",
}

# The svn committer name translation table.
SVN_COMMITTERS = {
}

# Alternative names for the committers.
COMMITTER_ALT = {
}

# Blacklisted files.
BLACKLISTED_FILES = [
]

# Directories to skip.
DIR_SKIP = [
    '.git',
]

# Add some new mimetypes.

# Binary mimetypes.
BINARY_MIMETYPES = [
]

# Binary files (for those without a mimetype or extension).
BINARY_FILES = [
]

# Stop incorrect svn history by specifying the first commit key of a file (i.e. svn copy but then a complete file replacement).
SVN_START = {
}

# Stop incorrect git history by specifying the first commit key of a misidentified file.
GIT_START = {
}

# Additional copyright notices that are not present in the git log.
ADDITIONAL_COPYRIGHT = {
}

# Additional copyright years and authors to add to the list.  The keys are lists of lists of the year as an int and the author name as a string.
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
}

# False positives (copyright notices in files to ignore, as they are not in the git log).
FALSE_POS = {
    'fsfcv.conf.py':                                                    ["Copyright (C) year1, year2, year3 copyright-holder"],
}

# False negatives (significant git log commits which do not imply copyright ownership).
FALSE_NEG = {
}
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
    'R2/Ap4Aase/analysis/relax_fit.py':                                 [[2017, "Edward d'Auvergne"]],
}

# Commits to exclude as a list of commit keys - the first line of the commit message followed by the ISO date in brackets.
EXCLUDE = [
]

# Commits to switch authorship of (e.g. if someone commits someone else's code).
# The data consists of:
#       0 - The comitter's name.
#       1 - The real author.
#       2 - The commit key, consisting of the first line of the commit message followed by the ISO date in brackets.
AUTHOR_SWITCH = [
]


def committer_info_cleanup(file_path, committer_info):
    """Clean up the committer info data structure.

    @param file_path:       The full file path.
    @type file_path:        str
    @param committer_info:  The committer info data structure, listing the committers and years of significant commits.  This is a dictionary with the committer's name as a key with the value as the list of years.
    @type committer_info:   dict of lists of str
    """

    # Remove committers with no commits.
    prune = []
    for committer in committer_info:
        if len(committer_info[committer]) == 0:
            prune.append(committer)
    for committer in prune:
        del committer_info[committer]


def determine_compression(file_path):
    """Function for determining the compression type, and for also testing if the file exists.

    @param file_path:   The full file path of the file.
    @type file_path:    str
    @return:            A tuple of the compression type and full path of the file (including its extension).  A value of 0 corresponds to no compression.  Bzip2 compression corresponds to a value of 1.  Gzip compression corresponds to a value of 2.
    @rtype:             (int, str)
    """

    # The file has been supplied without its compression extension.
    if access(file_path, F_OK):
        compress_type = 0
        if search('.bz2$', file_path):
            compress_type = 1
        elif search('.gz$', file_path):
            compress_type = 2

    # The file has been supplied with the '.bz2' extension.
    elif access(file_path + '.bz2', F_OK):
        file_path = file_path + '.bz2'
        compress_type = 1

    # The file has been supplied with the '.gz' extension.
    elif access(file_path + '.gz', F_OK):
        file_path = file_path + '.gz'
        compress_type = 2

    # Return the compression type.
    return compress_type, file_path


def extract_copyright(file_path):
    """Pull out all the copyright notices from the given file.

    @param file_path:   The full file path.
    @type file_path:    str
    @return:            The list of current copyright notices.
    @rtype:             list of str
    """

    # Read the file data.
    file = open_read_file(file_path)
    lines = file.readlines()
    file.close()

    # Loop over the file, finding the statements.
    statements = []
    for line in lines:
        if "Copyright (C)" in line:
            # Skip README file copyright notices for other files.
            if 'README' in file_path and search(": *Copyright \(C\)", line):
                continue

            # Skip copyright notices in this script.
            if 'copyright_notices.py' in file_path and search("\"", line):
                continue

            # Strip leading and trailing comment characters, and all whitespace.
            line = line.strip()
            if line[0] in ['#', '%', '*']:
                line = line[1:]
            if line[-1] in ['#', '%', '*']:
                line = line[:-2]
            if search("^rem", line):
                line = line[4:]
            line = line.strip()

            # Append the statement.
            statements.append(line)

    # Return the list of copyright statements.
    return statements


def extract_copyright_readme(file_name, root):
    """Try to extract copyright notice for the file from the README file.

    @param file_name:   The isolated file name to search for the copyright notice.
    @type file_name:    str
    @param root:        The file path root which should contain the README file.
    @type root:         str
    @return:            The list of current copyright notices.
    @rtype:             list of str
    """

    # Search for the README file.
    readme = root + sep + 'README'
    if not path.exists(readme):
        return []

    # Read the README file data.
    file = open(readme)
    lines = file.readlines()
    file.close()

    # Loop over the file, finding the statements.
    statements = []
    file_name = file_name.replace('+', '\+')
    for line in lines:
        if search("^%s: " % file_name, line) and "Copyright (C)" in line:
            statements.append(line[line.index("Copyright"):].strip())

    # Return the list of copyright statements.
    return statements


def extract_public_domain_readme(file_name, root):
    """Try to extract public domain information for the file from the README file.

    @param file_name:   The isolated file name to search for the public domain notice.
    @type file_name:    str
    @param root:        The file path root which should contain the README file.
    @type root:         str
    @return:            True if the file is stated as public domain, False otherwise.
    @rtype:             bool
    """

    # Search for the README file.
    readme = root + sep + 'README'
    if not path.exists(readme):
        return []

    # Read the README file data.
    file = open(readme)
    lines = file.readlines()
    file.close()

    # Loop over the file, finding the statements.
    file_name = file_name.replace('+', '\+')
    for line in lines:
        if search("^%s: " % file_name, line) and "Public domain" in line:
            return True

    # Not public domain.
    return False


def format_copyright(committer_info):
    """Convert the committer and year data structure into copyright statements.

    @param committer_info:  The committer info data structure, listing the committers and years of significant commits.  This is a dictionary with the committer's name as a key with the value as the list of years.
    @type committer_info:   dict of lists of str
    @return:                The ordered list of copyright statements.
    @rtype:                 list of str
    """

    # Init.
    statements = []

    # Loop over each committer.
    for committer in committer_info:
        # Format the year string.
        years = format_years(committer_info[committer])

        # Format the copyright statement.
        statements.append("Copyright (C) %s %s" % (years, committer))

    # Return the list of copyright statements.
    return statements


def format_years(years):
    """Format the given list of years for the copyright string.

    @param years:   The unordered list of years.
    @type years:    list of str
    """

    # Convert the years to ints and sort the list.
    dates = []
    for i in range(len(years)):
        dates.append(int(years[i]))
    dates.sort()

    # Split the dates into ranges.
    date_ranges = [[dates[0]]]
    for i in range(1, len(dates)):
        if dates[i]-1 == date_ranges[-1][-1]:
            date_ranges[-1].append(dates[i])
        else:
            date_ranges.append([dates[i]])

    # String format the ranges.
    year_string = ''
    for i in range(len(date_ranges)):
        # Range separator required.
        if len(year_string):
            year_string += ','

        # A single year.
        if len(date_ranges[i]) == 1:
            year_string += '%s' % date_ranges[i][0]

        # A range.
        else:
            year_string += '%s-%s' % (date_ranges[i][0], date_ranges[i][-1])

    # Return the formatted string.
    return year_string


def git_log_data(file_path, repo_path=None, exclude=[], start_commit=[], author_switch=[], committer_info={}, after=None, before=None, init=False):
    """Get the committers and years of significant commits from the git log.

    @param file_path:           The full file path to obtain the git info for.
    @type file_path:            str
    @keyword repo_path:         The path to the local copy of the git repository.
    @type repo_path:            str
    @keyword exclude:           A list of commit keys to exclude from the search.  The commit key consists of the first line of the commit message followed by the ISO date in brackets.
    @type exclude:              list of str
    @keyword start_commit:      The starting commit for each file, where 'git log' identifies an incorrect history path.  This is a dictionary with the keys being the file paths and the values being the commit keys (the first line of the commit message followed by the ISO date in brackets).
    @type start_commit:         dict of str
    @keyword author_switch:     List of commit keys and authors to switch the authorship of.  The first element should be the comitter, the second the real comitter, and the third the commit key.  The commit key consists of the first line of the commit message followed by the ISO date in brackets.
    @type author_switch:        list of list of str
    @keyword committer_info:    The committer info data structure, listing the committers and years of significant commits.  This is a dictionary with the committer's name as a key with the value as the list of years.
    @type committer_info:       dict of lists of str
    @keyword after:             Show commits more recent than a specific date.
    @type after:                int or None
    @keyword before:            Show commits older than a specific date.
    @type before:               int or None
    @keyword init:              A flag which if True means that the current repository is the starting repository.
    @type init:                 bool
    """

    # File check.
    full_path = "%s%s%s" % (repo_path, sep, file_path)
    if not path.exists(full_path):
        sys.stderr.write("Warning, file missing from git: %s\n" % full_path)
        return

    # Date restrictions.
    after_opt = ''
    before_opt = ''
    if after:
        after_opt = '--after=%i-01-01' % after
    if before:
        before_opt = '--before=%i-12-31' % before

    # Exec.
    pipe = Popen("git log %s %s --numstat --follow --pretty='%%an Ø %%ad Ø %%H Ø %%s' --date=iso \"%s\"" % (after_opt, before_opt, full_path), shell=True, stdout=PIPE, close_fds=False)

    # Get the data.
    lines = pipe.stdout.readlines()
    i = 0
    committer = None
    commit_key = ''
    history_stop = False
    while 1:
        # Termination.
        if i >= len(lines):
            break
        if file_path in start_commit and start_commit[file_path] == commit_key:
            history_stop = True
            if DEBUG:
                sys.stderr.write("  Git:  Terminating to stop false history.  Commit by '%s': %s\n" % (committer, commit_key))
            break

        # Obtain the committer and date info.
        committer, date, commit_hash, subject = lines[i].decode().split(' Ø ')
        year = int(date.split('-')[0])
        commit_key = "%s (%s)" % (subject.strip(), date)

        # Translate the committer name, if necessary.
        committer = translate_committer_name(committer)

        # The next line is a committer, so skip the current line.
        if search(' Ø ', lines[i+1].decode()):
            i += 1
            continue

        # Author switch.
        for j in range(len(author_switch)):
            if author_switch[j][2] == commit_key:
                committer = translate_committer_name(author_switch[j][1])

        # Commits to exclude.
        if commit_key in exclude:
            if DEBUG:
                sys.stderr.write("  Git:  Excluded commit by '%s': %s\n" % (committer, commit_key))
            i += 3
            continue

        # The numstat info.
        newlines = lines[i+2].decode().split()[0]
        if newlines == '-':
            newlines = 1e10
        else:
            newlines = int(newlines)

        # Not significant.
        if newlines < SIG_CODE:
            if DEBUG:
                sys.stderr.write("  Git:  Not significant by '%s': %s\n" % (committer, commit_key))
            i += 3
            continue

        # Skip svnmerge.py merges for svn->git migration repositories as these do not imply copyright ownership for the comitter.
        if search("^Merged revisions .* via svnmerge from", subject):
            if DEBUG:
                sys.stderr.write("  Git:  Skipping svnmerge.py migrated commit: %s\n" % commit_key)
            i += 3
            continue

        # Debugging printout.
        if DEBUG:
            sys.stderr.write("  Git:  Commit by '%s': %s\n" % (committer, commit_key))

        # Date already exists.
        if committer in committer_info and year in committer_info[committer]:
            i += 3
            continue

        # A new committer.
        if committer not in committer_info:
            committer_info[committer] = []

        # Store the info.
        committer_info[committer].append(year)

        # Increment the index.
        i += 3

    # Add committer info if the history was stopped, and no such info exists.
    if history_stop and committer and committer not in committer_info:
        committer_info[committer] = []
        committer_info[committer].append(year)

    # Always include the very first commit.
    if init:
        if committer and committer not in committer_info:
            committer_info[committer] = []
        if committer and year not in committer_info[committer]:
            committer_info[committer].append(year)


def open_read_file(file_name=None):
    """Open the file 'file' and return all the data.

    @keyword file_name: The name of the file to extract the data from.
    @type file_name:    str
    @return:            The open file object.
    @rtype:             file object
    """

    # Test if the file exists and determine the compression type.
    compress_type, file_path = determine_compression(file_name)

    # Open the file for reading.
    try:
        # Uncompressed text.
        if compress_type == 0:
            file_obj = open(file_path, 'r')

        # Bzip2 compressed text.
        elif compress_type == 1:
            file_obj = bz2.open(file_path, 't')

        # Gzipped compressed text.
        elif compress_type == 2:
            file_obj = gzip.open(file_path, 'rt')

    # Cannot open.
    except IOError:
        message = sys.exc_info()[1]
        raise NameError("Cannot open the file %s.  %s." % (file_path, message.args[1]))

    # Return the opened file.
    return file_obj


def readme_add_notice(file_name=None, file=None, notices=[]):
    """Add all copyright notices to the README file.

    @param file_name:   The isolated file name to add a copyright notice for.
    @type file_name:    str
    @keyword file:      The full README file path.
    @type file:         str
    @keyword notices:   The list of current copyright notices.
    @type notices:      list of str
    """

    # Append to the file.
    readme = open(file, 'a')

    # Loop over the notices.
    for notice in notices:
        readme.write("%-87s %s\n" % (("%s:" % file_name), notice))


def readme_setup(file=None):
    """Prepare the README file for appending copyright notices.

    @keyword file:  The full README file path.
    @type file:     str
    """

    # Create a new file.
    if not path.exists(file):
        # Open the file.
        readme = open(file, 'w')

        # Add a copyright notice.
        now = datetime.now()
        readme.write("###############################################################################\n")
        readme.write("#                                                                             #\n")
        readme.write("# Copyright (C) %i %-56s #\n" % (now.year, README_COMMITTER))
        readme.write("#                                                                             #\n")
        readme.write("# This file is part of the program relax (http://www.nmr-relax.com).          #\n")
        readme.write("#                                                                             #\n")
        readme.write("# This program is free software: you can redistribute it and/or modify        #\n")
        readme.write("# it under the terms of the GNU General Public License as published by        #\n")
        readme.write("# the Free Software Foundation, either version 3 of the License, or           #\n")
        readme.write("# (at your option) any later version.                                         #\n")
        readme.write("#                                                                             #\n")
        readme.write("# This program is distributed in the hope that it will be useful,             #\n")
        readme.write("# but WITHOUT ANY WARRANTY; without even the implied warranty of              #\n")
        readme.write("# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #\n")
        readme.write("# GNU General Public License for more details.                                #\n")
        readme.write("#                                                                             #\n")
        readme.write("# You should have received a copy of the GNU General Public License           #\n")
        readme.write("# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #\n")
        readme.write("#                                                                             #\n")
        readme.write("###############################################################################\n\n\n")

        # Close the file.
        readme.close()

    # Add the licencing section.
    readme = open(file)
    lines = readme.readlines()
    section = False
    for line in lines:
        if line == "Licensing\n":
            section = True
            break
    if not section:
        readme = open(file, 'a')
        readme.write("Licensing\n")
        readme.write("=========\n\n")
        readme.write("These files are licensed under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version:\n\n")
        readme.close()


def svn_log_data(file_path, repo_path=None, exclude=[], start_commit=[], author_switch=[], svn_head=None, committer_info={}, after=None, before=None, init=False):
    """Get the committers and years of significant commits from the svn log.

    @param file_path:           The full file path to obtain the git info for.
    @type file_path:            str
    @keyword repo_path:         The path to the local copy of the svn repository.
    @type repo_path:            str
    @keyword exclude:           A list of commit keys to exclude from the search.  The commit key consists of the first line of the commit message followed by the ISO date in brackets.
    @type exclude:              list of str
    @keyword start_commit:      The starting commit for each file to exclude incorrectly labelled history (i.e. a svn copy followed by complete file replacement).  This is a dictionary with the keys being the file paths and the values being the commit keys (the first line of the commit message followed by the ISO date in brackets).
    @type start_commit:         dict of str
    @keyword author_switch:     List of commit keys and authors to switch the authorship of.  The first element should be the comitter, the second the real comitter, and the third the commit key.  The commit key consists of the first line of the commit message followed by the ISO date in brackets.
    @type author_switch:        list of list of str
    @keyword svn_head:          The HEAD directory, e.g. "trunk".
    @type svn_head:             str
    @keyword committer_info:    The committer info data structure, listing the committers and years of significant commits.  This is a dictionary with the committer's name as a key with the value as the list of years.
    @type committer_info:       dict of lists of str
    @keyword after:             Show commits more recent than a specific date.
    @type after:                int or None
    @keyword before:            Show commits older than a specific date.
    @type before:               int or None
    @keyword init:              A flag which if True means that the current repository is the starting repository.
    @type init:                 bool
    """

    # File check.
    full_path = "%s%s%s%s%s" % (repo_path, sep, svn_head, sep, file_path)
    if "://" not in full_path and not path.exists(full_path):
        sys.stderr.write("Warning, file missing from svn: %s\n" % full_path)
        return

    # Date restrictions.
    date_range = ''
    if after or before:
        date_range += "-r"
    if before:
        date_range += '{%i-12-31}:' % before
    else:
        date_range += '{3000-01-01}:'
    if after:
        date_range += '{%i-01-01}' % after
    else:
        date_range += '{1000-01-01}'

    # Exec.
    pipe = Popen("svn log --diff %s \"%s\"" % (date_range, full_path), shell=True, stdout=PIPE, close_fds=False)

    # Get the data.
    lines = pipe.stdout.readlines()
    for i in range(len(lines)):
        try:
            lines[i] = lines[i].decode()[:-1]
        except UnicodeError:
            # Catch the ascii character 43 ("+").
            if lines[i][0] == 43:
                lines[i] = "+binary diff"
            else:
                lines[i] = ""
    i = 0
    committer = None
    commit_key = ''
    history_stop = False
    while 1:
        # Termination.
        if i >= len(lines)-1:
            break
        if file_path in start_commit and start_commit[file_path] == commit_key:
            history_stop = True
            if DEBUG:
                sys.stderr.write("  SVN:  Terminating to stop false history.  Commit by '%s': %s\n" % (committer, commit_key))
            break

        # A new commit.
        if search('^------------------------------------------------------------------------$', lines[i]) and lines[i+1][0] == 'r':
            # Move to the summary line.
            i += 1

            # Extract the committer and year.
            rev, svn_committer, date, length = lines[i].split(' | ')
            committer = SVN_COMMITTERS[svn_committer]
            year = int(date.split()[0].split('-')[0])
            date = date.split(" (")[0]
            date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z')
            date = date.astimezone(tz=utc)

            # Translate the committer name, if necessary.
            committer = translate_committer_name(committer)

            # Find the diff.
            in_diff = False
            newlines = 0
            msg = ""
            msg_flag = True
            while 1:
                # Walk down the lines.
                i += 1

                # Store the first line of the commit message.
                if msg_flag and search("^[A-Za-z]", lines[i]):
                    # Store the line.
                    msg += lines[i]
                    msg_flag = False

                    # Search for additional first lines.
                    while 1:
                        # Walk down the lines.
                        i += 1

                        # Termination.
                        if not len(lines[i]):
                            break

                        # Add the line.
                        else:
                            msg += " %s" % lines[i]

                # End of the diff.
                if i >= len(lines):
                    break
                if search('^------------------------------------------------------------------------$', lines[i]) and i < len(lines)-1 and len(lines[i+1]) and lines[i+1][0] == 'r':
                    break

                # Inside the diff.
                if search('^===================================================================$', lines[i]):
                    in_diff = True
                    i += 1
                if not in_diff:
                    continue

                # Binary diff.
                if "Cannot display: file marked as a binary type." in lines[i]:
                    newlines = 1000000
                    break

                # Count the added lines.
                if len(lines[i]) and lines[i][0] == "+" and lines[i][0:3] != "+++":
                    newlines += 1

            # Create the commit key.
            commit_key = "%s (%s +0000)" % (msg.strip(), date.strftime("%Y-%m-%d %H:%M:%S"))

        # Not a new commit.
        else:
            i += 1
            continue

        # Author switch.
        for j in range(len(author_switch)):
            if author_switch[j][2] == commit_key:
                committer = translate_committer_name(author_switch[j][1])

        # Commits to exclude.
        if commit_key in exclude:
            if DEBUG:
                sys.stderr.write("  SVN:  Excluded commit by '%s': %s\n" % (committer, commit_key))
            continue

        # No diff found.
        if not in_diff:
            if DEBUG:
                sys.stderr.write("  SVN:  No diff found by '%s': %s\n" % (committer, commit_key))
            continue

        # Not significant.
        if newlines < SIG_CODE:
            if DEBUG:
                sys.stderr.write("  SVN:  Not significant by '%s': %s\n" % (committer, commit_key))
            continue

        # Date already exists.
        if committer in committer_info and year in committer_info[committer]:
            continue

        # Skip svnmerge commits.
        if search("^Merged revisions .* via svnmerge from", msg):
            if DEBUG:
                sys.stderr.write("  SVN:  Skipping svnmerge.py migrated commit: %s\n" % commit_key)
            continue

        # Debugging printout.
        if DEBUG:
            sys.stderr.write("  SVN:  Commit by '%s': %s\n" % (committer, commit_key))

        # A new committer.
        if committer not in committer_info:
            committer_info[committer] = []

        # Store the info.
        committer_info[committer].append(year)

    # Add committer info if the history was stopped, and no such info exists.
    if history_stop and committer and committer not in committer_info:
        committer_info[committer] = []
        committer_info[committer].append(year)

    # Always include the very first commit.
    if init:
        if committer and committer not in committer_info:
            committer_info[committer] = []
        if committer and year not in committer_info[committer]:
            committer_info[committer].append(year)


def translate_committer_name(committer):
    """Translate the committer name, if necessary.

    @param committer:   The committer name to translate.
    @type committer:    str
    @return:            The translated name.
    @rtype:             str
    """

    # The name is in the translation table.
    if committer in COMMITTERS:
        return COMMITTERS[committer]

    # Or not.
    return committer


def validate_copyright(expected_copyright, recorded_copyright):
    """Check if the expected and recorded copyrights match.

    @param expected_copyright:  The unsorted list of expected copyright notices.
    @type expected_copyright:   list of str
    @param recorded_copyright:  The unsorted list of recorded copyright notices.
    @type recorded_copyright:   list of str
    @return:                    True if the copyright notices match, False otherwise.
    @rtype:                     bool
    """

    # Sort the lists.
    expected_copyright.sort()
    recorded_copyright.sort()

    # Replace alternative names in the recorded list.
    for i in range(len(recorded_copyright)):
        for alt in COMMITTER_ALT:
            if search(alt, recorded_copyright[i]):
                recorded_copyright[i] = recorded_copyright[i].replace(alt, COMMITTER_ALT[alt])

    # Compare the lists.
    if expected_copyright == recorded_copyright:
        return True
    return False


def validate_readme(root):
    """Check the validity of the copyright notices in the README file.

    @param root:    The path which should contain the README file.
    @type root:     str
    """

    # Search for the README file.
    if root[-1] == sep:
        readme = root + 'README'
    else:
        readme = root + sep + 'README'
    if not path.exists(readme):
        return

    # Printout.
    sys.stdout.write("Validating: %s\n" % readme)

    # Read the README file data.
    file = open(readme)
    lines = file.readlines()
    file.close()

    # Loop over the file, finding the statements.
    missing = []
    for line in lines:
        if search(": *Copyright \(C\)", line):
            # Strip out the file.
            file_name = line.split(':')[0]

            # Check if the file exists.
            file_path = root + sep + file_name
            if not path.exists(file_path):
                missing.append(file_path)

    # Errors.
    if missing:
        sys.stderr.write("Missing files with copyright notices:\n")
        for i in range(len(missing)):
            sys.stderr.write("    %s\n" % missing[i])



# Execute the script.
if __name__ == '__main__':
    # The path to search.
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        directory = getcwd()

    # Handle files as arguments.
    file_arg = None
    if path.isfile(directory):
        directory, file_arg = path.split(directory)

    # Initial printout.
    if file_arg:
        sys.stdout.write("\nFSF copyright notice compliance checking for the file '%s%s%s'.\n\n" % (directory, sep, file_arg))
    else:
        sys.stdout.write("\nFSF copyright notice compliance checking for the directory '%s'.\n\n" % directory)
    sys.stdout.flush()

    # Counters.
    files_total = 0
    files_blacklisted = 0
    files_untracked = 0
    files_valid = 0
    files_nonvalid = 0

    # Walk through the current dir, alphabetically.
    for root, dirs, files in walk(directory):
        dirs.sort()

        # Single file argument.
        if file_arg and directory != root:
            continue

        # Directory skip.
        skip = False
        for name in DIR_SKIP:
            if name in root:
                skip = True
                break
        if skip:
            continue

        # Validate any copyright statements in the README file, if present.
        validate_readme(root)

        # Loop over the files.
        files.sort()
        for file_name in files:
            # Command line argument supplied file.
            if file_arg and file_name != file_arg:
                continue

            # Count the file.
            files_total += 1

            # Full path to the file.
            if root[-1] == sep:
                file_path = root + file_name
            else:
                file_path = root + sep + file_name

            # Strip any './' characters from the start.
            if len(file_path) >= 2 and file_path[:2] == './':
                file_path = file_path[2:]

            # Blacklisted file.
            if file_path in BLACKLISTED_FILES:
                files_blacklisted += 1
                continue

            # Check for untracked files.
            if REPOS[-1][1] == 'git':
                pipe = Popen("git ls-files \"%s\" --error-unmatch; echo $?" % file_path, shell=True, stderr=PIPE, stdout=PIPE, close_fds=False)
            else:
                pipe = Popen("svn info \"%s/%s/%s\"" % (REPOS[-1][0], REPOS[-1][4], file_path), shell=True, stderr=PIPE, stdout=PIPE, close_fds=False)
            err = pipe.stderr.readlines()
            if err:
                sys.stdout.write("Untracked file: %s (mimetype = '%s')\n" % (file_path, type))
                sys.stdout.flush()
                files_untracked += 1
                continue

            # Determine the file type.
            type, encoding = mimetypes.guess_type(file_path)
            sys.stdout.write("Checking: %s (mimetype = '%s')\n" % (file_path, type))
            sys.stdout.flush()

            # Public domain files.
            if extract_public_domain_readme(file_name, root):
                files_valid += 1
                continue

            # Get the committer and year information from the repository logs.
            committer_info = {}
            init = True
            for repo_path, repo_type, repo_start, repo_end, repo_head in REPOS:
                if repo_type == 'git':
                    git_log_data(file_path, repo_path=repo_path, exclude=EXCLUDE, start_commit=GIT_START, author_switch=AUTHOR_SWITCH, committer_info=committer_info, after=repo_start, before=repo_end, init=init)
                else:
                    svn_log_data(file_path, repo_path=repo_path, exclude=EXCLUDE, start_commit=SVN_START, author_switch=AUTHOR_SWITCH, svn_head=repo_head, committer_info=committer_info, after=repo_start, before=repo_end, init=init)
                init = False
            committer_info_cleanup(file_path, committer_info)

            # Add any additional committer years.
            if file_path in ADDITIONAL_COPYRIGHT_YEARS:
                for years, committer in ADDITIONAL_COPYRIGHT_YEARS[file_path]:
                    if not committer in committer_info:
                        committer_info[committer] = []
                    if isinstance(years, int):
                        years = [years]
                    for year in years:
                        if year not in committer_info[committer]:
                            committer_info[committer].append(year)

            # Remove false negative years.
            if file_path in FALSE_NEG_YEARS:
                for year, committer in FALSE_NEG_YEARS[file_path]:
                    if committer in committer_info and year in committer_info[committer]:
                        committer_info[committer].pop(committer_info[committer].index(year))
                        if not len(committer_info[committer]):
                            del committer_info[committer]

            # Format the data as copyright statements.
            expected_copyright = format_copyright(committer_info)

            # Search for missing copyright notices in local README files.
            recorded_copyright = extract_copyright_readme(file_name, root)

            # Otherwise parse text files for the current copyright statements.
            if not len(recorded_copyright) and type not in BINARY_MIMETYPES and file_path not in BINARY_FILES:
                recorded_copyright = extract_copyright(file_path)

            # Add any additional copyright notices.
            if file_path in ADDITIONAL_COPYRIGHT:
                for notice in ADDITIONAL_COPYRIGHT[file_path]:
                    expected_copyright.append(notice)

            # Remove false positives and negatives.
            if file_path in FALSE_POS:
                for i in range(len(FALSE_POS[file_path])):
                    for j in reversed(range(len(recorded_copyright))):
                        if FALSE_POS[file_path][i] in recorded_copyright[j]:
                            recorded_copyright.pop(j)
            if file_path in FALSE_NEG:
                for i in range(len(FALSE_NEG[file_path])):
                    for j in reversed(range(len(expected_copyright))):
                        if FALSE_NEG[file_path][i] in expected_copyright[j]:
                            expected_copyright.pop(j)

            # Validate.
            if validate_copyright(expected_copyright, recorded_copyright):
                files_valid += 1
                continue

            # README file copyright notice addition.
            if README_APPEND_NOTICE:
                # Prepare the README file, if necessary.
                readme = root + sep + 'README'
                readme_setup(file=readme)

                # Add the copyright.
                readme_add_notice(file_name=file_name, file=readme, notices=expected_copyright)

                # Skip the failure printout.
                files_valid += 1
                continue

            # A non-valid file.
            files_nonvalid += 1

            # Failure printout.
            sys.stderr.write("File: '%s'\n" % file_path)
            sys.stderr.write("Expected non-matching copyrights:\n")
            for i in range(len(expected_copyright)):
                if expected_copyright[i] not in recorded_copyright:
                    sys.stderr.write("    %s\n" % expected_copyright[i])
            sys.stderr.write("Recorded non-matching copyrights:\n")
            for i in range(len(recorded_copyright)):
                if recorded_copyright[i] not in expected_copyright:
                    sys.stderr.write("    %s\n" % recorded_copyright[i])
            sys.stderr.write("\n")
            sys.stderr.flush()

    # Final printout.
    sys.stdout.write("\n\nStatistics:\n\n")
    sys.stdout.write("    %-35s %8i\n" % ("All files:", files_total))
    sys.stdout.write("    %-35s %8i\n" % ("Blacklisted files:", files_blacklisted))
    sys.stdout.write("    %-35s %8i\n" % ("Untracked files:", files_untracked))
    sys.stdout.write("\n")
    sys.stdout.write("    %-35s %8i\n" % ("Validated file count:", files_valid+files_nonvalid))
    sys.stdout.write("    %-35s %8i\n" % ("Non-matching copyright notices:", files_nonvalid))

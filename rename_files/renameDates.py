#! python3
# renameDates.py - Renames filenames with American MM-DD-YY date format
# to European DD-MM-YYYY

import shutil, os, re 

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)((0|1)?\d)-
                                ((0|1|2|3)?\d)-
                                ((19|20)\d\d)-
                                (.*?)$
                                """, re.VERBOSE)


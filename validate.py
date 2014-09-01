"""Validates HTML5 pages.

     Authors: Sven Kreiss and contributors
     License: MIT
Project page: https://github.com/svenkreiss/travisci_html5/

"""

__version__ = "0.1.0"

import os
import sys
import fnmatch
import subprocess


def all_html_files(directory='.', match='*.html', blacklist=['.git', 'vnu', 'reference_manual_html']):
    files = []
    for root, dirnames, filenames in os.walk(directory):
        for b in blacklist:
            if b in dirnames:
                dirnames.remove(b)
        for filename in fnmatch.filter(filenames, match):
            files.append(os.path.join(root, filename))
    return files


def main(errors_only=True):
    opts = []
    if errors_only:
        opts.append('--errors-only')
    files = all_html_files()
    try:
        subprocess.check_output(['java', '-jar', 'vnu/vnu.jar']+opts+files)
    except subprocess.CalledProcessError:
        print '===> Not HTML5 compatible.'
        sys.exit(1)

if __name__ == "__main__":
    main()


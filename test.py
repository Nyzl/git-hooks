#!/usr/local/bin/python3
"""
This is a git commit-hook which can be used to check if huge files
 where accidentally added to the staging area and are about to be
 committed.
If there is a file which is bigger then the given "max_file_size"-
 variable, the script will exit non-zero and abort the commit.
This script is meant to be added as a "pre-commit"-hook. See this
 page for further information:
    http://progit.org/book/ch7-3.html#installing_a_hook
In order to make the script work probably, you'll need to set the
 above path to the python interpreter (first line of the file)
 according to your system (under *NIX do "which python" to find out).
Also, the "git_binary_path"-variable should contain the absolute
 path to your "git"-executable (you can use "which" here, too).
See the included README-file for further information.
The script was developed and has been confirmed to work under
 python 3.2.2 and git 1.7.7.1 (might also work with earlier versions!)
"""

# The maximum file-size for a file to be committed:
max_file_size = 512 # in KB (= 1024 byte)
# The path to the git-binary:
git_binary_path = "/usr/bin/git"

# ---- DON'T CHANGE THE REST UNLESS YOU KNOW WHAT YOU'RE DOING! ----

import subprocess, sys, os, re, argparse

BLACKLIST = [
    b'BEGIN RSA PRIVATE KEY',
    b'BEGIN DSA PRIVATE KEY',
    b'BEGIN EC PRIVATE KEY',
    b'BEGIN OPENSSH PRIVATE KEY',
    b'BEGIN PRIVATE KEY',
    b'PuTTY-User-Key-File-2',
    b'BEGIN SSH2 ENCRYPTED PRIVATE KEY',
    b'BEGIN PGP PRIVATE KEY BLOCK',
]

file = ["creds/dummy-creds"]

def detect_private_key():

    private_key_files = []

    for filename in file:
        with open(filename, 'rb') as f:
            content = f.read()
            if any(line in content for line in BLACKLIST):
                private_key_files.append(filename)

    if private_key_files:
        for private_key_file in private_key_files:
            print('Private key found: {}'.format(private_key_file))
            sys.exit(1)
        
    else:
        #return 0
        print ('all ok')

detect_private_key()

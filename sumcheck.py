#!/usr/bin/env python
import subprocess
import sys
import random
from os.path import isfile, join
import os
import hashlib
from argparse import ArgumentParser as ap

checksumlist = {}
hasherclass = hashlib.sha1
BLOCKSIZE = 16384

emptysums = [
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "d41d8cd98f00b204e9800998ecf8427e",
    "da39a3ee5e6b4b0d3255bfef95601890afd80709"
]

parser = ap(description = "List all files in a given location that have the same checksum.",
            epilog = """Copyright 2016 Eero Leno. This software is licensed \
                           under the MIT license.""")

parser.add_argument("directory",
                   nargs = "?", # not required
                   type = str,
                   help = "The location in where to look"
                   )

parser.add_argument("--recursive", "-r",
                   required = False,
                   action = "store_true",
                   help = "Traverse subdirectories"
                   )

parser.add_argument("--all", "-a",
                   required = False,
                   action = "store_true",
                   help = "Show all files (ignores empty files by default)"
                   )

parser.add_argument("--hash",
                   required = False,
                   type = str,
                   choices = ["md5", "sha1", "sha256"],
                   help = "Hash function to be used, default is sha1"
                   )

args = parser.parse_args()

if args.hash == "md5":
    hasherclass = hashlib.md5
elif args.hash == "sha1":
    hasherclass = hashlib.sha1
elif args.hash == "sha256":
    hasherclass = hashlib.sha256

bcolors = [
    '\033[95m',
    '\033[94m',
    '\033[92m',
    '\033[93m',
    '\033[91m',
    '\033[0m'
]

def randomColor(last):
    current = last
    while current == last:
        current = bcolors[random.randint(0, len(bcolors) - 1)]
    return current

def getHash(path):
    hasher = hasherclass()
    with open(path, "rb") as hashfile:
        buffer = hashfile.read(BLOCKSIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = hashfile.read(BLOCKSIZE)
        return hasher.hexdigest()

def getFiles(dir=False, recursive=False):
    found = []
    if not dir:
        dir = os.getcwd()
    if recursive:
        for root, directories, files in os.walk(dir):
            for file in files:
                found.append(join(root, file))
    else:
        for file in os.listdir(dir):
            if isfile(join(dir, file)):
                found.append(join(dir, file))
    return found

def addFile(path):
    md = getHash(path)
    if md in checksumlist:
        # For some reason python won't compute this with one line
        currList = checksumlist[md]
        currList.append(path)
        checksumlist[md] = currList
    else:
        checksumlist[md] = [ path ]

files = getFiles(dir=args.directory, recursive=args.recursive)

indexed = 0
total = len(files)

print("Indexing files, this may take a while...")

for file in files:
    addFile(file)
    indexed += 1
    print(indexed, "files indexed out of", total, "   \r", end="")

print("")

lastColor = ""

for key, value in checksumlist.items():
    if len(value) > 1:
        if key not in emptysums or args.all:
            currColor = randomColor(lastColor)
            for path in value:
                print(currColor, key[:6], "\t ", path)
            print("")

print("\033[0m") # reset terminal colors

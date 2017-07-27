import glob
import os
import pprint
import pyminizip

# Glob the files in the directory src. Filter resulting glob list so that only files remain (no folders).
# Compress the files into a .zip called give by dst. 
# Optional password and compression level where (Faster) 1 <--> 9 (Better Compression)

def compress_files(src,dst,password='',clevel=1):
    glob_files = glob.glob(src,recursive=True)
    files = [item for item in glob_files if os.path.isfile(item) is True]
    pprint.pprint(files)
    files_unique = remove_duplicate_filenames(files)
    pprint.pprint(files_unique)
    pyminizip.compress_multiple(files_unique,dst,password,clevel)



# Based on https://www.dotnetperls.com/duplicates-python

def remove_duplicate_filenames(values):
    output = []
    for value in values:
        if value.split("/")[-1] not in [item.split("/")[-1] for item in output]:
            output.append(value)
    return output

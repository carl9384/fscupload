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
    pyminizip.compress_multiple(files,dst,password,clevel)

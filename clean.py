#!/usr/bin/python3
import os

# this cleans the target/reports directory 
print("Cleaning up reports folder")
os.system('rm -r target/reports/*')
print("Done!")

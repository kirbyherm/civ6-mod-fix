#!/usr/bin/env python3
import subprocess
import os
import json

def main():

    rootdir = ""
    with open('config.json','rb') as f:    
        configs = json.load(f)
        rootdir = configs['civmodsfolder'] 
            
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(subdir, file)
            lower_path = os.path.join(subdir, file.lower())
            if os.path.lexists(lower_path):
                subprocess.call(['rm',lower_path])
            subprocess.call(['ln','-s',path, lower_path])


if __name__ == "__main__":
    main()

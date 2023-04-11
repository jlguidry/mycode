#! /usr/bin/env python3
"""Pushing files around"""

#import additional code
import shutil
import os

def main():

    #move to working dir
    os.chdir("/home/student/mycode/")

    #copy the fileA to file B
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire dir to backup
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")


if __name__== "__main__":
    main()


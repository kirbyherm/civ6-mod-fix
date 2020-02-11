# written by kirbyherm, Feb 2020
# author not responsible for individual use or error 
#
# Python script "loop_lns.py" recusively loops through the directories in the 
#   mod directory specified in config.json and soft links lower case files to 
#   the upper case original.
#
# Designed to fix Linux bugs with Sukritact's mods
#   see comments by Hippish in https://steamcommunity.com/sharedfiles/filedetails/comments/939149009 
#   ca. Oct 2019



#  REQUIREMENTS
#  python3
#    packages: subprocess, os, json

#  INSTALLATION AND USE 
#  clone this directory into a folder on your computer
#  change the path in config.json to point to the path of your Civ6 workshop folder
#    (should be something like "~/.steam/steam/steamapps/workshop/content/289070")
#   




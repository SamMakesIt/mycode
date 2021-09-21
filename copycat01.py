#!/usr/bin/env python3


#import code to help complete
import shutil
import os
#move to working dir
os.chdir("/home/student/mycode/")
#copy file a to file b
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#Copy the entire dird will create a backup dir
shutil.copytree("5g_research/", "5g_research_backup/")


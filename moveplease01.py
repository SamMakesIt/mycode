#!/usr/bin/env python3

#import extra scripts
import shutil
import os

# Change working dir to home
os.chdir('/home/student/mycode/')

#move to path dest
shutil.move('raynor.obj', 'ceph_storage/')

#give new name to kerrigan
xname = input('What is the new name for kerrigan.obj? ')
#rename kerrigan
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



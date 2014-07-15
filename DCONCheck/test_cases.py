import sys, os
sys.path.append('../TestEng')
import csv
import re
from collections import Counter
from tools import *
#from spellCheck import *

errors = {}
dcon_repo_dir_txt = open('../info.txt', 'r')
dcon_staging_dir = dcon_repo_dir_txt.read() + '/staging/'
all_csvs = getAllCSV(dcon_staging_dir)
csvs = csv_class_factory(dcon_staging_dir)
print csvs["Achievements.csv"].row('LTQsuperhero1')

#********************************* List of Test Cases ************************************
def tests():
	# dupeAchievementStepsIdCheck()
	return errors

#********************************* EXAMPLE: Dupe Achievement Steps ID Check ***********************
# def dupeAchievementStepsIdCheck():
# 	test_name = 'Duplicate Achievements Steps ID Check'
# 	achievement_steps_csv = all_csvs['Achievement.csv']
# 	ids = []
# 	for row in achievement_steps_csv:
# 		ids.append(row[0])
# 	id_occurances = Counter(ids)
# 	dupe_ids = {}
# 	for id in id_occurances:
# 		if id_occurances[id] > 1:
# 			dupe_ids[id] = id_occurances[id]
# 	errors[test_name] = dupe_ids

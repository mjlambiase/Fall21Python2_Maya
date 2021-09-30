# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:36:31 2021

@author: mjlam
"""

'''
Maya Lambiase
9/28/21
Python 2 - DAT-129 
JSON project
Program that takes in a csv file and a json search criteria file.
Output json file with containing the records matched by the search criteria.  
'''

import csv
import json
    
   
def get_json_search_criteria(json_file):
    search_criteria = {}
    with open(json_file) as criteria:
        search_criteria = json.load(criteria)
    return search_criteria
    
                          
def import_csv_file(csv_file):   
    list_of_records = []
    with open(csv_file, 'r') as csvfile:
        project = csv.DictReader(csvfile)
        for row in project:
            list_of_records.append(row)
    #print(list_of_records)
    return list_of_records

def match_search_criteria(data_set, search_criteria):
    '''
    data_set is a list of dictionaries, each dictionary corresponding to a single list in data file
    for loop that iterates over each element of dictionary 
    search criteria is a dictionary
    check value from record against value in search criteria producing a yes if matches or no if does not match
    '''
    
    for record in data_set:
        #compare value of records key status to first item in the list which is the value of the criteria's keys status
        #this is matching!!!!
        if record['status'] == criteria['status']:
            print(record['status'])
 
  

list_of_records = import_csv_file("capital_projects.csv")

criteria = get_json_search_criteria("json_search_criteria.json")

match_search_criteria(list_of_records, criteria)
# -*- coding: utf-8 -*-
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
                               
def import_csv_file(csv_file):   
    list_of_records = []
    with open(csv_file, 'r') as csvfile:
        project = csv.DictReader(csvfile)
        for row in project:
            list_of_records.append(row)
    return list_of_records
   
def get_json_search_criteria(json_file):
    search_criteria = {}
    with open(json_file) as criteria:
        search_criteria = json.load(criteria)
    return search_criteria

def validate_json_file(json_file):
    try:
        with open(json_file) as file:
            json.load(file)
            return True
    except ValueError as error:
        print("invalid json file", error)
        return False

def match_search_criteria_and_output_json_file():
    criteria = get_json_search_criteria("json_search_criteria.json")
    list_of_records = import_csv_file("capital_projects.csv")
    with open("json_file_output_3.json", "w") as jsonfile:
        for record in list_of_records:
        #compare value of records key status to first item in the list which is the value of the criteria's keys status
        #this is matching!!!!
            if record['asset_type'] == criteria['asset_type']:
                jsonfile.write(json.dumps(record))  
            jsonfile.write('\n')   

def main():
    valid = validate_json_file("json_search_criteria.json")
    if valid == True:
        match_search_criteria_and_output_json_file()
    else:
        print("fix json file and try again")

if __name__ == "__main__":
    main()

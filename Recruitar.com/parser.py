import pandas as pd
import json
import os

def json_file(path):

    with open(path, 'r') as file:
        content = json.load(file)

    return content


def category_key_mapping(dict_object):
    dict_keys = dict_object.keys()
    key_count = 1
    key_cat_mapping = {}

    for key in dict_keys:
        key_cat_mapping[key] = key_count
        key_count += 1

    return key_cat_mapping

def category_keys(dict_object):
    dict_keys = dict_object.keys()
    key_count = 1
    key_cat_mapping = {}

    for key in dict_keys:
        key_cat_mapping[key] = key_count
        key_count += 1

    return key_cat_mapping

def dict_to_list(data):

    li_data = []
    for key in data:
        #print(key)
        for sub in data[key].keys():
            #print(sub)
            li = [key, sub]
            for values in data[key][sub]:
                #print(values)
                li.append(','.join(data[key][sub]))
            li_data.append(li)
    #print(li_data)
    return li_data
def creat_sql(key_dict, list):

    if not os.path.isfile('sqlstructure.sql'):
        sql_file = open('sqlstructure.sql', 'a')
        sql_file.write("CREATE DATABASE `mymajorsdata`;\n")
        sql_file.write("USE `mymajorsdata`;\n")
        sql_file.write("CREATE TABLE `categories` (`id` smallint NOT NULL,`catname` varchar(100) DEFAULT NULL,PRIMARY KEY (`id`));\n")
        sql_file.write("CREATE TABLE `jobskill` (`id` int NOT NULL AUTO_INCREMENT,`catid` smallint NOT NULL,`subcat` varchar(200) DEFAULT NULL,`skills` varchar(1000) DEFAULT NULL,PRIMARY KEY (`id`),KEY `catid` (`catid`),CONSTRAINT `jobskill_ibfk_1` FOREIGN KEY (`catid`) REFERENCES `categories` (`id`));\n")
        sql_file.close()

    sql_file = open('sqlstructure.sql', 'a')
    for key, value in key_dict.items():
        query_stmt = "INSERT INTO categories (id, catname) VALUES ({}, '{}');\n".format(value, key)
        sql_file.write(query_stmt)

    for job_list in list:
        cat_id = key_dict[job_list[0]]
        subcat = job_list[1].replace("'", '')
        skill = job_list[2].replace("'", '')
        query_stmt = "INSERT INTO jobskill (catid, subcat, skills) VALUES ({}, '{}', '{}');\n".format(cat_id, subcat, skill)
        sql_file.write(query_stmt)

    sql_file.close()

if __name__ == '__main__':
    da = '/home/ritik/Documents/tutree INC/flask code /active/recuriter.json'
    dict = json_file(da)
    #print(dict)
    key_dict = category_keys(dict)
    #print(key_dict)
    list = dict_to_list(dict)
    #print(list)
    creat_sql(key_dict, list)
    print(creat_sql)
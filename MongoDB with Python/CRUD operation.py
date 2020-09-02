#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:07:44 2020

@author: jasneekchugh
"""

import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')


mydb=client['Employee']

information=mydb.employeeinformation

record= {
        'first_name':'Jasneek',
        'last_name':'Chugh',
        'department':'Analytics'
        
        }

information.insert_one(record)

record2= [
        {
        'first_name':'Jasneek1',
        'last_name':'Chugh1',
        'department':'Analytics1'
        },
        {
        'first_name':'Jasneek2',
        'last_name':'Chugh2',
        'department':'Analytics2',
        'Phone':'9148937054'
        },
         {
        'first_name':'Jasneek3',
        'last_name':'Chugh3',
        'department':'Analytics3'
        }

]

information.insert_many(record2)




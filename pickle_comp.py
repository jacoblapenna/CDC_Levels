# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:36:31 2022

@author: jlapenna
"""

import pickle

with open("data_07182022125006.pickle", 'rb') as f:
    json_old_old = pickle.load(f)
    
with open("data_07182022125019.pickle", 'rb') as f:
    json_old = pickle.load(f)

with open("data_07212022093614.pickle", 'rb') as f:
    json_new = pickle.load(f)


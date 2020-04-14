import os
import datajoint as dj
import numpy as np
import yaml
from computation import compute
    
with open('./credentials.yaml') as file:
    credential = yaml.load(file, Loader=yaml.FullLoader)
    
# Connect to the datajoint database
dj.config['database.user'] = credential['user']
dj.config['database.password'] = credential['password']
dj.config['database.host'] = credential['host']
dj.conn()

# Get the specified schema reference
schema = dj.schema(credential['schema'])

# Below are the table definitions
@schema
class Parent(dj.Manual):
    definition = """
    filename: varchar(200)   #filename without extension.
    ---
    """ 

@schema
class Children(dj.Imported):
    definition = """
    -> Parent
    ----------------
    processed: varchar(200)
    """
    
    def make(self, key):
        row_input = (Parent & key).fetch1()
        output = compute(row_input)
        
        if output:
            self.insert1(output)
            
Children.populate()


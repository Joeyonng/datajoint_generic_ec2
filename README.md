# Datajoint Generic EC2 Computation Script

## About

This is a generic script that is meant to be used to run computation on EC2 instances via leveraging the populate method available as part of DJ. 

## Structure

The structure is as follows:

* *credentials.yaml*: Specifies the credentials and the schema that is to be used for Datajoint connection.
* *schema.py*: Defines the 'Parent' and 'Child' table definitions and a generic make function that calls a computation method and calls populate method.
* *computation.py*: Actual computation method that needs to be specified by the user.

## How to setup

1. Fork current github repository into your own account.
2. Add credentials and schema information in *credentials.yaml*.
3. Define the compute method in *computation.py* (input/ouput structure information in doc string).
4. (Optional) To change table name change class name of 'Parent' or 'Child' in *schema.py*
5. (Optional) To change columns in tables change appropriate definition string of class. [For format information click here](https://docs.datajoint.io/python/definition/03-Table-Definition.html)
6. Push changes to github repository. Note link.

## How to run

To run the script (assuming that all dependencies e.g. datajoint, etc. are installed) run the command `python schema.py` 

## How to run on multiple instances 

To create multiple EC2 instances and run the script on them parallelly in an easy way, go to ./aws-jupyter for more information.
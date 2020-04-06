def compute(row_input):
    '''
    This function will be called inside make function of Children table.

    Parameters:
    row_input: dict
    Each row in the database table in the format of {key: value}

    Return: dict or None
    It should return a dict that is needed into the Children table. 
    The dict should at least contain the same key-value pair of the row_input's primary key.
    If return None, nothing will be inserted into the Children table.
    '''
    print(row_input)
    return


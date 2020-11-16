
def mapa(dataframe):
    '''
    This function takes a dataframe and extracts the values that are contained
    inside a list.
    '''
    return dataframe.applymap(lambda x: x[0] if isinstance(x, list) else x)

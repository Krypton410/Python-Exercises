# Paste your function here
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    invert = {v: k for k, v in d.items()}
    print invert
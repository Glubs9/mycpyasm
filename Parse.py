#split the line into a series of code objects
    #entry point labelled as main

from CodeContext import CodeContext

def split(lines):
    """ 
    split splits the files into a series of lines for each object
    (how to handle the args in)
    (this takes already lexed information from the csv reader)
    """
    curr_obj = None #gets defined as a CodeContext
    all_objs = []
    for n in lines:
        if len(n) == 0 or n[0][0] == "#": continue #this is preprocessing which should be done in preprocess.py but
                                 #i'm doing it here because the parser requires thsi to functoin
        elif n[0].upper() == "DEFINE":
            curr_obj = CodeContext(name=n[1], arg_num=len(n[2:]), varnames=n[2:])
        elif n[0].upper() == "END":
            all_objs += [curr_obj]
            curr_obj = None
        else:
            curr_obj.bytes += [n]
    return all_objs

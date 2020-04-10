try:
    import os
except Exception as e:
    print("Exception Occured:{0}".format(str(e)))
def osName():
    return os.name

try:
    from osName import *
except Exception as e:
    print("Exception Occured:{0}".format(str(e)))
os = osName()
if os == 'nt' or os == 'posix':
    print ("Functional Testing Sucessful")
import os
import functions


#checking database existance
if functions.filechk('forget.db') is True:
    functions.intialsetup()
    functions.caller()
else:
	functions.caller()



# ************************************************************************
# Script: myclass.py
# Author: Richard Knechtel
# Date: 05/20/2021
# Description: This Module contains a Class that contains Some Functions.
# Python Version: 3.8.x
#
#
#************************************************************************

#---------------------------------------------------------[Imports]------------------------------------------------------

_modules = [
            'ast',
            'datetime',
            'errno',
            'logging',
            'os',
            'sys',
           ]

for module in _modules:
  try:
    locals()[module] = __import__(module, {}, {}, [])
  except ImportError:
    print('Error importing %s.' % module)

# Custom Modules:
from config import MyScriptconfig as config
from modules import genericfunctions as genfunc

#---------------------------------------------------------[Class]--------------------------------------------------------

# ###################################################################################
# Class:  My_Class
class My_Class:

  """
  Class:  My_Class
  Description: This is a python class of SomeFunctions
  
  Example usage:
    from myclass import My_Class \n
    my_+class = myclass()  \n
  
  """

  # ###################################################################################
  # Function: __init__
  def __init__(self):

    """
    Function: __init__
    Description: This is the class iniitializaion \n
    Parameters: self: My_Class class
    Return: None
    """

    # Logging:
    # For Info and up logging
    config.LogLevel = logging.INFO
    # For Debug and up Logging:
    # config.LogLevel = logging.DEBUG
    
    # Initialize Logging:
    global MyScriptLogger
    MyScriptLogger = genfunc.InitScriptConsoleLogging(__name__, config.LogLevel)

  # ###################################################################################
  # Function: _clear
  def _clear(self):

    """
    Function: _clear
    Description: Clears the object of it's instance data.
    Parameters: self: My_Class class
    Return: None
    """

    def function1:
     # Some initialization code here

   def function2:
     # Some initialization code here
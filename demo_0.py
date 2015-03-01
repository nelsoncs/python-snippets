
'''
Created on Jun 17, 2012

@author: nelsoncs - 2012 Jun 17 - Phoenix BIOS

In version 3+ of python the function "raw_input()" was changed to "input()".
The "print()" function was also changed.

I am not interested in devising a method to support command line input for 
all possible versions above 2.7.  Therefore, this program uses "input()" as 
in version 3 and above, and thus must be run with version 3 or above.  It was 
tested with 3.2 and 2.7.3.  Version 2.7.3 will fail because the user input is
interpreted as a python identifier, not as an rvalue assignment.

If you want to use this program with 2.7 then please refactor 
input() to raw_input(), and add the line:

from __future__ import print_function

:as the very first line of this file.

This program was tested under Linux, so sys.stdin.readline() could be used to 
support all version 2.7 +. However, readline() may not be compatible with 
Windows based platforms without additional modules (untested), thus violating
the terms of the test specification.  Therefore, I have chosen to restrict 
python versioning in favor of platform compatibility.
'''

import os


class Demo_0():
    '''
    Prompts for input.  
    User inputs a color and gets a color in response.  
    Incorrect input ends program.  
    
    Program follows instructions for this test strictly in that each 
    color must be spelled correctly and is case sensitive.  
    Specification only addresses "text" entry by user, but use
    of cntl-d is covered just in case.
    
    The program uses a dictionary. This could have easily been a list
    where the response is the next item relative to a matched string.
    A list would require less memory. However, the number of items is 
    small so the extra data for a dictionary is not a problem in this 
    instance and I like dictionaries.
    '''


    def __init__( self ):
        '''
        Constructor - creates mapping of 
        input (key) to response (value) colors
        '''

        self.colors = dict({
                 "Red" : "Blue",
                 "Blue": "Green",
                 "Green": "White",
                 "White": "Black",
                 "Black": "Pink"
                 })
        
        # most recent user input
        self.user = ""


    def prompt( self ):
        '''
        Presents the prompt, prints error message if user's
        color is not found in dictionary.
        '''
           
        try:
            # ask for a color
            self.user = input( " Input a color: ")
        
        # cover exception for cntl-d
        except EOFError as eof:
            print( "Exiting.", eof )
            os._exit(0)
            
        except NameError as name_err:
            print( "Please use python version 3 or higher.")
            print( name_err )

        try:
            # look up color in dictionary
            response = self.colors.get( self.user )
            
            # tell user what was found
            print( "My response is:", response )
            print( '\r' )
            
            # Let caller know if None was found
            return response
            
        # may never reach this exception
        except AttributeError as e:
            print( "   Quitting on:" + e )
            os._exit(0)


if __name__ == '__main__':
    
    response = ""
    
    # Instantiate class
    demo = Demo_0()
    
    # Offer a way out.
    print( "  Cntl-d exits.\r\r")
    
    # Endless while loop, not something I use very often.
    while True:
        response = demo.prompt()
         
        # dictionary returns None when lookup fails
        if response == None:
            
            # print the offending input
            print( "   Quitting on:", demo.user )
            os._exit(0)
            

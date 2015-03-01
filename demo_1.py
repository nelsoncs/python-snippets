'''
Created on Jun 17, 2012

@author: nelsoncs - 2012 Jun 17 - Phoenix BIOS
 
This program was tested with python 3.2 and 2.7.3.  
Version 2.7.3 will fail because the user input is interpreted as a python 
identifier, not as an rvalue assignment.  Please see the header comments
for demo_0.  If you want to use this program with 2.7 then please refactor 
input() to raw_input(), and add the line:

from __future__ import print_function

:as the very first line of this file.
'''

import os, re

class Demo_1():
    '''
    Prompts for input.  
    User inputs an eight digit hexadecimal number.

    On correct input, prints decimal and binary value and the 
    number of bits set in binary representation.
    
    Incorrect input gives new prompt.  Ctrl-d quits.
    '''


    def __init__( self ):
        '''
        Constructor
        '''
        # most recent user input
        self.user = ""
        
        # match [0x]########[h] where # is a hex digit
        # seems to be a problem with the regex accepting ####-#### interspersed '-'
        # 09789-7890688906890 is accepted as 78906889
        self.hex = re.compile( '(0x)?([0-9a-fA-F]){8}(h)?' )
        
        # remove any leading or training characters
        self.hex_stripped = re.compile( '([0-9a-fA-F]){8}' )

    
    def bits_set( self, num ):  
        '''
        takes an (unsigned) int as the second argument and returns an int count
        of the bit that are set by repeatedly masking the lowest bit and right
        shifting
        '''
        count = 0
        
        while num > 0:
            
            if num & 0x1:
                ++count
            
            num = num >> 1
        
        return count

        
    def prompt( self ):
        '''
        Presents the prompt
        '''
        # allocate return variable
        num = None
        
        try:
            # ask for a number
            self.user = input( "Input eight digit hexadecimal number: ")
        
            # if user gave an input
            if self.user:
                # check against DFA for hex format
                num = self.hex.search( self.user )
                
                # give some feedback to user
                if num:
                    
                    # strip any extraneous characters ( from entire matching string converted to lower case )
                    num_strip = self.hex_stripped.search( num.group().lower() )

                    # Note: actually allows longer string of digits, then takes first eight
                    if num_strip:
                        print( "     Hex : {0:X}".format( int( num_strip.group(), 16 ) ) )
                        print( "     Dec : {0:,d}".format( int( num_strip.group(), 16 ) ) )
                        print( "     Bin : {0:0>32b}".format( int( num_strip.group(), 16 ) ) )
                    
                        # convince "loose" typing to cast from representation to string
                        #num_str = num.group()
                    
                        print( "Bits set :", self.bits_set( int( num_strip.group(), 16 ) ) )
                        print( "\r" )
                    else:
                        print( 'Not a good number.\r' )
                    
                else:
                    print( 'Not a good number.\r' )
        
        # cover exception for cntl-d
        except EOFError as eof:
            print( "\rExiting.", eof )
            os._exit(0)
            
        except NameError as name_err:
            print( "Please use python version 3 or higher.")
            print( name_err )
            
        return num 

            
if __name__ == '__main__':
    
    # Instantiate class
    demo = Demo_1()
    
    # Offer a way out.
    print( "Cntl-d exits.\r\r")
    
    # Endless while loop.
    while True:
        response = demo.prompt()
        

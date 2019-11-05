# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 02:16:02 2019

@author: PaulGraham
"""
from Array import Array1D
class Array2D :
    def __init__(self, numRows, numCols):
        self._theRows = Array1D(numRows)
        for i in range(numRows):
            self._theRows[i] = Array1D( numCols )
    
    def numRows( self ):
        return len( self._theRows )

    def numCols( self ):
        return len( self._theRows[0] )

    def clear( self, value ):
        for row in self._theRows:
            row.clear(value)

    def __getItem__( self, indexTuple ):
        assert len(indexTuple) == 2, "Invalid number of array subscripts."
        row , col = indexTuple
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        return self._theRows[row][col]

    def __setItem__( self, indexTuple, value ):
        assert len(indexTuple) == 2, "Invalid number of array subscripts."
        row , col = indexTuple
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range"     
        self._theRows[row][col] = value
    
    def __print__(self):
        for row in self._theRows:
            row.__print__()
            print("\n")
    
#myArray = Array2D(5,6)
#myArray.clear(6)
#myArray.__printArray__()
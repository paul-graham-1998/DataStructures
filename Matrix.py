# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:47:41 2019

@author: PaulGraham
"""

from Array_2 import Array2D

class Matrix :
    def __init__( self, numRows, numCols ):
        self._theGrid = Array2D( numRows, numCols )
        self._theGrid.clear( 5 )

    def numRows( self ):
        return self._theGrid.numRows()
    def numCols( self ):
        return self._theGrid.numCols()

    def __getItem__( self, indexTuple ):
        return self._theGrid.__getItem__(indexTuple)

    def __setItem__( self, indexTuple, scalar ):
        self._theGrid.__setItem__(indexTuple,scalar)

    def scaleBy( self, scalar ):
        for r in range(self.numRows()) :
            for c in range(self.numCols()):
                self[ r, c ] *= scalar

    def tranpose( self ):
        tranpose = Array2D(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                transpose.__setitem__([r,c] , __getitem__([c,r]))
        return transpose
                

    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the matrix addition."
        
        newMatrix = Matrix( self.numRows(), self.numCols() )
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]
        return newMatrix

    def __sub__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the matrix subtraction."
        newMatrix = Matrix( self.numRows(), self.numCols() )
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] - rhsMatrix[ r, c ]
        return newMatrix
 
    def __mul__( self, rhsMatrix ):
        assert self.numCols() == rhsMatrix.numRows(),\
            "Matrix sizes not compatible for matrix multiplicaiton."
        newMatrix = Matrix(self.numRows() , rhsMatrix.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                element = 0
                for k in range(self.numCols()):
                    element += self.__getItem__((r,k)) * rhsMatrix.__getItem__((k,c))
                newMatrix.__setItem__((r,c) , element)
        return newMatrix
    
    def __print__(self):
        self._theGrid.__print__()
    



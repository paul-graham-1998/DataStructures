# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 01:21:26 2019

@author: PaulGraham
"""

import ctypes

class Array1D:
    def __init__(self, size):
        assert size > 0
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)
        
    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self)
        return self._elements[index]
    
    def __setitem__(self, index, value):
        assert index >=0 and index < len(self)
        self._elements[index] = value
    
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
    
    def __iter__(self):
        return _ArrayIterator(self._elements)
    
    def __print__(self):
        for element in self._elements:
            print(element,end = ' ')
class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
            

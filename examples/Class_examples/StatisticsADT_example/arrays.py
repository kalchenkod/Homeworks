import ctypes


class Array:
    """
    Implements the Array structure using array 
    capabilities of the ctypes module.
    """
    def __init__(self, size):
        """
        Creates an array with size elements.

        :param size: size of array.
        """
        assert size > 0, "Array size must be > 0"
        self._size = size

        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.

        :return: the size of the array. 
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element.

        :param index: the index of element.
        :return: value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.

        :param index: the index element.
        :param value: the value of element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        self._elements[index] = value

    def clear(self, value):
        """
        Clears the array by setting each element to the given value.

        :param value: the value of element.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.

        :return: the array's iterator for traversing the elements. 
        """
        return ArrayIterator(self._elements)

    def __str__(self):
        """
        Converts structure to a string.

        :return: converted structure.
        """
        to_return = "("
        for index in range(self._size - 1):
            to_print = str(self[index])
            to_return = to_return + to_print + ","
        to_print = str(self[self._size - 1])
        return to_return + to_print +")"

class ArrayIterator:
    """
    An iterator for the Array ADT.
    """
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration

class Array2D :
    def __init__( self, num_rows, num_cols ):
        self.rows = Array( num_rows )

        for i in range( num_rows ) :
            self.rows[i] = Array( num_cols )

    def num_rows( self ):
        return len( self.rows )

    def num_cols( self ):
        return len( self.rows[0] )

    def clear( self, value ):
        for row in range( self.num_rows() ):
            self.rows[row].clear( value )

    def __getitem__( self, index_tuple ):
        assert len(index_tuple) == 2           
        row = index_tuple[0]
        col = index_tuple[1]
        assert row >= 0 and row < self.num_rows() \
           and col >= 0 and col < self.num_cols(), \
               "Array subscript out of range."
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__( self, index_tuple, value ):
        assert len(index_tuple) == 2            
        row = index_tuple[0]
        col = index_tuple[1]
        assert row >= 0 and row < self.num_rows() \
           and col >= 0 and col < self.num_cols(), \
              "Array subscript out of range."
        array_1d = self.rows[row]
        array_1d[col] = value

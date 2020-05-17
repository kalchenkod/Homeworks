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


class DynamicArray:
    """
    A dynamic array class a simplified Python list.
    """

    def __init__(self):
        """
        Creates an empty array.
        """
        self._size = 0 
        self._capacity = 1  
        self._elements = self.make_array(self._capacity)

    def __len__(self):
        """
        Returns the number of elements in the array.

        :return: the number of elements in the array. 
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element by index.

        :param index: the index of element.
        :return: the value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def append(self, value):
        """
        Puts the value in the end of the array.

        :param value: the value of element.
        """
        if self._size == self._capacity: 
            self.resize(2 * self._capacity) 
        self._elements[self._size] = value
        self._size += 1

    def resize(self, capacity):
        """
        Resize internal array to new capacity.
                
        :param capacity: new capacity of array.
        """
        new_elements = self.make_array(capacity) 

        for k in range(self._size):
            new_elements[k] = self._elements[k]
        self._elements = new_elements 
        self._capacity = capacity

    def make_array(self, size):
        """
        Return new array.
        
        :param size: size of array.
        :return: array.
        """
        return Array(size)

    def insert(self, index, value):
        """
        Inserts value at index, shifting subsequent values rightward.        

        :param index: the index.
        :param value: the value that need to be inserted. 
        """
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        for i in range(self._size, index, -1):
            self._elements[i] = self._elements[i - 1]

        self._elements[index] = value
        self._size += 1

    def remove(self, value):
        """
        Removes first occurrence of value.
        
        :param value: the value that need to be removed.
        """
        for i in range(self._size):
            if self._elements[i] == value: 
                for j in range(i, self._size - 1):
                    self._elements[j] = self._elements[j + 1]

                self._elements[self._size - 1] = None 
                self._size -= 1 

                return 
        raise ValueError("Value not found")
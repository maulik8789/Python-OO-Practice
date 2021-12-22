"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 100):
        """
        serial number starts from 100 and can be configured.
        """
        self.original = start
        self.start = start
        self.begin = True

    def generate(self) :
        """
        generates serial number starting from attribute 'start' 
        
        and increases by 1 at every call 
        """
        if self.begin == True:
            self.begin =False
            return self.original
        else:
            self.start = self.start + 1
            return self.start

    def reset(self):
        """
        makes it start to generate serial number from start
        """
        self.begin = True
        self.start = self.original


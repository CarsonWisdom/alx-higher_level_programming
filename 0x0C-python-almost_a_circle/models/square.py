from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instances of Square

        Args:
            size (int): width and height of square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Property retriever for size.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.
        Args:
            value (int): width of square.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        super().__setattr__('width', value)
        super().__setattr__('height', value)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        attributes = ['id', 'size', 'x', 'y']
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square.

        Returns:
            dict: square.
        """
        square_dict = super().to_dictionary()
        square_dict['size'] = square_dict.pop('width')  # Rename key 'width' to 'size'
        return square_dict

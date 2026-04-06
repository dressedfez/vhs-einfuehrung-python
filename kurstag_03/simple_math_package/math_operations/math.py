"""A simple math module for demonstration purposes."""


class Matrix:
    """A simple matrix class for demonstration purposes."""

    def __init__(self, data):
        """Initialize the matrix with a 2D list."""
        self.data = data

    def scalar_multiply(self, scalar):
        """Multiply the matrix by a scalar."""
        result = [
            [self.data[i][j] * scalar for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def add(self, other):
        """Add another matrix to this matrix."""
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def subtract(self, other):
        """Subtract another matrix from this matrix."""
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        return self.add(other.scalar_multiply(-1))

    def __str__(self):
        """Return a string representation of the matrix."""
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __repr__(self):
        """Return a string representation of the matrix for debugging."""
        return f"Matrix({self.data})"

# Matrix.


# Write a class that can represent any 4𝑥4 real matrix.
# Include two functions to calculate the sum and dot product of two matrices.
# Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
# Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction
# - inversion
# - string representation
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
# Delete these comments before commit!
#
# Good luck.
import logging


class NonMatchingMatrixSizes(Exception):

    def __init__(self, matrix1Size, matrix2Size):
        self.matrix1Size = matrix1Size
        self.matrix2Size = matrix2Size
        self.message = "Matrix of size {}x{} and Matrix of size {}x{} do not match".format(
            self.matrix1Size, self.matrix1Size, self.matrix2Size, self.matrix2Size)
        super(NonMatchingMatrixSizes, self).__init__(self.message)


class SquareMatrix:

    def __init__(self, data="Empty", size=2):
        if data != "Empty":
            self.size = len(data)
        else:
            self.size = size

        self.Matrix = self._createEmptyMatrixOfSize(self.size)
        if data != "Empty":
            for i in range(self.size):
                for j in range(self.size):
                    self.Matrix[i][j] = data[i][j]

    def transpone(self):
        logging.info("Ongoing Operation: Matrix transposition")
        transpositionProduct = SquareMatrix(data="Empty", size=self.size)
        for i in range(self.size):
            for j in range(self.size):
                transpositionProduct.Matrix[i][j] = self.Matrix[j][i]
        return transpositionProduct

    def __str__(self, loggingValue=""):
        loggingValue = "Displaying Matrix of size {}x{}:\n".format(
            self.size, self.size)
        loggingValue += self._getMatrixValues()
        return loggingValue

    def __repr__(self):
        return self._getMatrixValues()

    def __add__(self, secondMatrix):
        secondOperand = self._validateMatricesSizes(self, secondMatrix)
        additionProdut = SquareMatrix(data="Empty", size=self.size)

        if secondOperand["type"] == "int":
            additionProdut = self._calculateWithOperand(
                self, '+', secondMatrix, additionProdut)
        elif secondOperand["type"] == "matrix":
            additionProdut = self._calculateMatrices(
                self, '+', secondMatrix, additionProdut)
        return additionProdut

    def __radd__(self, secondOperand: int):
        additionProdut = SquareMatrix(data="Empty", size=self.size)
        additionProdut = self._calculateWithOperand(
            self, '+', secondOperand, additionProdut)
        return additionProdut

    def __sub__(self, secondMatrix):
        secondOperand = self._validateMatricesSizes(self, secondMatrix)
        subtractionProduct = SquareMatrix(data="Empty", size=self.size)

        if secondOperand["type"] == "int":
            subtractionProduct = self._calculateWithOperand(
                self, '-', secondMatrix, subtractionProduct)
        elif secondOperand["type"] == "matrix":
            subtractionProduct = self._calculateMatrices(
                self, '-', secondMatrix, subtractionProduct)
        return subtractionProduct

    def __rsub__(self, secondOperand: int):
        subtractionProduct = SquareMatrix(data="Empty", size=self.size)
        subtractionProduct = self._calculateWithOperand(
            self, "-", secondOperand, subtractionProduct)
        return subtractionProduct

    def __mul__(self, secondMatrix):
        secondOperand = self._validateMatricesSizes(self, secondMatrix)
        multiplicationProduct = SquareMatrix(data="Empty", size=self.size)

        if secondOperand["type"] == "int":
            multiplicationProduct = self._calculateWithOperand(
                self, '*', secondMatrix, multiplicationProduct)
        elif secondOperand["type"] == "matrix":
            multiplicationProduct = self._calculateMatrices(
                self, '*', secondMatrix, multiplicationProduct)
        return multiplicationProduct

    def __rmul__(self, secondOperand: int):
        multiplicationProduct = SquareMatrix(data="Empty", size=self.size)
        multiplicationProduct = self._calculateWithOperand(
            self, "*", secondOperand, multiplicationProduct)
        return multiplicationProduct

    def __truediv__(self, secondMatrix):
        secondOperand = self._validateMatricesSizes(self, secondMatrix)
        multiplicationProduct = SquareMatrix(data="Empty", size=self.size)

        if secondOperand["type"] == "int":
            multiplicationProduct = self._calculateWithOperand(
                self, '/', secondMatrix, multiplicationProduct)
        elif secondOperand["type"] == "matrix":
            multiplicationProduct = self._calculateMatrices(
                self, '/', secondMatrix, multiplicationProduct)
        return multiplicationProduct

    def __rtruediv__(self, secondOperand: int):
        multiplicationProduct = SquareMatrix(data="Empty", size=self.size)
        multiplicationProduct = self._calculateWithOperand(
            self, "/", secondOperand, multiplicationProduct)
        return multiplicationProduct

    def __matmul__(self, secondMatrix):
        logging.info("Ongoing Operation: Matrix @ Matrix multiplication")
        secondOperand = self._validateMatricesSizes(self, secondMatrix)
        multiplicationProduct = SquareMatrix(data="Empty", size=self.size)
        if secondOperand["type"] == "int":
            multiplicationProduct = self._calculateWithOperand(
                self, '*', secondMatrix, multiplicationProduct)
        if secondOperand["type"] == "matrix":
            for i in range(len(self.Matrix)):
                for j in range(len(secondMatrix.Matrix[0])):
                    for k in range(len(secondMatrix.Matrix)):
                        multiplicationProduct.Matrix[i][j] += self.Matrix[i][k] * \
                            secondMatrix.Matrix[k][j]
        return multiplicationProduct

    def _calculateWithOperand(self, firstOperand, operator, secondOperand, result):
        logging.info("Ongoing Operation: Matrix {} {}".format(
            operator, secondOperand))
        for i in range(firstOperand.size):
            for j in range(firstOperand.size):
                result.Matrix[i][j] = eval(
                    "firstOperand.Matrix[i][j]" + operator + "secondOperand")
        return result

    def _calculateMatrices(self, firstOperand, operator, secondOperand, result):
        logging.info(
            "calculating Matrices, operation operator: {}".format(operator))
        for i in range(firstOperand.size):
            for j in range(firstOperand.size):
                result.Matrix[i][j] = eval(
                    "firstOperand.Matrix[i][j]" + operator + "secondOperand.Matrix[i][j]")
        return result

    def _createEmptyMatrixOfSize(self, size):
        return [[0 for i in range(size)] for j in range(size)]

    def _getMatrixValues(self):
        loggingValue = ""
        for i in range(self.size):
            for j in range(self.size):
                loggingValue += "{} ".format(self.Matrix[i][j])
            loggingValue += "\n"
        return loggingValue

    def _validateMatricesSizes(self, matrix1, matrix2):
        if isinstance(matrix2, int):
            operandType = {}
            operandType["type"] = "int"
            return operandType
        if matrix1.size != matrix2.size:
            raise NonMatchingMatrixSizes(matrix1.size, matrix2.size)
        operandType = {}
        operandType["type"] = "matrix"
        return operandType


if __name__ == "__main__":

    # Displaying info logs for better comprehension of the example operations presented below
    logging.basicConfig(level=logging.DEBUG)

    logging.info("creating the first 2x2 matrix")
    filledMatrix_2x2 = SquareMatrix([[1, 2],
                                     [3, 4]])
    print(filledMatrix_2x2)

    logging.info("creating the second 2x2 matrix")
    secondFilledMatrix_2x2 = SquareMatrix([[4, 3],
                                           [2, 1]])
    print(secondFilledMatrix_2x2)

    matrixAddition = filledMatrix_2x2 + secondFilledMatrix_2x2
    print(matrixAddition)

    matrixsubtraction = filledMatrix_2x2 - secondFilledMatrix_2x2
    print(matrixsubtraction)

    matrixNumAddition = 2 + filledMatrix_2x2
    print(matrixNumAddition)

    matrixNumSubtraction = 2 - filledMatrix_2x2
    print(matrixNumSubtraction)

    matrixNumMultiplication = 2 * filledMatrix_2x2
    print(matrixNumMultiplication)

    matrixNumDivision = 2 / filledMatrix_2x2
    print(matrixNumDivision)

    matrixMultiplication = filledMatrix_2x2 @ secondFilledMatrix_2x2
    print(matrixMultiplication)

    logging.info("creating a 3x3 matrix for transposition purposes")
    filledMatrix_3x3 = SquareMatrix([[1, 2, 3],
                                     [4, 5, 6],
                                     [7, 8, 9]])
    print(filledMatrix_3x3)

    matrixTranspone = filledMatrix_3x3.transpone()
    print(matrixTranspone)

    logging.info("creating a 4x4 EMPTY matrix")
    emptyMatrix_4x4 = SquareMatrix(data="Empty", size=4)
    print(emptyMatrix_4x4)

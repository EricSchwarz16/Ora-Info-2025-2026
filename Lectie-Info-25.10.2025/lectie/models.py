"""
    Operator	Method	Example
+	__add__(self, other)	a + b
-	__sub__(self, other)	a - b
*	__mul__(self, other)	a * b
/	__truediv__(self, other)	a / b
==	__eq__(self, other)	a == b
<	__lt__(self, other)	a < b
>	__gt__(self, other)	a > b
str()	__str__(self)	print(a)
"""


class ComplexNumber:
    def __init__(self, imaginary = 0, real = 0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):#ii arat programului cum sa adune 
        result = ComplexNumber()
        result.real = other.real + self.real
        result.imaginary = other.imaginary + self.imaginary
        
        return result
    def __sub__(self, other):
        result = ComplexNumber()
        result.real = other.real - self.real
        result.imaginary = other.imaginary - self.imaginary
        
        return result

    def __mul__(self, other):
        """
            ((z1)i + a) * ((z2)i + b) = -(z1*z2) + a*b + b(z1)i + (z2)i*a
        """
        result = ComplexNumber()
        
        if isinstance(other, int):
            result.imaginary = self.imaginary * other
            result.real = self.real * other
        elif isinstance(other, ComplexNumber):
            result.imaginary = self.imaginary * other.real + other.imaginary * self.real
            result.real = -(self.imaginary * other.imaginary) + self.real * other.real
        
        return result

    def __truediv__(self, other): # numar imaginar / numar real
        result = ComplexNumber()
        
        result.imaginary = self.imaginary / other
        result.real = self.real / other
        return result
    
    def __eq__(self, other):#a == b __repr__(self) == __repr__(other)
        return other.imaginary == self.imaginary and other.real == self.real
        
    def __str__(self): #ii arat programului cum sa printeze clasa mea
        return f"{str(self.imaginary) + "i" if self.imaginary != 0 else ""} {"+ " + str(self.real) if self.real > 0 else str(self.real)}"
    
    def __lt__(self, other):	#a < b -> boolean
        pass
    
    def showReal(self):
        return self.real

if __name__ == "__main__":
    z1 = ComplexNumber(2, 3)
    z2 = ComplexNumber(-72, 5)
    
    print(z1 + z2)
    print(((z1 + z2) / 5) * z2)
'''
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''
class ComplexNumber:
    def __init__(self, a, b):
        self.real_z = a
        self.imaginary_z = b

    def __str__(self):
        if self.imaginary_z < 0:
            sign = '-'
        else:
            sign = '+'

        self.imaginary_z = abs(self.imaginary_z)

        return f'{self.real_z} {sign} {self.imaginary_z}i'

    def __add__(self, other_complex):
        real = self.real_z + other_complex.real_z
        imaginary = self.imaginary_z + other_complex.imaginary_z
        return ComplexNumber(real, imaginary)

    def __mul__(self, other_complex):
        real = self.real_z * other_complex.real_z - self.imaginary_z * other_complex.imaginary_z
        imaginary = self.imaginary_z * other_complex.real_z + self.real_z * other_complex.imaginary_z
        return ComplexNumber(real, imaginary)


num1 = ComplexNumber(1, 1)
num2 = ComplexNumber(1, 4)
print(num1 + num2)
print(num1 * num2)
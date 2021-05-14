import unittest
from ..polynomial.polynomial import Polynomial as pol

class TestPolinomialMethods(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(pol(
            [-100, 200, 300])), 'Polinomial([-100, 200, 300])')
        self.assertEqual(repr(pol(
            [0, 200, 300])), 'Polinomial([200, 300])')
        self.assertEqual(repr(pol(
            [0, -200, 300])), 'Polinomial([-200, 300])')
        self.assertEqual(repr(pol(
            [*([0]*100), 200, 300])), 'Polinomial([200, 300])')
        self.assertEqual(repr(pol(
            [1, *([0]*2), 200, 300])), 'Polinomial([1, 0, 0, 200, 300])')
        self.assertEqual(repr(pol(
            [0])), 'Polinomial([0])')
        self.assertEqual(repr(pol(
            [0, 1])), 'Polinomial([1])')
        self.assertEqual(repr(pol(
            [0, -1])), 'Polinomial([-1])')
        self.assertEqual(repr(pol(
            [-1, 0, -1])), 'Polinomial([-1, 0, -1])')

    def test_str(self):
        self.assertEqual(pol(
            [-100, 200, 300]).__str__(), '-100x^2+200x+300')
        self.assertEqual(pol(
            [0, 200, 300]).__str__(), '200x+300')
        self.assertEqual(pol(
            [0, -200, 300]).__str__(), '-200x+300')
        self.assertEqual(pol(
            [*([0]*100), 200, 300]).__str__(), '200x+300')
        self.assertEqual(pol(
            [1, *([0]*2), 200, 300]).__str__(), 'x^4+200x+300')
        self.assertEqual(pol(
            [0]).__str__(), '0')
        self.assertEqual(pol(
            [0, 1]).__str__(), '1')
        self.assertEqual(pol(
            [0, -1]).__str__(), '-1')
        self.assertEqual(pol(
            [1]).__str__(), '1')
        self.assertEqual(pol(
            [-1]).__str__(), '-1')
        self.assertEqual(pol(
            [-1, 0, -1]).__str__(), '-x^2-1')
        self.assertEqual(pol(
            [1, 2, -4]).__str__(), 'x^2+2x-4')
        self.assertEqual(pol(
            [1, 1, 0]).__str__(), 'x^2+x')
        self.assertEqual(pol(
            [1, -1, 0]).__str__(), 'x^2-x')
        self.assertEqual(pol(
            [-1, -1, 0]).__str__(), '-x^2-x')
        self.assertEqual(pol(
            [-1, -1, 0]).__str__(), '-x^2-x')

    def test_add(self):
        self.assertEqual(
            repr(pol([-1, 0, -1]) + pol([-1, 0, -1])), 'Polinomial([-2, 0, -2])')
        self.assertEqual(
            repr(pol([-1, 0, -1]) + pol([1, 0, 1])), 'Polinomial([0])')
        self.assertEqual(
            repr(pol([0, 0, -1]) + pol([1, 0, 1])), 'Polinomial([1, 0, 0])')
        self.assertEqual(
            repr(pol([0, 0, 1]) + pol([1, 1000, 0, 100])), 'Polinomial([1, 1000, 0, 101])')
        self.assertEqual(repr(pol([0]) + pol([0])), 'Polinomial([0])')
        self.assertEqual(
            repr(pol([100, 0]) + pol([0])), 'Polinomial([100, 0])')
        self.assertEqual(
            repr(pol([100, 0]) + pol([-10])), 'Polinomial([100, -10])')
        self.assertEqual(
            repr(pol([100, 0]) + pol([-100, 0])), 'Polinomial([0])')

        self.assertEqual(repr(pol([123, 0]) + 100), 'Polinomial([123, 100])')
        self.assertEqual(repr(pol([0]) + 100), 'Polinomial([100])')
        self.assertEqual(repr(pol([-100]) + 100), 'Polinomial([0])')
        self.assertEqual(repr(pol([-101]) + 100), 'Polinomial([-1])')
        self.assertEqual(repr(pol([101]) + 100), 'Polinomial([201])')

    def test_radd(self):
        self.assertEqual(repr(100 + pol([123, 0])), 'Polinomial([123, 100])')
        self.assertEqual(repr(100 + pol([0])), 'Polinomial([100])')
        self.assertEqual(repr(100 + pol([-100])), 'Polinomial([0])')
        self.assertEqual(repr(100 + pol([-101])), 'Polinomial([-1])')
        self.assertEqual(repr(100 + pol([101])), 'Polinomial([201])')

    def test_sub(self):
        self.assertEqual(repr(pol([123, 0]) - 100), 'Polinomial([123, -100])')
        self.assertEqual(repr(pol([123, 100]) - 100), 'Polinomial([123, 0])')
        self.assertEqual(repr(pol([123, 101]) - 100), 'Polinomial([123, 1])')

        self.assertEqual(repr(pol([0]) - pol([0])), 'Polinomial([0])')
        self.assertEqual(repr(pol([0]) - pol([100])), 'Polinomial([-100])')
        self.assertEqual(repr(pol([100]) - pol([100])), 'Polinomial([0])')
        self.assertEqual(
            repr(pol([10, 100]) - pol([100])), 'Polinomial([10, 0])')
        self.assertEqual(
            repr(pol([100]) - pol([10, 100])), 'Polinomial([-10, 0])')
        self.assertEqual(
            repr(pol([100]) - pol([-10, 100])), 'Polinomial([10, 0])')
        self.assertEqual(
            repr(pol([100, 100]) - pol([100, 100])), 'Polinomial([0])')
        self.assertEqual(
            repr(pol([1, 100, 100]) - pol([100, 100])), 'Polinomial([1, 0, 0])')

    def test_rsub(self):
        self.assertEqual(repr(100 - pol([123, 0])), 'Polinomial([-123, 100])')
        self.assertEqual(repr(100 - pol([123, 100])), 'Polinomial([-123, 0])')
        self.assertEqual(repr(100 - pol([123, 101])), 'Polinomial([-123, -1])')

    def test_mul(self):
        self.assertEqual(repr(pol([0]) * 1), 'Polinomial([0])')
        self.assertEqual(repr(pol([1]) * 1), 'Polinomial([1])')
        self.assertEqual(repr(pol([-1]) * 1), 'Polinomial([-1])')
        self.assertEqual(repr(pol([-1]) * -1), 'Polinomial([1])')
        self.assertEqual(repr(pol([123, 0]) * 100), 'Polinomial([12300, 0])')
        self.assertEqual(repr(pol([123, 100]) * 100), 'Polinomial([12300, 10000])')
        self.assertEqual(repr(pol([123, 0]) * -100), 'Polinomial([-12300, 0])')
        self.assertEqual(repr(pol([-123, 0]) * -100), 'Polinomial([12300, 0])')

        self.assertEqual(repr(pol([0]) * pol([0])), 'Polinomial([0])')
        self.assertEqual(repr(pol([1]) * pol([1])), 'Polinomial([1])')
        self.assertEqual(repr(pol([1]) * pol([-1])), 'Polinomial([-1])')
        self.assertEqual(repr(pol([1]) * pol([1, 0])), 'Polinomial([1, 0])')
        self.assertEqual(repr(pol([1]) * pol([2, 0])), 'Polinomial([2, 0])')
        self.assertEqual(repr(pol([2]) * pol([1, 0])), 'Polinomial([2, 0])')
        self.assertEqual(repr(pol([1, 0]) * pol([1, 0])), 'Polinomial([1, 0, 0])')
        self.assertEqual(repr(pol([1, 0]) * pol([1, 1])), 'Polinomial([1, 1, 0])')
        self.assertEqual(repr(pol([1, 0]) * pol([1, -1])), 'Polinomial([1, -1, 0])')
        self.assertEqual(repr(pol([1, 0]) * pol([1, -1])), 'Polinomial([1, -1, 0])')
        self.assertEqual(repr(pol([1, 0]) * pol([1, -1])), 'Polinomial([1, -1, 0])')
        self.assertEqual(repr(pol([10, 20, 11]) * pol([12, 2, 7])), 'Polinomial([120, 260, 242, 162, 77])')
        self.assertEqual(repr(pol([4, 20, 101]) * pol([2, 0, 0, 2, 7])), 'Polinomial([8, 40, 202, 8, 68, 342, 707])')

    def test_rmul(self):
        self.assertEqual(repr(1 * pol([0])), 'Polinomial([0])')
        self.assertEqual(repr(1 * pol([1])), 'Polinomial([1])')
        self.assertEqual(repr(1 * pol([-1])), 'Polinomial([-1])')
        self.assertEqual(repr(-1 * pol([-1])), 'Polinomial([1])')
        self.assertEqual(repr(100 * pol([123, 0])), 'Polinomial([12300, 0])')
        self.assertEqual(repr(100 * pol([123, 100])), 'Polinomial([12300, 10000])')

        self.assertEqual(repr(-100 * pol([123, 0])), 'Polinomial([-12300, 0])')
        self.assertEqual(repr(-100 * pol([-123, 0])), 'Polinomial([12300, 0])')

    def test_eq(self):
        self.assertEqual(pol([0]) == 0, True)
        self.assertEqual(pol([0]) == 1, False)
        self.assertEqual(pol([1]) == 0, False)
        self.assertEqual(pol([1]) == 1, True)
        self.assertEqual(pol([123]) == 1, False)
        self.assertEqual(pol([123]) == 123, True)
        self.assertEqual(pol([1, 1]) == 1, False)
        self.assertEqual(pol([1, 1]) == 1, False)
        self.assertEqual(pol([1123, 1]) == 1, False)
        self.assertEqual(1 == pol([1123, 1]), False)

        self.assertEqual(pol([0]) == pol([0]), True)
        self.assertEqual(pol([0]) == pol([1]), False)
        self.assertEqual(pol([123]) == pol([1]), False)
        self.assertEqual(pol([123]) == pol([123]), True)
        self.assertEqual(pol([1, 2, 3]) == pol([1, 2, 3]), True)
        self.assertEqual(pol([1, 2, 3]) == pol([1, 2, 4]), False)
        self.assertEqual(pol([1, 2, 3]) == pol([1, 2, 3, 4]), False)

    def test_getAttr(self):
        self.assertEqual(pol([0]).coeffs == [0], True)
        self.assertEqual(pol([0]).coeffs == [1], False)
        self.assertEqual(pol([123]).coeffs == [123], True)
        self.assertEqual(pol([1, 2, 3]).coeffs == [1, 2, 3], True)
        self.assertEqual(pol([1, 2, 3]).coeffs == [1, 2, 4], False)

        z = [100, 200, 300]
        p = pol(z)
        coeff = p.coeffs
        self.assertEqual(z is coeff, False)
        self.assertEqual(z == coeff, True)
    
    def test_setAttr(self):
        p = pol([0])
        p.coeffs = [1]
        self.assertEqual(p == pol([1]), True)
        p.coeffs = [1, 0]
        self.assertEqual(p == pol([1, 0]), True)
        p.coeffs = [1, 100]
        self.assertEqual(p == pol([1, 100]), True)
        p.coeffs = [0, 100]
        self.assertEqual(p == pol([100]), True)
        p.coeffs = [100, 0]
        self.assertEqual(p == pol([100, 0]), True)

    def test_copyConstr(self):
        self.assertEqual(pol(pol([0])) == pol([0]), True)
        self.assertEqual(pol(pol([1])) == pol([1]), True)
        self.assertEqual(pol(pol([-1])) == pol([-1]), True)
        self.assertEqual(pol(pol([100, 0])) == pol([100, 0]), True)

if __name__ == '__main__':
    unittest.main()


def runTests():
    unittest.main()

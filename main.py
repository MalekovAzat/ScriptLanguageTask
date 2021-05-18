import test
import unittest

def main():
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
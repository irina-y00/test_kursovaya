import unittest
from HomeTest.CarouselTest import CarouselTest
from HomeTest.FilmsTest import FilmsTest
from FilmPagesTest.CatalogTest import CatalogTest
from UserTest.ProfileTest import ProfileTest
from UserTest.Registration import RegistrationTest
from UserTest.SignInTest import SignInTest
from NavbarTest.NavbarTest import NavbarTest


def runTests(testClasses):
    loader = unittest.TestLoader()
    suitesList = []
    for testClass in testClasses:
        suite = loader.loadTestsFromTestCase(testClass)
        suitesList.append(suite)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unittest.TestSuite(suitesList))


def main():
    runTests([CarouselTest, FilmsTest])
    runTests([NavbarTest])
    runTests([CatalogTest])
    runTests([ProfileTest, RegistrationTest, SignInTest])


if __name__ == '__main__':
    main()
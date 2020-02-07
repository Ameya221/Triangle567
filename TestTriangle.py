# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testInValid(self):
        self.assertEqual(classifyTriangle(255, 255, 255), 'InvalidInput')

    def testInValid2(self):
        self.assertEqual(classifyTriangle(555, 10, 150), 'InvalidInput')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(5, 10, 150), 'NotATriangle')

    def testScalene(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene')

    def testIsoceles(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'Isoceles')

    def testEquileteral2(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral')

    def testIsoceles2(self):
        self.assertEqual(classifyTriangle(5,5, 7), 'Isoceles')

    def testScalene2(self):
        self.assertEqual(classifyTriangle(23, 32, 47), 'Scalene')

    def testInValid3(self):
        self.assertEqual(classifyTriangle(5, 'a', 3), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


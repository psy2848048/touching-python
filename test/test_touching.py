# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('./')

from touching import Touching


class TouchingTestCase(TestCase):
    def setUp(self):
        self.touchingObj = Touching('p2hcblWwXOncD_YZbZv7m79yK4VeM4Qa')

    def tearDown(self):
        pass

    def test_getPointList(self):
        result = self.touchingObj.check_point('01012345678')

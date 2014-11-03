
__author__ = 'manu'

import unittest
import mock
from simple_remove import *


class MockTestCase(unittest.TestCase):

    @mock.patch('simple_remove.os.path')
    @mock.patch('simple_remove.os')
    def test_remove(self, mock_os, mock_path):
        mock_path.isfile.return_value = True
        rm("test")
        mock_os.remove.assert_called_with("test")


if __name__ == '__main__':
    unittest.main()

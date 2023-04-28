import unittest
from estimate_pi import estimate_pi, PiFileWriter
import doctest

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01)

    def testPiFileWriter(self):
        mock_file_writer = MockPiFileWriter()
        estimate = estimate_pi(1000000)
        path = '/test.txt'
        mock_file_writer.write(estimate, path)
        self.assertEqual(mock_file_writer.content(), estimate)
        self.assertEqual(mock_file_writer.file_path(), path)

    def test_estimate_pi_doctest(self):
        """
        >>> pi = estimate_pi(1000000)
        >>> pi # doctest: +ELLIPSIS
        3.1...

        >>> estimate_pi(0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
        """
        pass


class MockPiFileWriter:
    def __init__(self):
        self._content = None
        self._file_path = None

    def write(self, content, file_path):
        self._content = content
        self._file_path = file_path

    def content(self):
        return self._content

    def file_path(self):
        return self._file_path


if __name__ == '__main__':
    result = doctest.testmod()
    print(result)
    unittest.main()

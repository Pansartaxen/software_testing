import unittest
from estimate_pi import estimate_pi, PiFileWriter

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01)

    def testPiFileWriter(self):
        mock_file_writer = PiFileWriter()
        estimate = estimate_pi(1000000)
        path = '/test.txt'
        mock_file_writer.write(estimate, path)
        self.assertEqual(mock_file_writer.content(), estimate)
        self.assertEqual(mock_file_writer.file_path(), path)


if __name__ == '__main__':
    unittest.main()

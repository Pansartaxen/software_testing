import unittest
from estimate_pi import estimate_pi, PiFileWriter

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01)

class TestPiWriter(unittest.TestCase):
    def test_file_writer(self):
        fake_file_path = "fake/file/path"
        content = "1234"
        with unittest.mock.patch('__main__.__builtins__.open', unittest.mock.mock_open()) as mocked_file:
            PiFileWriter().write(content, fake_file_path)
            mocked_file.assert_called_once_with(fake_file_path, 'w', encoding='utf8')
            mocked_file().write.assert_called_once_with(content)


if __name__ == '__main__':
    unittest.main()

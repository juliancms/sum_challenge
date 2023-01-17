import io, unittest, sys

from app import printPairs

class TestApp(unittest.TestCase):

    def test_app_with_positive_integers(self):
        numbers = [1,3,4,5,2,2]
        target_sum = 4

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        printPairs(numbers, target_sum)
        sys.stdout = sys.__stdout__

        numbers_printed = capturedOutput.getvalue()

        self.assertIn('2,2', numbers_printed )
        self.assertRegex(numbers_printed, "(1,3|3,1)")

    def test_app_with_negative_integers_and_zero_integers(self):
        numbers = [1,9,5,0,20,-4,12,16,7]
        target_sum = 12

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        printPairs(numbers, target_sum)
        sys.stdout = sys.__stdout__

        numbers_printed = capturedOutput.getvalue()

        self.assertRegex(numbers_printed, "(12,0|0,12)")
        self.assertRegex(numbers_printed, "(5,7|7,5)")
        self.assertRegex(numbers_printed, "(16,-4|-4,16)")

if __name__ == '__main__':
    unittest.main()
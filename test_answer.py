import unittest
import answer as ans

class AnswerTest(unittest.TestCase):
  def setUp(self) -> None:
    pass

  def tearDown(self) -> None:
    pass

  def input_example1(self):
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    self.assertEqual(8, ans.main(N, A, X))
  
if __name__ == "__main__":
  unittest.main()
import unittest
import shunting_yard as sy

class AppendToOutputTest(unittest.TestCase):
	def test_5_plus(self):
		self.assertEqual("",sy.appendToOutput(5,"+"))
	def test_noString(self):
		self.assertEqual("+",sy.appendToOutput("","+"))
	def test_noToken_and_no_string(self):
		self.assertEqual("",sy.appendToOutput("",""))
	def test_noToken(self):
		self.assertEqual("5 ",sy.appendToOutput("5",""))

class comparePrecedenceTest(unittest.TestCase):
	def test_equal_precedence(self):
		self.assertEqual(0,sy.comparePrecedence("-","+"))
	def test_lower_precedence(self):
		self.assertEqual(-1,sy.comparePrecedence("-","*"))
	def test_higher_precedence(self):
		self.assertEqual(1,sy.comparePrecedence("*","-"))
	def test_more_than_one_op(self):
		self.assertRaises(sy.comparePrecedence("**","-"))

class isDigitTest(unittest.TestCase):
	def test_one(self):
		self.assertTrue(sy.isDigit("1"))
	def test_is_twelve_digit(self):
		self.assertFalse(sy.isDigit("12"))

class isBracketTest(unittest.TestCase):
	def test_left_bracket(self):
		self.assertTrue(sy.isLeftBracket("["))
	def test_notaBracket(self):
		self.assertFalse(sy.isLeftBracket("5"))
	def test_right_bracket(self):
		self.assertTrue(sy.isRightBracket("]"))
	def test_right_with_extraStuff(self):
		self.assertFalse(sy.isRightBracket("]asf"))

class StackTests(unittest.TestCase):
	def test_peekAtStack(self):
		stack = [1,2,3,4,5]
		self.assertEqual(1,sy.peekAtStack(stack))
	def test_popFromStack(self):
		stack = [1,2,3,4,5]
		self.assertEqual(1,sy.popFromStack(stack))
		self.assertEqual([2,3,4,5],stack)
	def test_pushToStack(self):
		stack = [1]
		self.assertEqual([2,1],sy.pushToStack(stack,2))
	def test_stackIsEmpty_onNonEmptyStack(self):
		stack = [1]
		self.assertFalse(sy.stackIsEmpty(stack))
	def test_stackIsEmpty_onEmptyStack(self):
		stack = []
		self.assertTrue(sy.stackIsEmpty(stack))


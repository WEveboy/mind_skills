import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'skills/mind_skill/scripts'))
from check_models import stock,loop,argument

class Checks(unittest.TestCase):
 def test_stock_accumulation(self):self.assertEqual(stock(100,30,20,5),150)
 def test_positive_stock_with_falling_inflow(self):self.assertEqual(stock(100,15,10,2),110)
 def test_fraction(self):self.assertEqual(str(stock(1,0.2,0.1,0.5)),'21/20')
 def test_equal_flows(self):self.assertEqual(stock(10,3,3,7),10)
 def test_bad_interval(self):
  with self.assertRaises(ValueError):stock(1,2,1,0)
 def test_overdraw(self):
  with self.assertRaises(ValueError):stock(1,0,2)
 def test_signs(self):
  self.assertEqual(loop(['+','-']),'balancing')
  self.assertEqual(loop(['-','-']),'reinforcing')
 def test_unknown_sign(self):
  with self.assertRaises(ValueError):loop(['?'])
 def test_modus_ponens(self):self.assertTrue(argument(['P','Q'],[lambda a:not a['P'] or a['Q'],lambda a:a['P']],lambda a:a['Q'])['valid'])
 def test_modus_tollens(self):self.assertTrue(argument(['P','Q'],[lambda a:not a['P'] or a['Q'],lambda a:not a['Q']],lambda a:not a['P'])['valid'])
 def test_affirming_consequent(self):self.assertEqual(argument(['P','Q'],[lambda a:not a['P'] or a['Q'],lambda a:a['Q']],lambda a:a['P'])['counterexamples'],[{'P':False,'Q':True}])
 def test_denying_antecedent(self):self.assertFalse(argument(['P','Q'],[lambda a:not a['P'] or a['Q'],lambda a:not a['P']],lambda a:not a['Q'])['valid'])
 def test_inclusive_or(self):self.assertFalse(argument(['P','Q'],[lambda a:a['P'] or a['Q'],lambda a:a['P']],lambda a:not a['Q'])['valid'])

if __name__=='__main__':unittest.main(verbosity=2)

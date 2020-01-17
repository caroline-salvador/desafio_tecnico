import unittest
from app import app_service, translate, checkNumber

class TestApp(unittest.TestCase):
		
	def test_home(self):
		app = app_service.test_client()
		response = app.get('/')
		self.assertEqual(200, response.status_code)
	
	def test_checkNumber_limit_min(self):
		self.assertIsNone(checkNumber("-99999"))
		
	def test_checkNumber_limit_max(self):
		self.assertIsNone(checkNumber("99999"))
		
	def test_checkNumber_max(self):
		self.assertIsNotNone(checkNumber( "100000"))
		
	def test_checkNumber_min(self):
		self.assertIsNotNone(checkNumber( "-100000"))
	
	def test_translate(self):
		self.assertEqual(translate("100"), "cem")
		self.assertEqual(translate("102"), "cento e dois")
		self.assertEqual(translate("1000"), "um mil")
		self.assertEqual(translate("10000"), "dez mil")
		self.assertEqual(translate("-100"), "menos cem")
		self.assertEqual(translate("23697"), "vinte e três mil e seiscentos e noventa e sete")
		self.assertEqual(translate("-345"), "menos trezentos e quarenta e cinco")
		self.assertEqual(translate("15"), "quinze")
		self.assertEqual(translate("2036"), "dois mil e trinta e seis")
		
if __name__ == '__main__':
    unittest.main()

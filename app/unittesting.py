from app import app
import unittest 
import json

class FlaskBookshelfTests(unittest.TestCase): 

	@classmethod
	def setUpClass(cls):
		pass 

	@classmethod
	def tearDownClass(cls):
		pass 

	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True 

	def tearDown(self):
		pass 

	# test 1-> registering a valid user
	def test_1_register_valid_user(self):
		print("\n\n\n")
		print("TEST CASE 1: Registering Valid User")
		body = {'name': "UnitTest", 'email': "unittest@gmail.com", 'password': "unittest"}
		result = self.app.post("/register_user", data = json.dumps(body), content_type='application/json')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result)	
		print("\n\n\n")

	# test 2 -> registering a new user with invalid email format
	def test_2_register_user_invalid_email(self):
		print("\n\n\n")
		print("TEST CASE 2: Registering user with Invalid email format\n")
		body = {'name': "UnitTest", 'email': "blahblah", 'password': "unittest"}
		result = self.app.post("/register_user", data = json.dumps(body), content_type='application/json')		
		print("Received Response:", result)
		print("Expected Response: 400")
		self.assertEqual(result.status_code, 400)		
		self.assertIsNone(result)
		print("\n\n\n")

	# test 3 -> registering an existing user
	def test_3_register_existing_user(self):
		print("\n\n\n")
		print("TEST CASE 3: Registering an existing user\n")
		body = {'name': "UnitTest", 'email': "blahblah", 'password': "unittest"}
		result = self.app.post("/register_user", data = json.dumps(body), content_type='application/json')
		print("Received Response:", result)
		print("Expected Response: 409")
		self.assertEqual(result.status_code, 409)
		print("\n\n\n")

	# test 4 -> registering a valid user with wrong METHOD
	def test_4_register_user_wrong_method(self):
		print("\n\n\n")
		print("TEST CASE 4: Registering a Valid User with Wrong Method\n")
		body = {'name': "UnitTest", 'email': "unittest@gmail.com", 'password': "unittest"}
		result = self.app.put("/register_user", data = json.dumps(body), content_type='application/json')
		print("Received Response:", result)
		print("Expected Response: 405")
		self.assertEqual(result.status_code, 405)
		self.assertIsNotNone(result)
		print("\n\n\n")

	# test 5 -> adding a valid item to the cart
	def test_5_cart_adding_valid_item(self):
		print("\n\n\n")
		print("TEST CASE 5: Adding a Valid Product\n")
		body = {"item":"Men Joggers","cost":699,"category":"food"}
		result = self.app.post("/add_to_cart", data = json.dumps(body), content_type='application/json')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)		
		self.assertIsNotNone(result)
		print("\n\n\n")

	# test 6 -> adding a spam item to the cart
	def test_6_cart_adding_invalid_item(self):
		print("\n\n\n")
		print("TEST CASE 6: Adding an Invalid Product\n")
		body = {"item":"hdws","cost":989,"category":"idk"}
		result = self.app.post("/add_to_cart", data = json.dumps(body), content_type='application/json')
		print("Received Response:", result)
		print("Expected Response: 400")
		self.assertEqual(result.status_code, 400)
		self.assertIsNotNone(result)
		print("\n\n\n")

	# test 7 -> getting cart contents
	def test_7_getting_cart_contents(self):
		print("\n\n\n")
		print("TEST CASE 7: Getting Cart Contents\n")
		result = self.app.get('/cart')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)		
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# test 8 -> Logging out without Logging In
	def test_8_logout_without_login(self):
		print("\n\n\n")
		print("TEST CASE 8: Logging Out without Logging In\n")
		result = self.app.get('/logout')
		print("Received Response:", result)
		print("Expected Response: 400")
		self.assertEqual(result.status_code, 400)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# test 9 -> loading recommendations page
	def test_9_recommend_status_code(self):
		print("\n\n\n")
		print("TEST CASE 9: Loading Recommendations Page\n")
		result = self.app.get('/recommend')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# test 10 -> LOADING OTHER WEBPAGES

	# web page 1 -> START PAGE
	def test_A_start_page(self):
		print("\n\n\nTEST CASE 10: LOADING OTHER WEBPAGES")
		print("\n\n\n")
		print("WEBPAGE 1: Loading Start Page\n")
		result = self.app.get('/') 
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 2 -> SignUp Page
	def test_B_home_page(self):
		print("\n\n\n")
		print("WEBPAGE 2: Loading SignUp Page\n")
		result = self.app.get('/signup')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 3 -> LogIn Page
	def test_C_home_page(self):
		print("\n\n\n")
		print("WEBPAGE 3: Loading LogIn Page\n")
		result = self.app.get('/login')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 4 -> Home Page
	def test_D_home_page(self):
		print("\n\n\n")
		print("WEBPAGE 4: Loading Home Page\n")
		result = self.app.get('/homepage')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 5 -> Food Page
	def test_E_food_page(self):
		print("\n\n\n")
		print("WEBPAGE 5: Loading Food Page\n")
		result = self.app.get('/eat')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 6 -> Workout Page
	def test_F_workout_page(self):
		print("\n\n\n")
		print("WEBPAGE 6: Loading Workout Page\n")
		result = self.app.get('/cult')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 7 -> Merchandise Page
	def test_G_merchandise_page(self):
		print("\n\n\n")
		print("WEBPAGE 7: Loading Merchandise Page\n")
		result = self.app.get('/merch')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 8 -> Payment Page
	def test_H_payment_page(self):
		print("\n\n\n")
		print("WEBPAGE 8: Loading Payment Page\n")
		result = self.app.get('/payment')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 9 -> Terms Page
	def test_I_terms_page(self):
		print("\n\n\n")
		print("WEBPAGE 9: Loading Terms & Conditions Page\n")
		result = self.app.get('/terms')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 10 -> Privacy Page
	def test_J_privacy_page(self):
		print("\n\n\n")
		print("WEBPAGE 10: Loading Privacy Page\n")
		result = self.app.get('/privacy')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")

	# web page 11 -> Contact Us Page
	def test_K_contact_page(self):
		print("\n\n\n")
		print("WEBPAGE 11: Loading Contact Us Page\n")
		result = self.app.get('/contact')
		print("Received Response:", result)
		print("Expected Response: 200")
		self.assertEqual(result.status_code, 200)
		self.assertIsNotNone(result.data)
		print("\n\n\n")		

if __name__ == '__main__':
	unittest.main()

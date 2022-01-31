from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
#############Start of Happy Tests########################   
        
    def test_check_char_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
        
    def test_check_capitalised_char_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'BBBBBBBBBRRRRRRRRRGGGGGGGGGOOOOOOOOOYYYYYYYYYWWWWWWWWW'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    
    def test_check_num_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'111111111222222222333333333444444444555555555666666666'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
        
    def test_check_num_and_char_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'111111111aaaaaaaaa222222222eeeeeeeeerrrrrrrrrggggggggg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    
    def test_check_num_and_char_capitalised_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'111111111eeeeeeeee222222222EEEEEEEEERRRRRRRRRGGGGGGGGG'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok') 
        
          
        
    ###############Start of Error Tests#################
        
    def test_check_CubeIsNone(self):
        parm = {'op':'check',
                'cube': None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is missing')   

    
    def test_check_CubeIsEmptyString(self):
        parm = {'op':'check',
                'cube': ''}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube cannot be an empty string')   
    
    
    #Length is less than 54  
    def test_check_LengthIsLessThan54(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrggggggggoooooooooyyyyyyyywwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is less than the required length of 54')
        
    
    
    #Length is greater than 54 
    def test_check_LengthIsGreaterThan54(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is greater than the required length of 54')
    
    
    #Given string has whitespace    
    def test_check_HasWhiteSpace(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrr rgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube has white space' )   
    
        
    #checks to ensure it has 6 unique chars, with 9 elements of each separate char  
    def test_check_01_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 10b, 8r, 9g, 9o, 9y, 9w
                'cube':'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')
        
    def test_check_02_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 8b, 10r, 9g, 9o, 9y, 9w
                'cube':'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')
        
    def test_check_03_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 9b, 8r, 10g, 9o, 9y, 9w
                'cube':'bbbbbbbbbrrrrrrrrggggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')

    def test_check_03_HasUnequalAmountOfElementsWithNums(self):
        parm = {'op':'check',
                 #cube string has 9b, 9r, 8g, 10o, 9 1's, 9w
                'cube':'bbbbbbbbbrrrrrrrrrggggggggoooooooooo111111111wwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')
        
    def test_check_04_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 9b, 9r, 9g, 8o, 10y, 9w
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggooooooooyyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')        
    
    
    def test_check_05_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 9b, 9r, 9g, 9o, 8y, 10w
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyywwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')   
        
    def test_check_06_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 10b, 9r, 9g, 9o, 9y, 8w
                'cube':'bbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars') 
    
        
    #Number of unique values doesn't equal six
    #Does not pass\returns error msg
    def test_check_HasLessThanSixUniqueValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbBBBBBBBBBgggggggggoooooooooyyyyyyyyyyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube requires more unique chars (exactly 6 are required)')
    
     
    #Has more than 6 unique characters in string
    def test_check_HasMoreThanSixUniqueValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbvvbbbbbbbgggggggggopoooooooyyyyyyyyyyyyyyyyyyxx'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube requires less unique chars (exactly 6 are required)')
      
    #Tests for symbols not permitted (recall that a-z, A-Z, and 0-9 are permitted)
    def test_check_ContainsForrbidenSymbols(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbb!!!!!!!!!eeeeeeeeerrrrrrrrrtttttttttyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube cannot contain chars including:`~!@#$%^&*()-_=+[]{}\|";:?/.>,<\'')
    
    #checks first face center with other center pieces
    def test_check_01_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbrbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
        
    #checks 2nd face center with other center pieces
    def test_check_02_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrgrggggrggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
     
    #checks 3rd face center with other center pieces   
    def test_check_03_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggogoooogooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
    
    #checks fourth face center with other center pieces
    def test_check_04_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggooooooyooyyyyoyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
    
    #checks 5th face center with other center pieces
    def test_check_05_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbwbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwbwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers')  
      
    #Test if cube is string or not
    def test_check_IsntString(self):
        parm = {'op':'check',
                'cube': 2 }
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must be a String')   
    

        
        
     
        
           
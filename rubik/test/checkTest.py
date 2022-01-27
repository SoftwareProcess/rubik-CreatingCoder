from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        ##Check to see that output is equal to 'ok' in check() function
        self.assertEqual(status, 'ok')
        
        
        #Come back and add tests that check to ensure middle pieces are separate, as well as edge pieces
        
        
        
        

    
    #Length is less than 54
    #Does not pass\returns error msg    
    def test_check_LengthIsLessThan54(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrggggggggoooooooooyyyyyyyywwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is less than the required length of 54')
        
    
    
    #Length is greater than 54 
    #Does not pass\returns error msg
    def test_check_LengthIsGreaterThan54(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is greater than the required length of 54')
    
    
    #Given string has whitespace    
    #Does not pass\returns error msg  
    def test_check_HasWhiteSpace(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrr rgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube has white space' )   
        
        
    #Number of unique values doesn't equal six
    #Does not pass\returns error msg
    def test_check_HasLessThanSixUniqueValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyyyyyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube requires more unique chars (exactly 6 are required)')
    
     
    #Has more than 6 unique characters in string
    #Does not pass\returns error msg 
    def test_check_HasMoreThanSixUniqueValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbvvbbbbbbbgggggggggopoooooooyyyyyyyyyyyyyyyyyyxx'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube requires less unique chars (exactly 6 are required)')
     
     
    
        
        
        
           
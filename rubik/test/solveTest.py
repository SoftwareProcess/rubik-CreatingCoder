import unittest
import rubik.solve as solve
import rubik.check as check 

#Dev Strat
#
#    Validate parms
#    Load parms['cube'] into cube model
#    rotate cube
#    serialize cube in string
#    return str + status of 'ok'
#    localhost:5000/rubik?op=check


class Test(unittest.TestCase):
   
            
    def test_solve_ShouldRotateValidNominalCube_RightPrime(self):
        parms = {'op':'solve',
                 'rotate':'r',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
    
    def test_solve_ShouldRotateValidNominalCube_Front(self):
        parms = {'op':'solve',
                 'rotate':'F',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    
    def test_solve_ShouldRotateValidNominalCube_FrontPrime(self):
        parms = {'op':'solve',
                 'rotate':'f',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'gyrgbybwbgogrrrybwogrbgooggbwowoywoywwybygwoyorrbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_Left(self):
        parms = {'op':'solve',
                 'rotate':'L',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'wggbbyyyrwogorrybwogrbgbogywwboowrrogwyoygryobrgwwybrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
     
    def test_solve_ShouldRotateValidNominalCube_LeftPrime(self):
        parms = {'op':'solve',
                 'rotate':'l',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'yggbbyryrwogorrybwogybgbogworrwoobwwbwywygbyogrgowyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)   
    
    
    def test_solve_ShouldRotateValidNominalCube_Back(self):
        parms = {'op':'solve',
                 'rotate':'B',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbybyrwoborrybroboggggorywoworworgrwbygyyoyrgbwybww',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
        
    def test_solve_ShouldRotateValidNominalCube_BackPrime(self):
        parms = {'op':'solve',
                 'rotate':'b',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbybyrwoworwybyroggggoborwororborwwbbygyyoyrgbwywrg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_Up(self):
        parms = {'op':'solve',
                 'rotate':'U',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'wogwbybyrogrorrybwbwobgooggbggworworybwyywogyyrgbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)  
        
        
    def test_solve_ShouldRotateValidNominalCube_UpPrime(self):
        parms = {'op':'solve',
                 'rotate':'u',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bwowbybyrbggorrybwwogbgooggogrworworygowyywbyyrgbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms) 
        
        
    def test_solve_ShouldRotateValidNominalCube_Down(self):
        parms = {'op':'solve',
                 'rotate':'D',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbyworwogorrbyrogrbgoybwbwoworoggwwybygyyorbyrwrbyg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms) 
        
        
    def test_solve_ShouldRotateValidNominalCube_DownPrime(self):
        parms = {'op':'solve',
                 'rotate':'d',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbyybwwogorroggogrbgoworbwoworbyrwwybygyyogybrwrybr',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms) 
        
        
    def test_solve_ShouldRotateValidNominalCube_Right_Twice(self):
        parms = {'op':'solve',
                 'rotate':'RR',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'ggbggbggbrrrrrrrrrgbbgbbgbbooooooooowwywwywwyyywyywyyw',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    #Rotate contains letter for rotation that isn't recoginized   
    def test_solve_ErrorMsgForInvalidRotation(self):
        parms = {'op':'solve',
                 'rotate':'z',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'status':'error: invalid rotation'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    #Rotate contains letter for rotation that isn't recoginized   
    def test_solve_ErrorMsgForInvalidRotationMultiple(self):
        parms = {'op':'solve',
                 'rotate':'Rzr',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'status':'error: invalid rotation'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_Right(self):
        parms = {'op':'solve',
                 'rotate':'R',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        }
        updatedParms = {
                'cube':'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)   
    
    
    def test_solve_ShouldRotateValidNominalCube_Right_ExampleFromSlide(self):
        parms = {'op':'solve',
                 'rotate':'R',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    #From pg 16 
    def test_solve_ShouldRotateValidNominalCube_ExampleFromSlides(self):
        parms = {'op':'solve',
                 'rotate':'B',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    
    #From pg 17 
    def test_solve_ShouldRotateValidNominalCube_ExampleFromSlides2(self):
        parms = {'op':'solve',
                 'rotate':'FLFFBUUdLfDrFLdRRdLLdRRu',
                'cube':'rbbgbobbgrgwyrywyobggrggywgoryyowowwyoobyrgwyrorrwbwob'
        }
        updatedParms = {
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    #===========================================================================
    # def test_solve_ShouldRotateValidNominalCube_EmptyRotateF(self):
    #     parms = {'op':'solve',
    #              'rotate':'',
    #             'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     }
    #     updatedParms = {
    #             'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
    #             'status':'ok'
    #     }
    #     encodedCube = solve._solve(parms)
    #     self.assertEqual(encodedCube, updatedParms)
    #===========================================================================
        
    #===========================================================================
    # def test_solve_ShouldRotateValidNominalCube_NoneType(self):
    #     parms = {'op':'solve',
    #              'rotate':None,
    #             'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     }
    #     updatedParms = {
    #             'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
    #             'status':'ok'
    #     }
    #     encodedCube = solve._solve(parms)
    #     self.assertEqual(encodedCube, updatedParms)
    #     
    # def test_solve_ShouldRotateValidNominalCube_RotateDoesntExist(self):
    #     parms = {'op':'solve',
    #             'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     }
    #     updatedParms = {
    #             'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
    #             'status':'ok'
    #     }
    #     encodedCube = solve._solve(parms)
    #     self.assertEqual(encodedCube, updatedParms)   
    #===========================================================================
    
  
    
    def test_solve_ShouldRotateValidNominalCube_MultipleTurns02(self):
        parms = {'op':'solve',
                 'rotate':'fUB',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        }
        updatedParms = {
                'cube':'wrrbbbbbbggwwrwwrwggoggoggyybbyoyroygrrryyryyooowwwboo',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
  
    
    def test_solve_ShouldRotateValidNominalCube_MultipleTurnsWithNumbers(self):
        parms = {'op':'solve',
                 'rotate':'FB',
                'cube':'111111111222222222333333333444444444555555555666666666'
        }
        updatedParms = {
                'cube':'111111111526526526333333333546546546222555444222666444',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
  
        
    def test_solve_ShouldRotateValidNominalCube_MultipleTurns01(self):
        parms = {'op':'solve',
                 'rotate':'FFU',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        }
        updatedParms = {
                'cube':'orrbbbbbbgggorrorroorggggggbbbooroorwyywyywyyyyywwwwww',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
  
        
    def test_solve_ShouldRotateValidNominalCube_BadCubeLessThan5(self):
        parms = {'op':'solve',
                 'rotate':'B',
                'cube':'ggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is less than the required length of 54')
     
    #Given string has whitespace    
    def test_check_HasWhiteSpace(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrr rgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube has white space' )   

    
    #Length is greater than 54 
    def test_check_LengthIsGreaterThan54(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is greater than the required length of 54')

    
    #checks to ensure it has 6 unique chars, with 9 elements of each separate char  
    def test_check_01_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 10b, 8r, 9g, 9o, 9y, 9w
                'cube':'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')
    
    def test_check_02_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 8b, 10r, 9g, 9o, 9y, 9w
                'cube':'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')    
    
    def test_check_03_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 9b, 8r, 10g, 9o, 9y, 9w
                'cube':'bbbbbbbbbrrrrrrrrggggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')

    def test_check_03_HasUnequalAmountOfElementsWithNums(self):
        parm = {'op':'check',
                 #cube string has 9b, 9r, 8g, 10o, 9 1's, 9w
                'cube':'bbbbbbbbbrrrrrrrrrggggggggoooooooooo111111111wwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')
        
    def test_check_04_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 9b, 9r, 9g, 8o, 10y, 9w
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggooooooooyyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')        
    
    
    def test_check_05_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 9b, 9r, 9g, 9o, 8y, 10w
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyywwwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars')   
        
    def test_check_06_HasUnequalAmountOfElements(self):
        parm = {'op':'check',
                 #cube string has 10b, 9r, 9g, 9o, 9y, 8w
                'cube':'bbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have exactly 6 unique chars, and 9 of each unique chars') 
        
        
    #Number of unique values doesn't equal six
    #Does not pass\returns error msg
    def test_check_HasLessThanSixUniqueValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbBBBBBBBBBgggggggggoooooooooyyyyyyyyyyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube requires more unique chars (exactly 6 are required)')
    
     
    #Has more than 6 unique characters in string
    def test_check_HasMoreThanSixUniqueValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbvvbbbbbbbgggggggggopoooooooyyyyyyyyyyyyyyyyyyxx'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube requires less unique chars (exactly 6 are required)')
      
    #Tests for symbols not permitted (recall that a-z, A-Z, and 0-9 are permitted)
    def test_check_ContainsForrbidenSymbols(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbb!!!!!!!!!eeeeeeeeerrrrrrrrrtttttttttyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube cannot contain chars including:`~!@#$%^&*()-_=+[]{}\|";:?/.>,<\'')
    
    #checks first face center with other center pieces
    def test_check_01_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbrbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
        
    #checks 2nd face center with other center pieces
    def test_check_02_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrgrggggrggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
     
    #checks 3rd face center with other center pieces   
    def test_check_03_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggogoooogooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
    
    #checks fourth face center with other center pieces
    def test_check_04_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggooooooyooyyyyoyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers') 
    
    #checks 5th face center with other center pieces
    def test_check_05_HasEqualCenterValues(self):
        parm = {'op':'check',
                'cube':'bbbbbbwbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwbwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must 6 unique centers')  
      
    #Test if cube is string or not
    def test_check_IsntString(self):
        parm = {'op':'check',
                'cube': 2 }
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must be a String') 
        
    
    def test_check_CubeIsNone(self):
        parm = {'op':'check',
                'cube': None}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is missing')
        
    #Failed test from A3    
    def test_check_CubeIsMissing(self):
        parm = {'op':'solve'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is missing')
        
  
        

      
    #BEGIN ITERATION 2 TESTS
        
    #Failed test from A3    
    def test_shouldIgnoreExtraneousParms(self):
        parm = {'op':'check',
                'rotate':'r',
                 'extraneousKey': 'this should be ignored',
                'cube': 'YssKjscjsjjcTssKKYKTsKKYTYTKYccYcYcjcjYKcYjjTscTsTTjTK'}
         
        updatedParms = {
                'cube':'YsYKjYcjTcsYjsKjTKKTsTKYTYTKYccYcYcjcjTKcKjjKscssTsjTs',
                'status':'ok'
        }
        encodedCube = solve._solve(parm)
        self.assertEqual(encodedCube, updatedParms) 
        
    
        
    def test_check_CubeIsEmptyString(self):
        parm = {'op':'check',
                'cube': ''}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube cannot be an empty string')   
    
    
    
    #===========================================================================
    # #plan is to move all white cross elements(except center) to the yellow face
    # def test_shouldReturnWhiteCross_WhiteOnTop(self):
    #     parm = {'op':'check',
    #             'cube': 'ryyobyrrgggroroogryryggywoboyyrobwbwbbbbyrggogwwwwwowb'}
    #        
    #     encodedCube = solve._solve(parm)
    #     #self.assertEqual(encodedCube, updatedParms)
    #     cubeString = encodedCube.get('cube')
    #     cubeList = list(cubeString)
    #     self.assertEqual(cubeList[37], cubeList[49])
    #     self.assertEqual(cubeList[39], cubeList[49])
    #     self.assertEqual(cubeList[41], cubeList[49])
    #     self.assertEqual(cubeList[43], cubeList[49])
    #===========================================================================
         
        
        #plan is to move all white cross elements(except center) to the yellow face
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBottomAtPos46(self):
        parm = {'op':'solve',
                'cube': 'bbbgbbororororoggggggggborororrorbbbwwyyywwwyywyywywyw'}
           
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'UUUFF')
        
           
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBottomAtPos48(self):
        parm = {'op':'solve',
                'cube': 'bbbgbbgggrororoorogggggbbbbrorrororowwyyywwwyyywwwyyyw'}
           
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'LL')
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBottomAtPos48_v2(self):
        parm = {'op':'solve',
                'cube': 'rorgbbggggggoroorororggbbbbbbbrororowywwywywyyywwwyyyw'}
           
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'UUULL')      
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBottomAtPos50(self):
        parm = {'op':'solve',
                'cube': 'bbbgbbbbbrororoorogggggbgggrorrororowwyyywwwywyyywwwyy'}
           
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'UURR') 
        
        
    
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBottomAtPos52(self):
        parm = {'op':'solve',
                'cube': 'ggggbbororororobbbbbbggborororrorgggywwwyyywwwywywyywy'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'UUUBB')    
        
    

    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBlueFaceAtPos1(self):
        parm = {'op':'solve',
                'cube': 'wwyyboobrgbbyrowggrorggbobwggororrgbywywywbroyobrwygyw'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'FrdRFF')  
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBlueFaceAtPos3(self):
        parm = {'op':'solve',
                'cube': 'oorwbyyyoggbbroygwwowggyrggbrwoobyrbobrwywgwyrrbbwyorg'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'UUUl')  
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBlueFaceAtPos5(self):
        parm = {'op':'solve',
                'cube': 'oyyybwrggbgwbroyrbooryggwowgryoobbgwywgwywbrrgroywbrbo'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'UUUR')
        
    
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBlueFaceAtPos7(self):
        parm = {'op':'solve',
                'cube': 'rorgbbywogrgyrogyorbybggwgwoowoorobbbwwyywbwyrgyrwrbyg'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'UUUdlFL') 
        
    
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos10(self):
        parm = {'op':'solve',
                'cube': 'rbgbbbygwowoorobgyworyggrbwgrgooygroywbwygwwybyrywrorb'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'rrdfRF')
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos12(self):
        parm = {'op':'solve',
                'cube': 'rbbbbgygyooywrgoobborrggrbwgrgooygroywrwyywwwbygywborw'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'rdfRF')
        
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos14(self):
        parm = {'op':'solve',
                'cube': 'groyboygwwgbyrwrbwrgybggbbogoroorwooowywyrywbbygbwrgyr'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'RdfRF')
        
        
    
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos16(self):
        parm = {'op':'solve',
                'cube': 'grgybrygrrywbrgwwbbgyrggybogoroorwooowowyoywwbybbwbgyr'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'dfRF')
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos19(self):
        parm = {'op':'solve',
                'cube': 'wgggbyooryrwgrybgwowyogrrbygobyorbywobgwywrwrbbybwoorg'}
            
        encodedCube = solve._solve(parm)
        #self.assertEqual(encodedCube, updatedParms)
        cubeString = encodedCube.get('cube')
        cubeList = list(cubeString)
        self.assertEqual(cubeList[37], cubeList[49])
        self.assertEqual(cubeList[39], cubeList[49])
        self.assertEqual(cubeList[41], cubeList[49])
        self.assertEqual(cubeList[43], cubeList[49])
        self.assertEqual(parm['solution'], 'BBdrBR')    
        
        
        
        
        
    
    
    
     
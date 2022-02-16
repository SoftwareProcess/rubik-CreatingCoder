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


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip('skipping this test until cube model is complete')
    #
    
    def test_solve_ShouldRotateValidNominalCube_Front(self):
    
        parm = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate':'F'
        }
        
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
        
        encodedCube = solve._solve(parm)
        #self.assertIn('status', result)
        #status = result.get('status', None)
        self.assertEqual(encodedCube, 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
    
    
    
    
    
    
    
    
    
    
    
    
        # #Here are the actual items
        # inputDict = {}
        # inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        # inputDict['rotate'] = 'F'
        # inputDict['op'] = 'solve'
        #
        # #Here are the expected results
        # expectedResult = {}
        # expectedResult['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        # expectedResult['status'] = 'ok'
        #
        # actualResult = solve._solve(inputDict)
        #
        # self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        # self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    #
    #
    #
    # @unittest.skip('skipping this test until cube model is complete')   
    # def test_solve_ShouldRotateValidNominalCube_FrontPrime(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'f'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'gyrgbybwbgogrrrybwogrbgooggbwowoywoywwybygwoyorrbwyrrb'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    #
    # @unittest.skip('skipping this test until cube model is complete')   
    # def test_solve_ShouldRotateValidNominalCube_Back(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'B'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bggwbybyrwoborrybroboggggorywoworworgrwbygyyoyrgbwybww'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    #
    # @unittest.skip('skipping this test until cube model is complete')   
    # def test_solve_ShouldRotateValidNominalCube_BackPrime(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'b'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bggwbybyrwoworwybyroggggoborwororborwwbbygyyoyrgbwywrg'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))   
    #
    # @unittest.skip('skipping this test until cube model is complete')   
    # def test_solve_ShouldRotateValidNominalCube_Right(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'R'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bggwbybybyowbrowrgogrggoyggbwoworworwwgbyyyyryrobwbrro'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
    #
    # @unittest.skip('skipping this test until cube model is complete')
    # def test_solve_ShouldRotateValidNominalCube_RightPrime(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'r'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bgywbgbyogrworbwoybgrygogggbwoworworwwobybyyoyrgbwyrrr'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    # @unittest.skip('skipping this test until cube model is complete')
    # def test_solve_ShouldRotateValidNominalCube_Left(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'L'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'wggbbyyyrwogorrybwogrbgbogywwboowrrogwyoygryobrgwwybrb'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
    #
    # @unittest.skip('skipping this test until cube model is complete')
    # def test_solve_ShouldRotateValidNominalCube_LeftPrime(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'l' #lowercase l in eclipse is weird
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'yggbbyryrwogorrybwogybgbogworrwoobwwbwywygbyogrgowyrrb'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
    #
    # @unittest.skip('skipping this test until cube model is complete')   
    # def test_solve_ShouldRotateValidNominalCube_Up(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'U'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'wogwbybyrogrorrybwbwobgooggbggworworybwyywogyyrgbwyrrb'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
    #
    #
    # @unittest.skip('skipping this test until cube model is complete')
    # def test_solve_ShouldRotateValidNominalCube_UpPrime(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'u'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bwowbybyrbggorrybwwogbgooggogrworworygowyywbyyrgbwyrrb'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
    #
    # @unittest.skip('skipping this test until cube model is complete')   
    # def test_solve_ShouldRotateValidNominalCube_Down(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'D'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bggwbyworwogorrbyrogrbgoybwbwoworoggwwybygyyorbyrwrbyg'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
    #
    # @unittest.skip('skipping this test until cube model is complete')   
    # def test_solve_ShouldRotateValidNominalCube_DownPrime(self):
    #
    #     #Here are the actual items
    #     inputDict = {}
    #     inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
    #     inputDict['rotate'] = 'd'
    #     inputDict['op'] = 'solve'
    #
    #     #Here are the expected results
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bggwbyybwwogorroggogrbgoworbwoworbyrwwybygyyogybrwrybr'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
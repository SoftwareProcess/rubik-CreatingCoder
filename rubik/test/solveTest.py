import unittest
import rubik.solve as solve

class Test(unittest.TestCase):


#Interface Analysis



    def setUp(self):
        pass

    def tearDown(self):
        pass



























    @unittest.skip('skipping this test until cube model is complete')
    #Example Red light test
    #clockwise turn 
    def test_solve_ShouldRotateValidNominalCubeF(self):
        
        #Here are the actual items
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        #Here are the expected results
        expectedResult = {}
        expectedResult['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    @unittest.skip('skipping this test until cube model is complete')
    #Front prime test, double check for valid string
    def test_solve_ShouldRotateValidNominalCube_F_Prime(self):
        
        #Here are the actual items
        inputDict = {}   
        inputDict['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        #Here are the expected results
        expectedResult = {}
        expectedResult['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
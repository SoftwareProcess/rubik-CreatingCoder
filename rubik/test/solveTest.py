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
    
    def test_solve_ShouldRotateValidNominalCube_Right(self):
    
        parm = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate':'R'
        }
        
        ##checks that status is ok
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
       
        
        
        encodedCube = solve._solve(parm)
        #self.assertIn('status', result)
        #status = result.get('status', None)
        self.assertEqual(encodedCube, 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
    
    
    
    
    
    
    
    
    
    
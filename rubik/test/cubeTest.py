
import unittest
import rubik.cube as rubik


class CubeTest(unittest.TestCase):


#Interface Analysis
    def test_front_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        encodedCube = CubeObject.front(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    
        
       
        
        
    


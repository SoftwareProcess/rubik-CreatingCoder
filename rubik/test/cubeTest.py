
import unittest
import rubik.cube as rubik


class CubeTest(unittest.TestCase):


#Interface Analysis
    def test_front_rotation(self):
        cubeBeforeRot = {
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        CubeObject = rubik.Cube()

        cubeAfterRot = {
                'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        }
        encodedCube = CubeObject.front(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    
        
       
        
        
    


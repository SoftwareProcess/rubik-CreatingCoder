
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
        
        
        
    def test_front_prime_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'gyrgbybwbgogrrrybwogrbgooggbwowoywoywwybygwoyorrbwyrrb'
        encodedCube = CubeObject.frontPrime(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    def test_right_rotation(self):
        cubeBeforeRot = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
        encodedCube = CubeObject.right(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
    
    def test_right_prime_rotation(self):
        cubeBeforeRot = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg'
        encodedCube = CubeObject.right_prime(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)    
        
    
        
       
        
        
    


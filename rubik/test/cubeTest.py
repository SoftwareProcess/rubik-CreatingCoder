
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
        encodedCube = CubeObject.rightPrime(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)    
        
    
    def test_left_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'wggbbyyyrwogorrybwogrbgbogywwboowrrogwyoygryobrgwwybrb'
        encodedCube = CubeObject.left(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)   
       
        
        
    def test_left_prime_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'yggbbyryrwogorrybwogybgbogworrwoobwwbwywygbyogrgowyrrb'
        encodedCube = CubeObject.leftPrime(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    def test_back_rotation(self):
        cubeBeforeRot = ''
        CubeObject = rubik.Cube()
        cubeAfterRot = ''
        encodedCube = CubeObject.back(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)


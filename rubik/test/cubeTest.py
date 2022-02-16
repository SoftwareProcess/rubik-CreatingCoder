
import unittest
import rubik.cube as cube


class CubeTest(unittest.TestCase):


#Interface Analysis

    def test_init_010_ShouldCreateEmptyCube(self):
        myCube = cube.Cube(cube)
        self.assertIsInstance(myCube, cube.Cube)


    def test_load(self):
        parms = {'op':'rotate',
                'cube':'BBBBBBBBBRRRRRRRRRGGGGGGGGGOOOOOOOOOYYYYYYYYYWWWWWWWWW'}
        #myCube = cube.Cube.load( parms)
        encodedCube = parms.get('cube', None)
        cubeStr = cube.Cube.load(encodedCube)
        self.assertEqual(cubeStr, 'BBBBBBBBBRRRRRRRRRGGGGGGGGGOOOOOOOOOYYYYYYYYYWWWWWWWWW')
        
    
    
        
        
        
        
        
        
        
    
        
       
        
        
    


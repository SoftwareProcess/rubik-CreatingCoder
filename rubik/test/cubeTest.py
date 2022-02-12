
import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass





    def test_init_010_ShouldCreateEmptyCube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)


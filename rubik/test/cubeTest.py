
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
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'bggwbybyrwoborrybroboggggorywoworworgrwbygyyoyrgbwybww'
        encodedCube = CubeObject.back(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    def test_back_prime_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'bggwbybyrwoworwybyroggggoborwororborwwbbygyyoyrgbwywrg'
        encodedCube = CubeObject.backPrime(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    def test_up_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'wogwbybyrogrorrybwbwobgooggbggworworybwyywogyyrgbwyrrb'
        encodedCube = CubeObject.up(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    def test_up_prime_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'bwowbybyrbggorrybwwogbgooggogrworworygowyywbyyrgbwyrrb'
        encodedCube = CubeObject.upPrime(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)


    def test_down_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'bggwbyworwogorrbyrogrbgoybwbwoworoggwwybygyyorbyrwrbyg'
        encodedCube = CubeObject.down(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    def test_down_prime_rotation(self):
        cubeBeforeRot = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        CubeObject = rubik.Cube()
        cubeAfterRot = 'bggwbyybwwogorroggogrbgoworbwoworbyrwwybygyyogybrwrybr'
        encodedCube = CubeObject.downPrime(cubeBeforeRot)
        self.assertEqual(encodedCube, cubeAfterRot)
        
        
    def test_pos46(self):
                       
        encodedCube = 'ygbgbbbrrobrorogybyooyggryggborooryywwbrywgwwowwrwbygw'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos46(encodedCube, solution)
        dataShouldEqual = ('rrbbbgobgygborooybobryggrygyogrooryybwwwywwwogrwrwbygw', 'UUUFF')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    def test_pos46_test2(self):
                       
        encodedCube = 'rgrgbrobbgoybrywoygrgbgobywrybboybrgwworywywywwogwgroo'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos46(encodedCube, solution)
        dataShouldEqual = ('bborbgbyrggryrygoygoybgobywgrwbobbrrowywywowwyrwgwgroo', 'UUUFF')
        self.assertEqual(afterMethod, dataShouldEqual)
         
    def test_pos48(self):
                       
        encodedCube = 'ybrgbogrggrbbrboowrywrgbbygbobyoyygrooywywowywgwwwgorr'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos48(encodedCube, solution)
        dataShouldEqual = ('gobbbobrgybrbrboowgrgrggbybrgyyoywyrwwywywowoygwowgorr', 'UUULL')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    
    def test_pos50(self):
                       
        encodedCube = 'gogbbowyrrrbbrbbbgygbrggyrgworyoyoybrwowywygwooyrwwwgo'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos50(encodedCube, solution)
        dataShouldEqual = ('woybbrwyrgbbbrbgogrrboggrrgygbyoyoybowywywrwooowrwgwgy', 'UUURR')
        self.assertEqual(afterMethod, dataShouldEqual)  
    
    def test_pos52(self):
                       
        encodedCube = 'ogyybboybrogorrygrobwbgyggboryoorrywgwywywbrgbgrbwowww'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos52(encodedCube, solution)
        dataShouldEqual = ('obwybboyborroroygrbggygbygorogroryywwwwwywywgbgrbwobrg', 'UUBB')
        self.assertEqual(afterMethod, dataShouldEqual)  
        
#================================Blue face=============================================
    def test_pos1(self):
                       
        encodedCube = 'wwyobbrybrogorrygbobwggbobborryoywrbgwywywgggwgrywoory'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos1(encodedCube, solution)
        dataShouldEqual = ('oggrbyyorroggrrwgbobwggborrorbyobbbrgwywywwwwgybowoyyy', 'FrdRFF')
        self.assertEqual(afterMethod, dataShouldEqual) 
        
    
    def test_pos3(self):
                       
        encodedCube = 'wgrwbgyogyowyryybrrogbggyyorrorobwoowgbwywbwbbboywrgrg'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos3(encodedCube, solution)
        dataShouldEqual = ('', 'UUUl')
        self.assertEqual(afterMethod, dataShouldEqual)
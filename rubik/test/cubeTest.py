
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
                       
        encodedCube = 'orrwbbgrbbgbyrgyowyygrggrybybwooowrorgowywgwwyyrbwboog'
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos3(encodedCube, solution)
        dataShouldEqual = ('ybwbbborborryrgyowbgrrggryogooyoryowywwwywgwgbyrgwbbog', 'UUUl')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBlueFaceAtPos5(self):
        encodedCube = 'rgoobwwyybowrrbrobogoygrrgywbyboboygbwgwywgoyrgbrwygrw'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos5(encodedCube, solution)
        dataShouldEqual = ('wbbobywywrrrorgbbogowogrygyogoboboyggwywywbwyrgrrwygrb', 'UUUR')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnBlueFaceAtPos7(self):
        encodedCube = 'gowybgywoogoorbyobwbrygrrgyworbogoybgwbbywywgrrbrwygrw'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos7(encodedCube, solution)
        dataShouldEqual = ('wrbyboygryowbrbygyogoygroyrwbrbogwybbwgwywgworogowrbrg', 'UUUdlFL')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos10(self):
        encodedCube = 'rboobboorywworybybrgbrgbogwooyrogrygwwbwyrgwgwyybwggry'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos10(encodedCube, solution)
        dataShouldEqual = ('rboobrgrrbrgyrywobogbggbyygooyrogoorwwywywgwywgbywbwbr', 'rrdfRF')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos12(self):
        encodedCube = 'wybobrgrgygbwryyobooyggbyywrbgrogbyrgwwwywooowgobwbrrr'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos12(encodedCube, solution)
        dataShouldEqual = ('rbooborrobrgyrywobogbggbyyrooyroggrbwwywywgwywyggwbwbr', 'UUUrdfRF')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos14(self):
        encodedCube = 'bbroborrowoyyrwwoyrboggyogybrwbogrrbywgwyworgwyggwbbyg'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos14(encodedCube, solution)
        dataShouldEqual = ('brgobbbygwgworyybbgoyogywrbrbobogrrrgwrwywywoygoywrwgo', 'UUURdfRF')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnRedFaceAtPos16(self):
        encodedCube = 'bybobbbywwboororwgbrgygrybrwgwgogyrrowywywobryggywogro'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos16(encodedCube, solution)
        dataShouldEqual = ('wgwobbgrwboooryrobybobgrrrrbrggogbyyywgwywoworbggwyyyw', 'UUUdfRF')
        self.assertEqual(afterMethod, dataShouldEqual) 
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos19(self):
        encodedCube = 'gyrybggrywrwwrobrobwrygowbrygrgobwboboorybyggywowwybog'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos19(encodedCube, solution)
        dataShouldEqual = ('gyrybgbrgwrwwrgywyrooogbrywwgroobgrybwbrybyggoyowwboob', 'BBdrBR')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos21(self):
        encodedCube = 'rooobryggwrrgrboybbgywgrobwrobyogryggwwbywywboywbwogry'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos21(encodedCube, solution)
        dataShouldEqual = ('wrrobroyybgygrbobgbbbogrrbwyooyogrggowrwywbwwwogywygry', 'UbdrBR')
        self.assertEqual(afterMethod, dataShouldEqual)   
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos23(self):
        encodedCube = 'obbbbrwyryoogrbgygwrrogwrbwygggoyboobwbyywywogrwgworry'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos23(encodedCube, solution)
        dataShouldEqual = ('yoobbrroowrrgrbwygbgyoggrbgbbbyoyyowrwwwywowbgggywrory', 'UBDLbl')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos25(self):
        encodedCube = 'wrgbbryowwgyyrgrorbbbygbwwgyooroyyorowrwyrbwogygbwgogb'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos25(encodedCube, solution)
        dataShouldEqual = ('yoobbrworwrryrryoobgyggbwygbbbroyyggrwwwywowbrbgowyogg', 'UUUDLbl')
        self.assertEqual(afterMethod, dataShouldEqual)   
           
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos28(self):
        encodedCube = 'grrobbrrybgyyrrboobbwggbgoobwwrobwygowroywrwwyyogwggyy'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos28(encodedCube, solution)
        dataShouldEqual = ('brrobbwrwbgyyrrgrobbgggggoyrooyoggbbwwrwywywwoboowyryy', 'lBDbLL')
        self.assertEqual(afterMethod, dataShouldEqual)  
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos30(self):
        encodedCube = 'ggbobbwrwrooyrygrrbrrogbyggbgywogwbbwwywyworyoboowyryg'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos30(encodedCube, solution)
        dataShouldEqual = ('goorbbrbbbrryrywrrbgoogoygrybogoybgwgwwwywwwygoorwbyyg', 'UBDbLL')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos32(self):
        encodedCube = 'bgoobbgrrybyorygrrobbogoygrorrgowbgwwybwywwwgoywrwbyyg'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos32(encodedCube, solution)
        dataShouldEqual = ('wrrobbyrrbgooryggrybrogrbgogoobogwboywgwywbwwbywywygry', 'UUUfdFLL')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldReturnWhiteCross_WhiteOnTop_WhiteOnGreenFaceAtPos34(self):
        encodedCube = 'ybrgbrwbbgoyyryrgrobrogrbgowgoboobwogobwywgwygywrwywry'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.pos34(encodedCube, solution)
        dataShouldEqual = ('wgogbrwryybryryrbbgooogorgbwrrbooobobwywywgwgggbrwyyyw', 'UUUDFlf')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    
    def test_shouldReturnWhiteCross_TurntoWhiteSideWhenAlignedBlue(self):
        encodedCube = 'ybrrbrgywgbobrorrrbgobgowgbggryoywoowoyryybwyyggwwwowb'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.blueAligned(encodedCube, solution)
        dataShouldEqual = ('wygrbrrbyoboyrorrrbgobgowgbggryobwogwoyryyggyywbwwwowb', 'FF')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    def test_shouldReturnWhiteCross_TurntoWhiteSideWhenAlignedRed(self):
        encodedCube = 'yywrbyrbwgrogrybooygorgoygbggryobwogwogrywbbrywrwwbowb'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.redAligned(encodedCube, solution)
        dataShouldEqual = ('yyyrbrrbyoobyrgorgwgoygowgbggryobwogworrybbbbywgwwwowr', 'RR')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldReturnWhiteCross_TurntoWhiteSideWhenAlignedGreen(self):
        encodedCube = 'yyyrbrrbyoowyryorgbgwogyogwggrgobbogrworybbbbywgwwwrow'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.greenAligned(encodedCube, solution)
        dataShouldEqual = ('yyyrbrrbyoobyrgorgwgoygowgbggryobwogworrybbbbywgwwwowr', 'BB')
        self.assertEqual(afterMethod, dataShouldEqual)      
    
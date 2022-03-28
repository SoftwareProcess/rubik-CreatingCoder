#===============================================================================
# Created March 1, 2022
# This cubeTest.py file is filled with
# tests for the cube.py file. 
# These tests were built incrementally 
#in accordance with the TDD process
# @Author: Shane Morgan
#===============================================================================
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
        
    def test_shouldReturnWhiteCross_TurntoWhiteSideWhenAlignedOrange(self):
        encodedCube = 'byyobrobyoobyrgorgwgrygrwgygowboyrggyorwybobbwwgrwwbwr'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.orangeAligned(encodedCube, solution)
        dataShouldEqual = ('yyyrbrrbyoobyrgorgwgoygowgbggryobwogworrybbbbywgwwwowr', 'LL')
        self.assertEqual(afterMethod, dataShouldEqual)
        
#======================================Start of Iteration 3 Tests================================   

    def test_shouldMoveWhite36toSideFace(self):
        encodedCube = 'goorbybbobobgrygrrrorbgygggbrrrobooowyygybygywwywwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnTop36(encodedCube, solution)
        dataShouldEqual = ('grbrbybbowoogrygrrbogbgyggywrroobrooobygygyyrwwywwwbww', 'Lul')
        self.assertEqual(afterMethod, dataShouldEqual)
        
     
    def test_shouldMoveWhite38toSideFace(self):
        encodedCube = 'brgrbrbbbyygyrorrbrogbgyyggoyogoboooygwbyoygrwwwwwwwwr'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnTop38(encodedCube, solution)
        dataShouldEqual = ('gogrbrbbbyyryrorrgyyoggyyggbrwgoboooybbgyorbrwwwwwwwwo', 'rUR')
        self.assertEqual(afterMethod, dataShouldEqual) 
        
    def test_shouldMoveWhite42toSideFace(self):
        encodedCube = 'oggbbrbbbyyoyrbrrrygbygygggrrbgooooyyrgbyoworowwwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnTop42(encodedCube, solution)
        dataShouldEqual = ('oggrbrrbbyboyrbrrrwyoygygggygygobooygobryoborbwwwwwwww', 'Fuf')
        self.assertEqual(afterMethod, dataShouldEqual)   
        
    def test_shouldMoveWhite44toSideFace(self):
        encodedCube = 'ogrobrbbrbbggrbbrryygygygggoyygoboooyrroyrbowwwywwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnTop44(encodedCube, solution)
        dataShouldEqual = ('ogyobbbbgbygrrbrrroywygygggrrygoboooboygyrborwwywwwwww', 'fUF')
        self.assertEqual(afterMethod, dataShouldEqual) 
        
    
    
    def test_shouldMoveWhite45toSideFace(self):
        encodedCube = 'yyybbggbbgowrryrrgbrrbgyrggyobgoroorbyogybooowwwwwwwwy'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnBottom45(encodedCube, solution)
        dataShouldEqual = ('orrybgybbwyyrryrrggorbgyrggyobgorooobbogyowbgbwwwwwwwy', 'luL')
        self.assertEqual(afterMethod, dataShouldEqual) 
    
    def test_shouldMoveWhite47toSideFace(self):
        encodedCube = 'rrrgbbybogyyyrrbrrboobgygggbowgoooogybryyrbgyowwwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnBottom47(encodedCube, solution)
        dataShouldEqual = ('byygbbybroyyorryrrbowbgygggrrwgoooogbyrgyrobbowgwwwwww', 'RUr')
        self.assertEqual(afterMethod, dataShouldEqual) 
    
    def test_shouldMoveWhite51toSideFace(self):
        encodedCube = 'yrggbgobbyggrrrrrrobrbgbggoyobooybogbyyyyooyrwwwwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnBottom51(encodedCube, solution)
        dataShouldEqual = ('ygbgbgobbrbgrrrrrrobwbgoggbbrgyoyoogoyyyyoroywwwwwwyww', 'bUB')
        self.assertEqual(afterMethod, dataShouldEqual)
         
    def test_shouldMoveWhite53toSideFace(self):
        encodedCube = 'wbgbbggbbogbrryrroryyrgobgbrggboroorgoyoyyoyywwwwwwyww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.whiteOnBottom53(encodedCube, solution)
        dataShouldEqual = ('yggbbggbbwborryrrywyyggoogbrrrboroorgobyyyboowwwwwwywg', 'Bub')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    
    def test_shouldMoveWhiteBottomCorner6(self):
        encodedCube = 'bgbybowbbyrybrrrrrrbygggggggyyoorooboygoybryoowwwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomLeftCorner6(encodedCube, solution)
        dataShouldEqual = ('ygbrborbbybybrrrrrgyoggggggwygoobooybooryyryobwwwwwwww', 'FUf')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteBottomCorner15(self):
        encodedCube = 'ybyobybbrgbyrrrwrrooyggggggbggooyooorbbyyyrrowwbwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomLeftCorner15(encodedCube, solution)
        dataShouldEqual = ('wrrobbbbyybyorrorroggggggggybbooyooorybryyrybwwgwwwwww', 'RUr')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteBottomCorner24(self):
        encodedCube = 'ybrobgbbbyroyrbrroyrwrgowgrgobboyyooryggygoybwwwwwwgwg'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomLeftCorner24(encodedCube, solution)
        dataShouldEqual = ('yrgobgbbbwroyrgrrobrwogoggrgbrboyyooryyyybbgowwwwwwgwy', 'BUb')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteBottomCorner33(self):
        encodedCube = 'yryobgbbboogyryrrryrbbgrggorooyoywooybrbygggbwwwwwwgww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomLeftCorner33(encodedCube, solution)
        dataShouldEqual = ('yogobgbbbyrgyryrrrwybbggggbyooroyyooorobybggrwwwwwwrww', 'LUl')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
        
    
    def test_shouldMoveWhiteBottomCorner8(self):
        encodedCube = 'ygbobgbbwyyryrybrryoybgrggggogboyoooogbbyrrrowwrwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomRightCorner8(encodedCube, solution)
        dataShouldEqual = ('yggobobboogwbryyrrryrbgrgggyogboyooobrbgyyrrywwbwwwwww', 'fuF')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    def test_shouldMoveWhiteBottomCorner17(self):
        encodedCube = 'rbyobrbbbggyyrorrwoggbgrrggyobboyooorybgyryyowwwwwwwwg'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomRightCorner17(encodedCube, solution)
        dataShouldEqual = ('yoyobrbbbggryrbrrbyowygrogggggboyooorbbyyrrgowwwwwwwwy', 'ruR')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteBottomCorner26(self):
        encodedCube = 'robobrbbbyogyryrrroggggbggwybbyoygoorryrygybowwwwwwoww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomRightCorner26(encodedCube, solution)
        dataShouldEqual = ('ryyobrbbbrobyryrrryowggrggyobbgoyoooggorybybgwwwwwwgww', 'Lul')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteBottomCorner35(self):
        encodedCube = 'yoygbrobbryyyryrrrbooggrgggbooboroowyyrbybgggbwwwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.BottomRightCorner35(encodedCube, solution)
        dataShouldEqual = ('rrwybrybbboyyryrrrryoggrgggbobboooogybgbygygoowwwwwwww', 'luL')
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    
    
    def test_shouldMoveWhiteTopLeftCorner0(self):
        encodedCube = 'wyobbrobbbybyryrrrrrgggrgggygobooooyrgyoyobbygwwwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopLeftCorner0(encodedCube, solution)
        dataShouldEqual = ('oyoobrbbbbyryryrrrgobggrgggrrgbogoooybygyoybywwwwwwwww', 'ulUL')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteTopLeftCorner9(self):
        encodedCube = 'yrbobrbbywyrgrybrrgogggrgggoyrbogoooybybyobyrwwowwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopLeftCorner9(encodedCube, solution)
        dataShouldEqual = ('oyoobrbbbbyryryrrrgobggrgggrrgbogoooybygyoybywwwwwwwww', 'ufUF')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteTopLeftCorner18(self):
        encodedCube = 'byoobrbbbyyryryrrywobbgrgggrrobogoooybggygyogwwwwwwwwr'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopLeftCorner18(encodedCube, solution)
        dataShouldEqual = ('oyoobrbbbbyryryrrrgobggrgggrrgbogoooybygyoybywwwwwwwww', 'urUR')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteTopLeftCorner27(self):
        encodedCube = 'oyrobrbbbgobyryrrryrgggyggywrgoogrooobogybybywwwwwwbww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopLeftCorner27(encodedCube, solution)
        dataShouldEqual = ('oyoobrbbbbyryryrrrgobggrgggrrgbogoooybygyoybywwwwwwwww', 'ubUB')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    
    
    
    def test_shouldMoveWhiteTopRightCorner2(self):
        encodedCube = 'oywobbbboryyoryyrrbyrggrggggrgbogoooyorgyrybbwwbwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopRightCorner2(encodedCube, solution)
        dataShouldEqual = ('oyoobrbbbbyryryrrrgobggrgggrrgbogoooybygyoybywwwwwwwww', 'URur')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteTopRightCorner11(self):
        encodedCube = 'brrobrbbbyywyrbrroggrogrggggyobogoooyyrbyoygbwwwwwwwwy'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopRightCorner11(encodedCube, solution)
        dataShouldEqual = ('yrrobrbbbyyoyryrrryyoggrgggbogbogoooybgbyorgbwwwwwwwww', 'UBub')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteTopRightCorner20(self):
        encodedCube = 'rogobrbbbyyoyryrrryywgggggoobbrogyoogbgryoybrwwwwwwbww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopRightCorner20(encodedCube, solution)
        dataShouldEqual = ('yrrobrbbbyyoyryrrryyoggrgggbogbogoooybgbyorgbwwwwwwwww', 'ULul')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    def test_shouldMoveWhiteTopRightCorner29(self):
        encodedCube = 'bogybrrbborryryrrryyoggrgggbowboooogybbbygogyywwwwwwww'  
        solution = ""
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.TopRightCorner29(encodedCube, solution)
        dataShouldEqual = ('yrrobrbbbyyoyryrrryyoggrgggbogbogoooybgbyorgbwwwwwwwww', 'UFuf')
        self.assertEqual(afterMethod, dataShouldEqual)
        
    
    def test_checkCornersAreSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'  
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.CornersAreSolved(encodedCube)
        dataShouldEqual = (True)
        self.assertEqual(afterMethod, dataShouldEqual)
        
        
    def test_checkCornersAreSolved(self):
        encodedCube = 'wboobywwbboorrryygygwbgyobygrbgogggbrwgwybryyoorrworww'  
        CubeObject = rubik.Cube()
        afterMethod = CubeObject.CornersAreSolved(encodedCube)
        dataShouldEqual = (False)
        self.assertEqual(afterMethod, dataShouldEqual)
    
    
        
    
        
    
    
        
    
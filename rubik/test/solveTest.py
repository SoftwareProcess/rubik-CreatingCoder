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
#    localhost:5000/rubik?op=check


class Test(unittest.TestCase):
   
            
    def test_solve_ShouldRotateValidNominalCube_RightPrime(self):
        parms = {'op':'solve',
                 'rotate':'r',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
    
    def test_solve_ShouldRotateValidNominalCube_Front(self):
        parms = {'op':'solve',
                 'rotate':'F',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    
    def test_solve_ShouldRotateValidNominalCube_FrontPrime(self):
        parms = {'op':'solve',
                 'rotate':'f',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'gyrgbybwbgogrrrybwogrbgooggbwowoywoywwybygwoyorrbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_Left(self):
        parms = {'op':'solve',
                 'rotate':'L',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'wggbbyyyrwogorrybwogrbgbogywwboowrrogwyoygryobrgwwybrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
     
    def test_solve_ShouldRotateValidNominalCube_LeftPrime(self):
        parms = {'op':'solve',
                 'rotate':'l',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'yggbbyryrwogorrybwogybgbogworrwoobwwbwywygbyogrgowyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)   
    
    
    def test_solve_ShouldRotateValidNominalCube_Back(self):
        parms = {'op':'solve',
                 'rotate':'B',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbybyrwoborrybroboggggorywoworworgrwbygyyoyrgbwybww',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
        
    def test_solve_ShouldRotateValidNominalCube_BackPrime(self):
        parms = {'op':'solve',
                 'rotate':'b',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbybyrwoworwybyroggggoborwororborwwbbygyyoyrgbwywrg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_Up(self):
        parms = {'op':'solve',
                 'rotate':'U',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'wogwbybyrogrorrybwbwobgooggbggworworybwyywogyyrgbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)  
        
        
    def test_solve_ShouldRotateValidNominalCube_UpPrime(self):
        parms = {'op':'solve',
                 'rotate':'u',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bwowbybyrbggorrybwwogbgooggogrworworygowyywbyyrgbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms) 
        
        
    def test_solve_ShouldRotateValidNominalCube_Down(self):
        parms = {'op':'solve',
                 'rotate':'D',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbyworwogorrbyrogrbgoybwbwoworoggwwybygyyorbyrwrbyg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms) 
        
        
    def test_solve_ShouldRotateValidNominalCube_DownPrime(self):
        parms = {'op':'solve',
                 'rotate':'d',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bggwbyybwwogorroggogrbgoworbwoworbyrwwybygyyogybrwrybr',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms) 
        
        
    def test_solve_ShouldRotateValidNominalCube_Right_Twice(self):
        parms = {'op':'solve',
                 'rotate':'RR',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'ggbggbggbrrrrrrrrrgbbgbbgbbooooooooowwywwywwyyywyywyyw',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    #Rotate contains letter for rotation that isn't recoginized   
    def test_solve_ErrorMsgForInvalidRotation(self):
        parms = {'op':'solve',
                 'rotate':'z',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'status':'error: invalid rotation'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    #Rotate contains letter for rotation that isn't recoginized   
    def test_solve_ErrorMsgForInvalidRotationMultiple(self):
        parms = {'op':'solve',
                 'rotate':'Rzr',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'status':'error: invalid rotation'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_Right(self):
        parms = {'op':'solve',
                 'rotate':'R',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        }
        updatedParms = {
                'cube':'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)   
    
    
    def test_solve_ShouldRotateValidNominalCube_Right_ExampleFromSlide(self):
        parms = {'op':'solve',
                 'rotate':'R',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    #From pg 16 
    def test_solve_ShouldRotateValidNominalCube_ExampleFromSlides(self):
        parms = {'op':'solve',
                 'rotate':'B',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    
    #From pg 17 
    def test_solve_ShouldRotateValidNominalCube_ExampleFromSlides2(self):
        parms = {'op':'solve',
                 'rotate':'FLFFBUUdLfDrFLdRRdLLdRRu',
                'cube':'rbbgbobbgrgwyrywyobggrggywgoryyowowwyoobyrgwyrorrwbwob'
        }
        updatedParms = {
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_EmptyRotateF(self):
        parms = {'op':'solve',
                 'rotate':'',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_NoneType(self):
        parms = {'op':'solve',
                 'rotate':None,
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
    def test_solve_ShouldRotateValidNominalCube_RotateDoesntExist(self):
        parms = {'op':'solve',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)   
        
    def test_solve_ShouldRotateValidNominalCube_BadCube(self):
        parms = {'op':'solve',
                 'rotate':'B',
                'cube':'ggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        }
        updatedParms = {
                'cube':'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo',
                'status':'error: cube is less than the required length of 54'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)
        
        
       
       
    
     
    
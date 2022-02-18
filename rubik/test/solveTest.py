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


class Test(unittest.TestCase):


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
                 'rotate':'b',
                'cube':'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        }
        updatedParms = {
                'cube':'wogwbybyrogrorrybwbwobgooggbggworworybwyywogyyrgbwyrrb',
                'status':'ok'
        }
        encodedCube = solve._solve(parms)
        self.assertEqual(encodedCube, updatedParms)  
    
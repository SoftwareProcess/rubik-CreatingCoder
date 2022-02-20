from rubik.check import *

class Cube:

     
    
# methods: instantiate:  inputs no input, out empty instance of cube
#          load : takes serialized string and loads it into the cube
#          get : takes content of the cube and returns it as a string


#Load cube
#Rotate cube
#Extract cube

    # #empty cube, constructor in python essentially
    # def __init__(self, cubeStr):   
    #     # input parameter: None
    #     # Output parameter: empty instance of cube
    #     self.cube = cube
    #
    #     #self.rotation = rotation
        

        
    
    # def load(self, cube):
    #     result = check._check(parms)
    #
    #     if(result == 'ok'):
    #
    #         self.cube = parms.get('cube', None)
    #
    #         return cubeStr
    #
    #     else: return "error"
    #
    #
    #
    # def get(self):
    #     #takes contest of cube and returns it as str
    #     pass
    
    
    
    
    
    def right(self):
    
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
    
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
        #face 1  BLUE CENTER
        updatedCube[2] = tempArray[47]
        updatedCube[5] = tempArray[50]
        updatedCube[8] = tempArray[53]
        #face 2 RED CENTER ROTATE
        #face 2 RED CENTER
        updatedCube[9] =  tempArray[15]
        updatedCube[10] = tempArray[12]
        updatedCube[11] = tempArray[9]
        updatedCube[12] = tempArray[16]
        updatedCube[13] = tempArray[13] #center doesn't change
        updatedCube[14] = tempArray[10]
        updatedCube[15] = tempArray[17]
        updatedCube[16] = tempArray[14]
        updatedCube[17] = tempArray[11]
        #face3 GREEN CENTER
        updatedCube[18] = tempArray[44]
        updatedCube[21] = tempArray[41]
        updatedCube[24] = tempArray[38]
        #face 4 ORANGE CENTER (no change)
        #face 5 YELLOW CENTER
        updatedCube[38] = tempArray[2] 
        updatedCube[41] = tempArray[5] 
        updatedCube[44] = tempArray[8]
    
        #face 6 WHITE CENTER
        updatedCube[47] = tempArray[24] 
        updatedCube[50] = tempArray[21]   
        updatedCube[53] = tempArray[18]  
    
        listToString = ''.join(updatedCube)
        return listToString
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
    
   



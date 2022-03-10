from rubik.check import *

class Cube:


# methods: instantiate:  inputs no input, out empty instance of cube
#          load : takes serialized string and loads it into the cube
#          get : takes content of the cube and returns it as a string

    @staticmethod
    def front(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE CENTER
        updatedCube[0] = tempArray[6] 
        updatedCube[1] = tempArray[3] 
        updatedCube[2] = tempArray[0] 
        updatedCube[3] = tempArray[7]
        updatedCube[4] = tempArray[4]
        updatedCube[5] = tempArray[1]
        updatedCube[6] = tempArray[8]
        updatedCube[7] = tempArray[5]
        updatedCube[8] = tempArray[2]
      
        #face 2 RED 
        updatedCube[9] = tempArray[42]
        updatedCube[12] = tempArray[43]
        updatedCube[15] = tempArray[44]
      
        #face 3 GREEN No change
      
        #face 4 ORANGE CENTER ROTATE
        updatedCube[29] = tempArray[45]
        updatedCube[32] = tempArray[46]
        updatedCube[35] = tempArray[47]
      
        #face 5 YELLOW CENTER
        updatedCube[42] = tempArray[35] 
        updatedCube[43] = tempArray[32] 
        updatedCube[44] = tempArray[29]
      
        #face 6 WHITE CENTER
        updatedCube[45] = tempArray[15] 
        updatedCube[46] = tempArray[12]   
        updatedCube[47] = tempArray[9]   
          
      
        listToString = ''.join(updatedCube)
        return listToString
     
     
    
    
    
    
    
    
    

        
 
   



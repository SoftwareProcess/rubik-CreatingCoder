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
     
     
    @staticmethod   
    def frontPrime(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE CENTER
        updatedCube[0] = tempArray[2] 
        updatedCube[1] = tempArray[5] 
        updatedCube[2] = tempArray[8] 
        updatedCube[3] = tempArray[1]
        updatedCube[4] = tempArray[4]
        updatedCube[5] = tempArray[7]
        updatedCube[6] = tempArray[0]
        updatedCube[7] = tempArray[3]
        updatedCube[8] = tempArray[6]
      
        #face 2 RED 
        updatedCube[9] = tempArray[47]
        updatedCube[12] = tempArray[46]
        updatedCube[15] = tempArray[45]
      
        #face 3 GREEN No change
      
        #face 4 ORANGE CENTER ROTATE
        updatedCube[29] = tempArray[44]
        updatedCube[32] = tempArray[43]
        updatedCube[35] = tempArray[42]
      
      
        #face 5 YELLOW CENTER
        updatedCube[42] = tempArray[9] 
        updatedCube[43] = tempArray[12] 
        updatedCube[44] = tempArray[15]
      
        #face 6 WHITE CENTER
        updatedCube[45] = tempArray[29] 
        updatedCube[46] = tempArray[32]   
        updatedCube[47] = tempArray[35]
             
          
        listToString = ''.join(updatedCube)
        return listToString
    
    
    @staticmethod
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
    
    
    
    @staticmethod
    def rightPrime(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        updatedCube[2] = tempArray[38]
        updatedCube[5] = tempArray[41]
        updatedCube[8] = tempArray[44]
      
        #face 2 RED CENTER ROTATE
        #face 2 RED CENTER
        updatedCube[9] =  tempArray[11]
        updatedCube[10] = tempArray[14]
        updatedCube[11] = tempArray[17]
        updatedCube[12] = tempArray[10]
        updatedCube[13] = tempArray[13] #center doesnt change
        updatedCube[14] = tempArray[16]
        updatedCube[15] = tempArray[9]
        updatedCube[16] = tempArray[12]
        updatedCube[17] = tempArray[15]
      
        #face3 GREEN CENTER
        updatedCube[18] = tempArray[53]
        updatedCube[21] = tempArray[50]
        updatedCube[24] = tempArray[47]
      
        #face 4 ORANGE CENTER (no change)
      
        #face 5 YELLOW CENTER
        updatedCube[38] = tempArray[24] 
        updatedCube[41] = tempArray[21] 
        updatedCube[44] = tempArray[18] 
      
        #face 6 WHITE CENTER
        updatedCube[47] = tempArray[2] 
        updatedCube[50] = tempArray[5]   
        updatedCube[53] = tempArray[8]   
      
        listToString = ''.join(updatedCube)
        return listToString
      
        
    @staticmethod
    def left(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE CENTER
        updatedCube[0] = tempArray[36]
        updatedCube[3] = tempArray[39]
        updatedCube[6] = tempArray[42]
      
        #face 2 RED No change
      
        #face3 GREEN CENTER
        updatedCube[20] = tempArray[51]
        updatedCube[23] = tempArray[48]
        updatedCube[26] = tempArray[45]
          
        #face 4 ORANGE CENTER ROTATE
      
        updatedCube[27] = tempArray[33]
        updatedCube[28] = tempArray[30]
        updatedCube[29] = tempArray[27]
        updatedCube[30] = tempArray[34]
        updatedCube[31] = tempArray[31] #no change
        updatedCube[32] = tempArray[28]
        updatedCube[33] = tempArray[35]
        updatedCube[34] = tempArray[32]
        updatedCube[35] = tempArray[29]
      
        #face 5 YELLOW CENTER
        updatedCube[36] = tempArray[26] 
        updatedCube[39] = tempArray[23] 
        updatedCube[42] = tempArray[20] 
      
        #face 6 WHITE CENTER
        updatedCube[45] = tempArray[0] 
        updatedCube[48] = tempArray[3]   
        updatedCube[51] = tempArray[6] 
      
        listToString = ''.join(updatedCube)
        return listToString
   

    @staticmethod 
    def leftPrime(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE CENTER
        updatedCube[0] = tempArray[45] 
        updatedCube[3] = tempArray[48] 
        updatedCube[6] = tempArray[51] 
        #face 2 RED No change
        #face 3 GREEN
        updatedCube[20] = tempArray[42] 
        updatedCube[23] = tempArray[39] 
        updatedCube[26] = tempArray[36]
        #face 4 ORANGE ROTATE
        updatedCube[27] = tempArray[29]
        updatedCube[28] = tempArray[32]
        updatedCube[29] = tempArray[35]
        updatedCube[30] = tempArray[28]
        updatedCube[31] = tempArray[31] #no change
        updatedCube[32] = tempArray[34]
        updatedCube[33] = tempArray[27]
        updatedCube[34] = tempArray[30]
        updatedCube[35] = tempArray[33]
        #face 5 YELLOW CENTER
        updatedCube[36] = tempArray[0] 
        updatedCube[39] = tempArray[3] 
        updatedCube[42] = tempArray[6]
        #face 6 WHITE CENTER
        updatedCube[45] = tempArray[26] 
        updatedCube[48] = tempArray[23]   
        updatedCube[51] = tempArray[20]
           
        listToString = ''.join(updatedCube)
        return listToString

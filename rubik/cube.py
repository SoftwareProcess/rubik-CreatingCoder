#===============================================================================
# Created March 1, 2022
# This cube.py file is filled with
# static methods that will be called upon 
# by the solve.py file to
# solve and rotate a rubik cube
# @Author: Shane Morgan
#===============================================================================

from rubik.check import *

class Cube:


# methods: instantiate:  inputs no input, out empty instance of cube
#          load : takes serialized string and loads it into the cube
#          get : takes content of the cube and returns it as a string


#=====================Begin of Turn methods==================
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
    
    
    @staticmethod 
    def back(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE no change
          
        #face 2  RED 
        updatedCube[11] = tempArray[53] 
        updatedCube[14] = tempArray[52]   
        updatedCube[17] = tempArray[51]
      
        #face 3 GREEN
        updatedCube[18] = tempArray[24] 
        updatedCube[19] = tempArray[21] 
        updatedCube[20] = tempArray[18]
        updatedCube[21] = tempArray[25]
        updatedCube[22] = tempArray[22]
        updatedCube[23] = tempArray[19]
        updatedCube[24] = tempArray[26]
        updatedCube[25] = tempArray[23]
        updatedCube[26] = tempArray[20]
      
        #face 4 ORANGE
        updatedCube[27] = tempArray[38] 
        updatedCube[30] = tempArray[37] 
        updatedCube[33] = tempArray[36]
      
        #face 5 YELLOW ROTATE
        updatedCube[36] = tempArray[11]
        updatedCube[37] = tempArray[14]
        updatedCube[38] = tempArray[17]
      
        #face 6 WHITE
        updatedCube[51] = tempArray[27]
        updatedCube[52] = tempArray[30]
        updatedCube[53] = tempArray[33]
          
           
        listToString = ''.join(updatedCube)
        return listToString   
    
    
    
    @staticmethod
    def backPrime(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE no change
        updatedCube[11] = tempArray[36] 
        updatedCube[14] = tempArray[37]   
        updatedCube[17] = tempArray[38]
      
        #face 3 GREEN
        updatedCube[18] = tempArray[20] 
        updatedCube[19] = tempArray[23] 
        updatedCube[20] = tempArray[26]
        updatedCube[21] = tempArray[19]
        updatedCube[22] = tempArray[22]
        updatedCube[23] = tempArray[25]
        updatedCube[24] = tempArray[18]
        updatedCube[25] = tempArray[21]
        updatedCube[26] = tempArray[24]
      
        #face 4 ORANGE
        updatedCube[27] = tempArray[51] 
        updatedCube[30] = tempArray[52] 
        updatedCube[33] = tempArray[53]
      
        #face 5 YELLOW ROTATE
        updatedCube[36] = tempArray[33]
        updatedCube[37] = tempArray[30]
        updatedCube[38] = tempArray[27]
      
        #face 6 WHITE
        updatedCube[51] = tempArray[17]
        updatedCube[52] = tempArray[14]
        updatedCube[53] = tempArray[11]
      
        listToString = ''.join(updatedCube)
        return listToString


    @staticmethod
    def up(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE 
        updatedCube[0] = tempArray[9] 
        updatedCube[1] = tempArray[10]   
        updatedCube[2] = tempArray[11]
      
        #face 2  RED 
        updatedCube[9] = tempArray[18] 
        updatedCube[10] = tempArray[19]   
        updatedCube[11] = tempArray[20]
      
        #face 3 GREEN
        updatedCube[18] = tempArray[27] 
        updatedCube[19] = tempArray[28] 
        updatedCube[20] = tempArray[29]
          
        #face 4 ORANGE
        updatedCube[27] = tempArray[0] 
        updatedCube[28] = tempArray[1] 
        updatedCube[29] = tempArray[2]
      
        #face 5 YELLOW ROTATE
        updatedCube[36] = tempArray[42]
        updatedCube[37] = tempArray[39]
        updatedCube[38] = tempArray[36]
        updatedCube[39] = tempArray[43]
        updatedCube[40] = tempArray[40]
        updatedCube[41] = tempArray[37]
        updatedCube[42] = tempArray[44]
        updatedCube[43] = tempArray[41]
        updatedCube[44] = tempArray[38]
      
        #face 6 WHITE no change
        listToString = ''.join(updatedCube)
        return listToString
    
    
    
      
    @staticmethod
    def upPrime(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
        #face 1  BLUE 
        updatedCube[0] = tempArray[27] 
        updatedCube[1] = tempArray[28]   
        updatedCube[2] = tempArray[29]
      
        #face 2  RED 
        updatedCube[9] = tempArray[0] 
        updatedCube[10] = tempArray[1]   
        updatedCube[11] = tempArray[2]
      
        #face 3 GREEN
        updatedCube[18] = tempArray[9] 
        updatedCube[19] = tempArray[10] 
        updatedCube[20] = tempArray[11]
          
        #face 4 ORANGE
        updatedCube[27] = tempArray[18] 
        updatedCube[28] = tempArray[19] 
        updatedCube[29] = tempArray[20]
      
        #face 5 YELLOW ROTATE
        updatedCube[36] = tempArray[38]
        updatedCube[37] = tempArray[41]
        updatedCube[38] = tempArray[44]
        updatedCube[39] = tempArray[37]
        updatedCube[40] = tempArray[40]
        updatedCube[41] = tempArray[43]
        updatedCube[42] = tempArray[36]
        updatedCube[43] = tempArray[39]
        updatedCube[44] = tempArray[42]
      
        #face 6 WHITE no change
        listToString = ''.join(updatedCube)
        return listToString
    
    
    @staticmethod
    def down(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
            #face 1  BLUE 
        updatedCube[6] = tempArray[33] 
        updatedCube[7] = tempArray[34]   
        updatedCube[8] = tempArray[35]
      
        #face 2  RED 
        updatedCube[15] = tempArray[6] 
        updatedCube[16] = tempArray[7]   
        updatedCube[17] = tempArray[8]
      
        #face 3 GREEN
        updatedCube[24] = tempArray[15] 
        updatedCube[25] = tempArray[16] 
        updatedCube[26] = tempArray[17]
      
        #face 4 ORANGE
        updatedCube[33] = tempArray[24] 
        updatedCube[34] = tempArray[25] 
        updatedCube[35] = tempArray[26]
      
        #face 5 YELLOW no change
      
        #face 6 WHITE rotate
        updatedCube[45] = tempArray[51] 
        updatedCube[46] = tempArray[48] 
        updatedCube[47] = tempArray[45]
      
        updatedCube[48] = tempArray[52] 
        updatedCube[49] = tempArray[49] 
        updatedCube[50] = tempArray[46]
      
        updatedCube[51] = tempArray[53] 
        updatedCube[52] = tempArray[50] 
        updatedCube[53] = tempArray[47]
      
        #face 6 WHITE no change
        listToString = ''.join(updatedCube)
        return listToString
    
    
    @staticmethod
    def downPrime(self):
          
        updatedCube = list(self)
        #makes empty array with 54 positions
        tempArray = [None] * 54
      
        #populates array with elements from cubeList
        for i in range(0, 54):
            tempArray[i] = updatedCube[i]
              
            #face 1  BLUE 
        updatedCube[6] = tempArray[15] 
        updatedCube[7] = tempArray[16]   
        updatedCube[8] = tempArray[17]
      
        #face 2  RED 
        updatedCube[15] = tempArray[24] 
        updatedCube[16] = tempArray[25]   
        updatedCube[17] = tempArray[26]
      
        #face 3 GREEN
        updatedCube[24] = tempArray[33] 
        updatedCube[25] = tempArray[34] 
        updatedCube[26] = tempArray[35]
      
        #face 4 ORANGE
        updatedCube[33] = tempArray[6] 
        updatedCube[34] = tempArray[7] 
        updatedCube[35] = tempArray[8]
      
        #face 5 YELLOW no change
      
        #face 6 WHITE rotate
        updatedCube[45] = tempArray[47] 
        updatedCube[46] = tempArray[50] 
        updatedCube[47] = tempArray[53]
      
        updatedCube[48] = tempArray[46] 
        updatedCube[49] = tempArray[49] 
        updatedCube[50] = tempArray[52]
      
        updatedCube[51] = tempArray[45] 
        updatedCube[52] = tempArray[48] 
        updatedCube[53] = tempArray[51]
      
      
        #face 6 WHITE no change
        listToString = ''.join(updatedCube)
        return listToString
      
#=====================================End of Turn Methdos======================================
    


#=====================================Start of White Cross Methods=============================
    @staticmethod
    def pos46(encodedCube, solution):
        #encodedCube = list(encodedCube)
         
        for i in range(4):
            if(encodedCube[43] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
                
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        solution = solution + 'FF'
        
        return (encodedCube, solution)
    
    
    
    @staticmethod
    def pos48(encodedCube, solution):
        #encodedCube = list(encodedCube)
         
        for i in range(4):
            if(encodedCube[39] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
                
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        solution = solution + 'LL'
        
        return (encodedCube, solution)
    
    
    
    
    @staticmethod
    def pos50(encodedCube, solution):
        #encodedCube = list(encodedCube)
         
        for i in range(4):
            if(encodedCube[41] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
                
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        solution = solution + 'RR'
        
        return (encodedCube, solution)
    
                       
    @staticmethod
    def pos52(encodedCube, solution):
         
        for i in range(4):
            if(encodedCube[37] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
                
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        solution = solution + 'BB'
        
        return (encodedCube, solution)
    
    
    
    @staticmethod
    def pos1(encodedCube, solution):
         
        for i in range(4):
            if(encodedCube[43] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        solution = solution + 'FrdRFF'
        
        return (encodedCube, solution)         
        
    @staticmethod
    def pos3(encodedCube, solution):
         
        for i in range(4):
            if(encodedCube[39] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'l'
        
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos5(encodedCube, solution):
         
        for i in range(4):
            if(encodedCube[41] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.right(encodedCube)
        encodedCube = rot
        solution = solution + 'R'
        
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos7(encodedCube, solution):
         
        for i in range(4):
            if(encodedCube[43] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot

        solution = solution + 'dlFL'
        
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos10(encodedCube, solution):
                 
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
         
        solution = solution + 'rrdfRF'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos12(encodedCube, solution):
                 
        for i in range(4):
            if(encodedCube[41] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        
        solution = solution + 'rdfRF'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos14(encodedCube, solution):
                 
        for i in range(4):
            if(encodedCube[41] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        
        solution = solution + 'RdfRF'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos16(encodedCube, solution):
                 
        for i in range(4):
            if(encodedCube[41] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        
        solution = solution + 'dfRF'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos19(encodedCube, solution):
                
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        
        solution = solution + 'BBdrBR'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos21(encodedCube, solution):
        
        for i in range(4):
            if(encodedCube[37] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        
        solution = solution + 'bdrBR'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos23(encodedCube, solution):
        
        for i in range(4):
            if(encodedCube[37] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.down(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        
        solution = solution + 'BDLbl'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos25(encodedCube, solution):
        
        for i in range(4):
            if(encodedCube[37] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.down(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        
        solution = solution + 'DLbl'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos28(encodedCube, solution):
                
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.down(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        
        solution = solution + 'lBDbLL'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos30(encodedCube, solution):
        
        for i in range(4):
            if(encodedCube[39] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.down(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
       
        
        solution = solution + 'BDbLL'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos32(encodedCube, solution):
        
        for i in range(4):
            if(encodedCube[39] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.downPrime(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
       
        
        solution = solution + 'fdFLL'
         
        return (encodedCube, solution)
    
    
    @staticmethod
    def pos34(encodedCube, solution):
        
        for i in range(4):
            if(encodedCube[39] == encodedCube[49]):
                rot = Cube.up(encodedCube)
                encodedCube = rot
                solution = solution + 'U'
                

        rot = Cube.down(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
       
        
        solution = solution + 'DFlf'
         
        return (encodedCube, solution)
    
    
    
    @staticmethod
    def blueAligned(encodedCube, solution):      
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        solution = solution + 'FF'
        return (encodedCube, solution)
    
    
    @staticmethod
    def redAligned(encodedCube, solution):      
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        solution = solution + 'RR'
        return (encodedCube, solution)
    
    
    @staticmethod
    def greenAligned(encodedCube, solution):      
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        solution = solution + 'BB'
        return (encodedCube, solution)
    
    
    @staticmethod
    def orangeAligned(encodedCube, solution):      
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        solution = solution + 'LL'
        return (encodedCube, solution)
    
#=====================================End White Cross Methods=============================

#=====================================Start of White Corner Methods=======================  
##White on top, move to side
    @staticmethod
    def whiteOnTop36(encodedCube, solution):      
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'Lul'
        return (encodedCube, solution)
    
    
    @staticmethod
    def whiteOnTop38(encodedCube, solution):      
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        solution = solution + 'rUR'
        return (encodedCube, solution)
    
    @staticmethod
    def whiteOnTop42(encodedCube, solution):      
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'Fuf'
        return (encodedCube, solution)

    @staticmethod
    def whiteOnTop44(encodedCube, solution):      
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        solution = solution + 'fUF'
        return (encodedCube, solution)
    
##White on bottom, but incorrect###  
    @staticmethod
    def whiteOnBottom45(encodedCube, solution):      
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        solution = solution + 'luL'
        return (encodedCube, solution)
     
    @staticmethod
    def whiteOnBottom47(encodedCube, solution):      
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'RUr'
        return (encodedCube, solution)
    
    @staticmethod
    def whiteOnBottom51(encodedCube, solution):      
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        solution = solution + 'bUB'
        return (encodedCube, solution)
    
    @staticmethod
    def whiteOnBottom53(encodedCube, solution):      
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'Bub'
        return (encodedCube, solution)
    
    
##Bottom left corners  
    @staticmethod
    def BottomLeftCorner6(encodedCube, solution):      
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'FUf'
        return (encodedCube, solution)
    
    @staticmethod
    def BottomLeftCorner15(encodedCube, solution):      
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'RUr'
        return (encodedCube, solution)
    
    @staticmethod
    def BottomLeftCorner24(encodedCube, solution):      
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'BUb'
        return (encodedCube, solution)
    
    @staticmethod
    def BottomLeftCorner33(encodedCube, solution):      
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'LUl'
        return (encodedCube, solution)
    
    
    
##Bottom right corners
    @staticmethod
    def BottomRightCorner8(encodedCube, solution):      
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        solution = solution + 'fuF'
        return (encodedCube, solution)
    
    @staticmethod
    def BottomRightCorner17(encodedCube, solution):      
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        solution = solution + 'ruR'
        return (encodedCube, solution)
    
    @staticmethod
    def BottomRightCorner26(encodedCube, solution):      
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'Lul'
        return (encodedCube, solution)
    
    @staticmethod
    def BottomRightCorner35(encodedCube, solution):      
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        solution = solution + 'luL'
        return (encodedCube, solution)
    
    
##Top left corners of faces, that solve##
    @staticmethod
    def TopLeftCorner0(encodedCube, solution):      
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        solution = solution + 'ulUL'
        return (encodedCube, solution)
    
    @staticmethod
    def TopLeftCorner9(encodedCube, solution):      
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        solution = solution + 'ufUF'
        return (encodedCube, solution)
    
    @staticmethod
    def TopLeftCorner18(encodedCube, solution):      
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        solution = solution + 'urUR'
        return (encodedCube, solution)
    
    @staticmethod
    def TopLeftCorner27(encodedCube, solution):      
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        solution = solution + 'ubUB'
        return (encodedCube, solution)
    
    
##Top right corners of faces, that solve##
    @staticmethod
    def TopRightCorner2(encodedCube, solution):      
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.right(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.rightPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'URur'
        return (encodedCube, solution)
    
    @staticmethod
    def TopRightCorner11(encodedCube, solution):      
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.back(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.backPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'UBub'
        return (encodedCube, solution)

    @staticmethod
    def TopRightCorner20(encodedCube, solution):      
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.left(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.leftPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'ULul'
        return (encodedCube, solution)
    
    @staticmethod
    def TopRightCorner29(encodedCube, solution):      
        rot = Cube.up(encodedCube)
        encodedCube = rot
        rot = Cube.front(encodedCube)
        encodedCube = rot
        rot = Cube.upPrime(encodedCube)
        encodedCube = rot
        rot = Cube.frontPrime(encodedCube)
        encodedCube = rot
        solution = solution + 'UFuf'
        return (encodedCube, solution)
    
    
    @staticmethod
    def CornersAreSolved(encodedCube):
        if(encodedCube[45]==encodedCube[49] and encodedCube[46]==encodedCube[49] and encodedCube[47]==encodedCube[49] and encodedCube[48]==encodedCube[49] and 
            encodedCube[50]==encodedCube[49] and encodedCube[51]==encodedCube[49] and encodedCube[52]==encodedCube[49] and encodedCube[53]==encodedCube[49] 
            and encodedCube[6] == encodedCube[4] and encodedCube[7] == encodedCube[4] and encodedCube[8] == encodedCube[4] and encodedCube[15] == encodedCube[13]
            and encodedCube[15] == encodedCube[13] and encodedCube[17] == encodedCube[13] and encodedCube[24] == encodedCube[22] and encodedCube[25] == encodedCube[22] 
            and encodedCube[26] == encodedCube[22] and encodedCube[33] == encodedCube[31] and encodedCube[34] == encodedCube[31] and encodedCube[35] == encodedCube[31]):
                return True
       
        
        
        
        
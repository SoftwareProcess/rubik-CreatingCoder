#import rubik.cube as rubik
import rubik.check as check 

# Dev Strat
#    Validate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize cube model in string
#    return string + status of 'ok'

    

def _solve(parms):
    rot = ""
    allowedLettersForRotation = 'FfRrBbLlUuDd'
    #result = {}
    #rotation =""
    
    #result = check._check(parms)
    #status = result.get('status', None) #status returns ok
    rotation = parms.get('rotate', None)
    #if (status == 'ok'):
    encodedCube = parms.get('cube',None)
    
    #NOTE: if letter is found empty, do F turn 
    if(rotation ==''):   
        rot = front(encodedCube)
        parms['cube'] = rot
        parms['status'] = 'ok'
        encodedCube = rot
        
    
        
    #for statement iterates through Rotation letters one at a time
    #and performs the necessary moves
    for letter in rotation:
    
        if (letter not in allowedLettersForRotation):
            parms['status']= 'error: invalid rotation'
            del parms['cube']
            continue
        
        if(letter == 'R'):
            #performs R rotation
            rot = right(encodedCube)
            ##sets dict after being rotated
            parms['cube'] = rot
            #sets status to ok
            parms['status'] = 'ok'
            #updates encodedCube for subsequent calls for rotations
            encodedCube = rot
    
        if(letter == 'r'):
            rot = rightPrime(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
        
        #NOTE: if letter is found empty, do F turn 
        if(letter == 'F'):   
            rot = front(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
            
            
        if(letter == 'f'):   
            rot = frontPrime(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
            
        if(letter == 'L'):   
            rot = left(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
    
        if(letter == 'l'):   
            rot = leftPrime(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
            
        if(letter == 'B'):   
            rot = back(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
            
        if(letter == 'b'):   
            rot = backPrime(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
    
        if(letter == 'U'):   
            rot = up(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
            
        if(letter == 'u'):   
            rot = upPrime(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot     
    
        if(letter == 'D'):   
            rot = down(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot
            
        if(letter == 'd'):   
            rot = downPrime(encodedCube)
            parms['cube'] = rot
            parms['status'] = 'ok'
            encodedCube = rot  
        
        
    
    #wasn't sure if reqs demanded the return var 'result', so made sure dictionary return was named 'result'   
    result = parms
    #removes op and rotate key value from dict
    del result['op']
    del result['rotate']
    #must return dictionary
    return result
###End of Solve###




 
def right(var):
    
    updatedCube = list(var)
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

    
def rightPrime(var):
    
    updatedCube = list(var)
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


def front(var):
    
    updatedCube = list(var)
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
    
    
    
def frontPrime(var):
    
    updatedCube = list(var)
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


def left(var):
    
    updatedCube = list(var)
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

 
def leftPrime(var):
    
    updatedCube = list(var)
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


 
def back(var):
    
    updatedCube = list(var)
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


def backPrime(var):
    
    updatedCube = list(var)
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


def up(var):
    
    updatedCube = list(var)
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

def upPrime(var):
    
    updatedCube = list(var)
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


def down(var):
    
    updatedCube = list(var)
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


def downPrime(var):
    
    updatedCube = list(var)
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

    




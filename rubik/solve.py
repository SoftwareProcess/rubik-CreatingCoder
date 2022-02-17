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
        
        
    for letter in rotation:
        if (letter not in allowedLettersForRotation):
            parms['status']= 'error: invalid rotation'
            del parms['cube']
            break
        
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
            #performs r rotation
            rot = rightPrime(encodedCube)
            ##sets dict after being rotated
            parms['cube'] = rot
            #sets status to ok
            parms['status'] = 'ok'
            #updates encodedCube for subsequent calls for rotations
            encodedCube = rot
        
            
    
    
    
    
    
    
    
    
    
    
    
    
        
    #removes op and rotate key value from dict
    #else
    del parms['op']
    del parms['rotate']
    #must return dictionary
    return parms




 
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
    
    
    
 
 

    




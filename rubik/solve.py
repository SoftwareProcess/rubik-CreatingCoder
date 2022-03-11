import rubik.cube as rubik
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
    CubeObject = rubik.Cube()
   
    checkVal = check._check(parms)
    status = checkVal.get('status', None)
    
    if(status =='ok'):
        checkReturnsOkCube = True
    else: checkReturnsOkCube = False
    
    
    if('rotate' in parms):
        rotation = parms.get('rotate', None)
    else:
        rotation = ''
    
    encodedCube = parms.get('cube',None)
    
    
    #THIS WILL CHANGE TO SOLVE MOVES
    #NOTE: if letter is found empty, do F turn 
    if(rotation =='' or rotation == None or 'rotate' not in parms and checkReturnsOkCube == True):
        
        #set string to bypass when type None
        ecLength = len(str(encodedCube))       
        if(encodedCube != "" and ecLength == 54):  #and str(encodedCube)== True
            rot = CubeObject.front(encodedCube)
        parms['cube'] = rot
        parms['status'] = 'ok'
        encodedCube = rot
        
        #=======================================================================
        # if(parms.get[])
        # CubeObject.moveWhiteTop(encodedCube)
        #=======================================================================
        
    
    #if statement skips over for loop if NoneType
    if(parms.get('rotate') != None and parms.get('rotate') != "" and 'rotate' in parms and checkReturnsOkCube == True):
        
        #for statement iterates through Rotation letters one at a time
        #and performs the necessary moves
        for letter in rotation:
        
            if (letter not in allowedLettersForRotation and letter !="" and letter != None):
                parms['status']= 'error: invalid rotation'
                del parms['cube']
                break
            
            #If cube is empty
            if(parms['cube'] == ''):
                parms['status']= 'error: invalid rotation'
                del parms['cube']
                break
            
            if(letter == 'R'):
                #performs R rotation
                rot = CubeObject.right(encodedCube)
                ##sets dict after being rotated
                parms['cube'] = rot
                #sets status to ok
                parms['status'] = 'ok'
                #updates encodedCube for subsequent calls for rotations
                encodedCube = rot
        
            if(letter == 'r'):
                rot = CubeObject.rightPrime(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
            
            #NOTE: if letter is found empty, do F turn 
            if(letter == 'F'):   
                rot = CubeObject.front(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
                  
            if(letter == 'f'):   
                rot = CubeObject.frontPrime(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
                
            if(letter == 'L'):   
                rot = CubeObject.left(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
        
            if(letter == 'l'):   
                rot = CubeObject.leftPrime(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
                
            if(letter == 'B'):   
                rot = CubeObject.back(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
                
            if(letter == 'b'):   
                rot = CubeObject.backPrime(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
        
            if(letter == 'U'):   
                rot = CubeObject.up(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
                
            if(letter == 'u'):   
                rot = CubeObject.upPrime(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot     
        
            if(letter == 'D'):   
                rot = CubeObject.down(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot
                
            if(letter == 'd'):   
                rot = CubeObject.downPrime(encodedCube)
                parms['cube'] = rot
                parms['status'] = 'ok'
                encodedCube = rot  
                
            
        
          
    neededKeys = [ 'op', 'cube', 'status']
    
    
    
    result = {}  
    
    for key in parms:
        if key in neededKeys:
            result[key] = parms[key] 
    
    
    #===========================================================================
    # if(result['cube']== "" ):
    #     result['status'] = status
    #     del result['cube']
    #===========================================================================
    
            
    #removes op and rotate key value from dict
    del result['op']
        
    if('rotate' in result):
        del result['rotate']

 
    if(checkReturnsOkCube == False):
        result['status'] = status
        del result['cube']
        


        
    return result
###End of Solve###


    




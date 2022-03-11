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
    
    #CREATE SOLUTION
    #THIS WILL CHANGE TO SOLVE MOVES
    #NOTE: if letter is found empty, do F turn 
    if(rotation =='' or rotation == None or 'rotate' not in parms and checkReturnsOkCube == True):
        
        #=======================================================================
        # #set string to bypass when type None
        # ecLength = len(str(encodedCube))       
        # if(encodedCube != "" and ecLength == 54): 
        #     rot = CubeObject.front(encodedCube)
        # parms['cube'] = rot
        # parms['status'] = 'ok'
        # encodedCube = rot
        #=======================================================================
        
        #=======================================================================
        # if(parms.get[])
        # CubeObject.moveWhiteTop(encodedCube)
        #=======================================================================
        

        ecLength = len(str(encodedCube))       
        if(encodedCube != "" and ecLength == 54):
            
            #===================================================================
            # rot = CubeObject.moveWhiteTop(encodedCube)
            # parms['cube'] = rot
            # parms['status'] = 'ok'
            # encodedCube = rot
            #===================================================================
            if(encodedCube[46] == encodedCube[49]):
                for i in range(4):
                    if(encodedCube[43] == encodedCube[49]):
                        rot = CubeObject.up(encodedCube)
                        parms['cube'] = rot
                        encodedCube = rot
                    
                rot = CubeObject.front(encodedCube)
                parms['cube'] = rot
                encodedCube = rot
                
                rot = CubeObject.front(encodedCube)
                parms['cube'] = rot
                encodedCube = rot
            
            
            
            
            
        
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            parms['status'] = 'ok'
    
    
    
    
    ################################end of white cross code/if statement#########################################
    
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
                
            
        
          
    neededKeys = [ 'op', 'cube', 'status', 'solution']
    
    
    
    result = {}  
    
    for key in parms:
        if key in neededKeys:
            result[key] = parms[key] 
    
    
    if('cube' in result and result['cube']== ""):
        result['status'] = status
        del result['cube']
    
            
    #removes op and rotate key value from dict
    del result['op']
        
    if('rotate' in result):
        del result['rotate']

    ##
    if(checkReturnsOkCube == False):
        result['status'] = status
        result.pop('cube', None)
        


        
    return result
###End of Solve###


    




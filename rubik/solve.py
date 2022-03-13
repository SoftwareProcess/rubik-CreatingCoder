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
    deleteCube = False
    tup =()
   
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
    

    #this solves
    if(rotation =='' or rotation == None or 'rotate' not in parms and checkReturnsOkCube == True):
         
        ecLength = len(str(encodedCube))       
        if(encodedCube != "" and ecLength == 54):
            parms['solution'] = ''
            deleteCube = True
            
            for i in range(4):
#=================Start of Logic for finding solution for white cross=================   

                if(encodedCube[46]== encodedCube[49] and encodedCube[48]== encodedCube[49] 
                   and encodedCube[50]== encodedCube[49] and encodedCube[52]== encodedCube[49]):
                        break
                    
                if(encodedCube[46] == encodedCube[49]):                
                    tup = CubeObject.pos46(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
                if(encodedCube[48] == encodedCube[49]):
                    tup = CubeObject.pos48(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                                     
                if(encodedCube[50] == encodedCube[49]):
                    tup =CubeObject.pos50(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                           
                if(encodedCube[52] == encodedCube[49]):
                    tup =CubeObject.pos52(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
    #=====================End of white face=====================================
    
    #====================blue face start========================================
                if(encodedCube[1] == encodedCube[49]):
                    tup =CubeObject.pos1(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
    #=========================================================================================   
                if(encodedCube[3] == encodedCube[49]):
                    tup =CubeObject.pos3(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
    #=========================================================================================   
                if(encodedCube[5] == encodedCube[49]):
                    tup =CubeObject.pos5(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]       
    #=========================================================================================   
                if(encodedCube[7] == encodedCube[49]):
                    tup =CubeObject.pos7(encodedCube, parms['solution']) 
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]  
    #===============================Red Face============================================                   
                if(encodedCube[10] == encodedCube[49]):
                    tup =CubeObject.pos10(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1] 
    #=========================================================================================                   
                if(encodedCube[12] == encodedCube[49]):
                    tup =CubeObject.pos12(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]     
    #=========================================================================================                   
                if(encodedCube[14] == encodedCube[49]):
                    tup =CubeObject.pos14(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]   
    #=========================================================================================                   
                if(encodedCube[16] == encodedCube[49]):
                    tup =CubeObject.pos16(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]  
    #============================Green Face============================
                if(encodedCube[19] == encodedCube[49]):
                    tup =CubeObject.pos19(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1] 
    #====================================================================================
                if(encodedCube[21] == encodedCube[49]):
                    tup =CubeObject.pos21(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1] 
    #====================================================================================
                if(encodedCube[23] == encodedCube[49]):
                    tup =CubeObject.pos23(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
    #====================================================================================
                if(encodedCube[25] == encodedCube[49]):
                    tup =CubeObject.pos25(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
    #===============================Orange Face============================================                   
                if(encodedCube[28] == encodedCube[49]):
                    tup =CubeObject.pos28(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
    #====================================================================================
                if(encodedCube[30] == encodedCube[49]):
                    tup =CubeObject.pos30(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]             
    #====================================================================================
                if(encodedCube[32] == encodedCube[49]):
                    tup =CubeObject.pos32(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]       
    #====================================================================================
                if(encodedCube[34] == encodedCube[49]):
                    tup =CubeObject.pos34(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]   

    #======================end of orange=====================
    
            #logic for flipping tiles over from yellow face to white (bottom)
            for i in range(4):
                
                if(encodedCube[1] == encodedCube[4] and encodedCube[43] == encodedCube[49]):
                    tup =CubeObject.blueAligned(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
                if(encodedCube[10] == encodedCube[13] and encodedCube[41] == encodedCube[49]):
                    tup =CubeObject.redAligned(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[19] == encodedCube[22] and encodedCube[37] == encodedCube[49]):
                    tup =CubeObject.greenAligned(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                     
                if(encodedCube[28] == encodedCube[31] and encodedCube[39] == encodedCube[49]):
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
    
    
                if(encodedCube[46]== encodedCube[49] and encodedCube[48]== encodedCube[49] 
                   and encodedCube[50]== encodedCube[49] and encodedCube[52]== encodedCube[49]):
                        break
                    
                    
                rot = CubeObject.up(encodedCube)
                parms['cube'] = rot
                encodedCube = rot
                parms['solution'] = parms['solution'] + 'U'
    
               
            parms['status'] = 'ok'
    
    
    ################################end of white cross code#########################################
    
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
                     
          
    neededKeys = [ 'op', 'rotate', 'cube', 'status', 'solution']
      
    
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
        result.pop('solution', None)
        

    
    if(deleteCube):
        result.pop('cube', None)
        
    return result
###End of Solve###


    




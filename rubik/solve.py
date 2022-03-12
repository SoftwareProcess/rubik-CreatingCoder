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
        
        ecLength = len(str(encodedCube))       
        if(encodedCube != "" and ecLength == 54):
            parms['solution'] = ''
            
            for i in range(4):
#=================Start of Logic for finding solution for white cross=================   

#==================move white cross elements from bottom to top==========================     
                if(encodedCube[46] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[43] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
    #=========================================================================================               
                if(encodedCube[48] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[39] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
    #=========================================================================================                 
                if(encodedCube[50] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[41] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'       
    #=========================================================================================                 
                if(encodedCube[52] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[37] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
    #=====================End of white face=====================================
    
    #====================blue face start========================================
                if(encodedCube[1] == encodedCube[49]):
                        
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
                    
                    rot = CubeObject.rightPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'r'    
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd'
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'        
    #=========================================================================================   
                if(encodedCube[3] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[39] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    rot = CubeObject.leftPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'l'
    #=========================================================================================   
                if(encodedCube[5] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[41] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'                
    #=========================================================================================   
                if(encodedCube[7] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[43] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd'
                    
                    rot = CubeObject.leftPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'l' 
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F' 
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'    
                    
                    
    #===============================Red Face============================================                   
                if(encodedCube[10] == encodedCube[49]):
    
                        
                    rot = CubeObject.rightPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'r'
                    
                    rot = CubeObject.rightPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'r'
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd' 
                    
                    rot = CubeObject.frontPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'f' 
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F' 
    
    
    
    #=========================================================================================                   
                if(encodedCube[12] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[41] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    
                    rot = CubeObject.rightPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'r' 
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd' 
                    
                    rot = CubeObject.frontPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'f'
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R' 
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'        
        
    #=========================================================================================                   
                if(encodedCube[14] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[41] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R' 
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd' 
                    
                    rot = CubeObject.frontPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'f'
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R' 
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'             
    
    #=========================================================================================                   
                if(encodedCube[16] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[41] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd' 
                    
                    rot = CubeObject.frontPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'f' 
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F' 
                    
    #============================Green Face============================
                if(encodedCube[19] == encodedCube[49]):
                     
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B' 
                     
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd'
                    
                    rot = CubeObject.rightPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'r'
    
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'          
    #====================================================================================
                if(encodedCube[21] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[37] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    
                    rot = CubeObject.backPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'b'
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd'
                    
                    rot = CubeObject.rightPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'r'
                    
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'
                    
    #====================================================================================
                if(encodedCube[23] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[37] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.down(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'D'
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
                    
                    rot = CubeObject.backPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'b'
                    
                    rot = CubeObject.leftPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'l'
                    
    #====================================================================================
                if(encodedCube[25] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[37] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                            
                    rot = CubeObject.down(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'D'
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
                    
                    rot = CubeObject.backPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'b'
                    
                    rot = CubeObject.leftPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'l'
    #===============================Orange Face============================================                   
                if(encodedCube[28] == encodedCube[49]):
           
                    rot = CubeObject.leftPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'l'
                    
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.down(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'D' 
                    
                    rot = CubeObject.backPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'b' 
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'
                    
    #====================================================================================
                if(encodedCube[30] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[39] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                                            
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.down(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'D'
                    
                    rot = CubeObject.backPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'b'
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L' 
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L' 
    #====================================================================================
                if(encodedCube[32] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[39] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    
                    rot = CubeObject.frontPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'f'
                    
                    rot = CubeObject.downPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'd'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L' 
                    
                    rot = CubeObject.left(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'L'                            
    
    #====================================================================================
                if(encodedCube[34] == encodedCube[49]):
                    
                    for i in range(4):
                        if(encodedCube[39] == encodedCube[49]):
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                        
                    
                    rot = CubeObject.down(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'D'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
                    
                    rot = CubeObject.leftPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'l'
                    
                    rot = CubeObject.frontPrime(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'f'    
    #======================end of orange=====================
    
            #logic for flipping tiles over from yellow face to white (bottom)
            for i in range(4):
                
                if(encodedCube[1] == encodedCube[4] and encodedCube[43] == encodedCube[49]):
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
                    
                    rot = CubeObject.front(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'F'
            
                if(encodedCube[10] == encodedCube[13] and encodedCube[41] == encodedCube[49]):
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'
                    
                    rot = CubeObject.right(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'R'
                    
                if(encodedCube[19] == encodedCube[22] and encodedCube[37] == encodedCube[49]):
                    
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
                    rot = CubeObject.back(encodedCube)
                    parms['cube'] = rot
                    encodedCube = rot
                    parms['solution'] = parms['solution'] + 'B'
                    
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
        result.pop('solution', None)
        
        


        
    return result
###End of Solve###


    




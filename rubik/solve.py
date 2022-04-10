#===============================================================================
# Created March 1, 2022
# This solve.py file is incrementally
# being built to solve a cube by giving the rotations 
# necessary to solve a rubik cube, as well as
# perform rotations on a cube if told to by the customer
# 
# @Author: Shane Morgan
#===============================================================================
import rubik.cube as rubik
import rubik.check as check 


    
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

                if(encodedCube[46]== encodedCube[49] and encodedCube[7] == encodedCube[4] and encodedCube[48]== encodedCube[49] and encodedCube[34] == encodedCube[31] 
                   and encodedCube[50]== encodedCube[49] and encodedCube[16] == encodedCube[13] and encodedCube[52]== encodedCube[49] and encodedCube[25] == encodedCube[22]):
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
    
                if(encodedCube[1] == encodedCube[49]):
                    tup =CubeObject.pos1(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]

                if(encodedCube[3] == encodedCube[49]):
                    tup =CubeObject.pos3(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]

                if(encodedCube[5] == encodedCube[49]):
                    tup =CubeObject.pos5(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]       
 
                if(encodedCube[7] == encodedCube[49]):
                    tup =CubeObject.pos7(encodedCube, parms['solution']) 
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]  
               
                if(encodedCube[10] == encodedCube[49]):
                    tup =CubeObject.pos10(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1] 
               
                if(encodedCube[12] == encodedCube[49]):
                    tup =CubeObject.pos12(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]     
                 
                if(encodedCube[14] == encodedCube[49]):
                    tup =CubeObject.pos14(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]   
              
                if(encodedCube[16] == encodedCube[49]):
                    tup =CubeObject.pos16(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]  

                if(encodedCube[19] == encodedCube[49]):
                    tup =CubeObject.pos19(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1] 

                if(encodedCube[21] == encodedCube[49]):
                    tup =CubeObject.pos21(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1] 

                if(encodedCube[23] == encodedCube[49]):
                    tup =CubeObject.pos23(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]

                if(encodedCube[25] == encodedCube[49]):
                    tup =CubeObject.pos25(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
               
                if(encodedCube[28] == encodedCube[49]):
                    tup =CubeObject.pos28(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]

                if(encodedCube[30] == encodedCube[49]):
                    tup =CubeObject.pos30(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]             

                if(encodedCube[32] == encodedCube[49]):
                    tup =CubeObject.pos32(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]       

                if(encodedCube[34] == encodedCube[49]):
                    tup =CubeObject.pos34(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]   

    
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
                    tup =CubeObject.orangeAligned(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
    
    
                if(encodedCube[46]== encodedCube[49] and encodedCube[7] == encodedCube[4] and encodedCube[48]== encodedCube[49] and encodedCube[34] == encodedCube[31] 
                   and encodedCube[50]== encodedCube[49] and encodedCube[16] == encodedCube[13] and encodedCube[52]== encodedCube[49] and encodedCube[25] == encodedCube[22]):
                        break
                    
                rot = CubeObject.up(encodedCube)
                parms['cube'] = rot
                encodedCube = rot
                parms['solution'] = parms['solution'] + 'U'
                     

##Start of White Corners
            for i in range(4):
            
                if(CubeObject.CornersAreSolved(encodedCube) == True):
                    break   
                
                if(encodedCube[36] == encodedCube[49]):
                    tup =CubeObject.whiteOnTop36(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[38] == encodedCube[49]):
                    tup =CubeObject.whiteOnTop38(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[42] == encodedCube[49]):
                    tup =CubeObject.whiteOnTop42(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[44] == encodedCube[49]):
                    tup =CubeObject.whiteOnTop44(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
#BOTTOM    
                if(encodedCube[45] == encodedCube[49] and encodedCube[6] != encodedCube[4]):
                    tup =CubeObject.whiteOnBottom45(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
                if(encodedCube[47] == encodedCube[49] and encodedCube[8] != encodedCube[4]):
                    tup =CubeObject.whiteOnBottom47(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
                if(encodedCube[51] == encodedCube[49] and encodedCube[26] != encodedCube[22]):
                    tup =CubeObject.whiteOnBottom51(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
                if(encodedCube[53] == encodedCube[49] and encodedCube[24] != encodedCube[22]):
                    tup =CubeObject.whiteOnBottom53(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
#BOTTOM LEFT CORNERS
                if(encodedCube[6] == encodedCube[49]):
                    tup =CubeObject.BottomLeftCorner6(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
                if(encodedCube[15] == encodedCube[49]):
                    tup =CubeObject.BottomLeftCorner15(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[24] == encodedCube[49]):
                    tup =CubeObject.BottomLeftCorner24(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[33] == encodedCube[49]):
                    tup =CubeObject.BottomLeftCorner33(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                    
#BOTOM RIGHT CORNERS
                if(encodedCube[8] == encodedCube[49]):
                    tup =CubeObject.BottomRightCorner8(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[17] == encodedCube[49]):
                    tup =CubeObject.BottomRightCorner17(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[26] == encodedCube[49]):
                    tup =CubeObject.BottomRightCorner26(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                if(encodedCube[35] == encodedCube[49]):
                    tup =CubeObject.BottomRightCorner35(encodedCube, parms['solution'])
                    encodedCube = tup[0]
                    parms['solution'] = tup[1]
                
                
#TOP LEFT CORNERS
                if (encodedCube[0] == encodedCube[49] or encodedCube[27] == encodedCube[49] or encodedCube[18] == encodedCube[49] or encodedCube[9] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[0] == encodedCube[49] and encodedCube[29] == encodedCube[31] and encodedCube[42] == encodedCube[4]):
                            tup =CubeObject.TopLeftCorner0(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
                            
                        if(encodedCube[9] == encodedCube[49] and encodedCube[2] == encodedCube[4] and encodedCube[44] == encodedCube[13]):
                            tup =CubeObject.TopLeftCorner9(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
                            
                        if(encodedCube[18] == encodedCube[49] and encodedCube[11] == encodedCube[13] and encodedCube[38] == encodedCube[22]):
                            tup =CubeObject.TopLeftCorner18(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
                            
                        if(encodedCube[27] == encodedCube[49] and encodedCube[36] == encodedCube[31] and encodedCube[20] == encodedCube[22]):
                            tup =CubeObject.TopLeftCorner27(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
                        
                        
                        if(encodedCube[0] != encodedCube[49] and encodedCube[27] != encodedCube[49] and encodedCube[18] != encodedCube[49] and encodedCube[9] != encodedCube[49]):
                            break
                        
                        else:
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                            

#TOP RIGHT CORNERS
                if (encodedCube[2] == encodedCube[49] or encodedCube[11] == encodedCube[49] or encodedCube[20] == encodedCube[49] or encodedCube[29] == encodedCube[49]):
                    for i in range(4):
                        if(encodedCube[2] == encodedCube[49] and encodedCube[44] == encodedCube[4] and encodedCube[9] == encodedCube[13]):
                            tup =CubeObject.TopRightCorner2(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
                
                        if(encodedCube[11]==encodedCube[49] and encodedCube[18] == encodedCube[22] and encodedCube[38] == encodedCube[13]):
                            tup =CubeObject.TopRightCorner11(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
                    
                        if(encodedCube[20] == encodedCube[49] and encodedCube[36] == encodedCube[22] and encodedCube[27] == encodedCube[31]):
                            tup =CubeObject.TopRightCorner20(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
            
                        if(encodedCube[29] == encodedCube[49] and encodedCube[0] == encodedCube[4] and encodedCube[42] == encodedCube[31]):
                            tup =CubeObject.TopRightCorner29(encodedCube, parms['solution'])
                            encodedCube = tup[0]
                            parms['solution'] = tup[1]
                        
                        if(encodedCube[2] != encodedCube[49] and encodedCube[11] != encodedCube[49] and encodedCube[20] != encodedCube[49] and encodedCube[29] != encodedCube[49]):
                            break
                        
                        else:
                            rot = CubeObject.up(encodedCube)
                            parms['cube'] = rot
                            encodedCube = rot
                            parms['solution'] = parms['solution'] + 'U'
                            
    
            parms['solution'] = CubeObject.RemoveExtraUpSpins(parms['solution'])
            parms['status'] = 'ok'

    
    ################################end of white bottom#########################################
    
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


    



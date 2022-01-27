import rubik.cube as rubik

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)  
    numOfUniqueChars = set(encodedCube)     
         
         
    if(encodedCube == None):
        result['status'] = 'error: xxx'
        
    elif(len(encodedCube) < 54):   
        result['status'] = 'error: cube is less than the required length of 54'
        
    elif(len(encodedCube) > 54):   
        result['status'] = 'error: cube is greater than the required length of 54'
        
    elif(' ' in encodedCube ):
        result['status'] = 'error: cube has white space'  
        
    elif(len(numOfUniqueChars) > 6 ):
        result['status'] = 'error: cube requires less unique chars (exactly 6 are required)'
        
    elif(len(numOfUniqueChars) < 6 ):
        result['status'] = 'error: cube requires more unique chars (exactly 6 are required)' 
        
    elif(' ' in encodedCube ):
        result['status'] = 'error: cube has white space'  
        
    else:
        result['status'] = 'ok'
        
        
        
        
        
    return result
import rubik.cube as rubik

#Shane Morgan
#szm0152@auburn.edu
#Behold, my if-elif-else statements
#I am but a humble Java user in search of a switch statement in this strange land of python

def _check(parms):
    #String that has chars 
    forbiddenChars = '`~!@#$%^&*()-_=+[]{}\|";:?/.>,<\''
    result={}
    encodedCube = parms.get('cube', None)
    cubeType = type(encodedCube)
    
    #Sets some variables under the pretense that the cube != None & encodedCube type == string
    if((encodedCube != None) & (cubeType == str)):                                             
        uniqueChars = set(encodedCube)
        uniqueCharsList = list(uniqueChars)
    
    #Ensures cube isn't None    
    if(encodedCube == None):
        result['status'] = 'error: cube is missing'
        
    #Checks if the encodedCube is a str value
    elif(cubeType != str):
        result['status'] = 'error: cube must be a String' 
    
    #Checks for empty str          
    elif(encodedCube == ''):
        result['status'] = 'error: cube cannot be an empty string'
    
    #Checks to ensure the cube string is not too small    
    elif(len(encodedCube) < 54):   
        result['status'] = 'error: cube is less than the required length of 54'
    
    #Checks to ensure the cube string is not too large      
    elif(len(encodedCube) > 54):   
        result['status'] = 'error: cube is greater than the required length of 54'
    
    #Checks for white space   
    elif(' ' in encodedCube ):
        result['status'] = 'error: cube has white space'  
     
    #Checks if there are less than 6 unique chars   
    elif(len(uniqueChars) > 6 ):
        result['status'] = 'error: cube requires less unique chars (exactly 6 are required)'
    
    #Checks if there are more than 6 unique chars      
    elif(len(uniqueChars) < 6 ):
        result['status'] = 'error: cube requires more unique chars (exactly 6 are required)' 
    
    #Checks cube for forbidden chars (only permitted chars are a-z, A-Z, 0-9)
    elif any(c in forbiddenChars for c in encodedCube):
        result['status'] = 'error: cube cannot contain chars including:`~!@#$%^&*()-_=+[]{}\|";:?/.>,<\''  

         
    #Checks center for first face to ensure there are no matching 
    elif(encodedCube[4] in (encodedCube[13], encodedCube[22], encodedCube[31], encodedCube[40], encodedCube[49])):
        result['status'] = 'error: cube must 6 unique centers'
        
    elif(encodedCube[13] in (encodedCube[22], encodedCube[31], encodedCube[40], encodedCube[49])):
        result['status'] = 'error: cube must 6 unique centers'
        
    elif(encodedCube[22] in (encodedCube[31], encodedCube[40], encodedCube[49])):
        result['status'] = 'error: cube must 6 unique centers'
        
    elif(encodedCube[31] in (encodedCube[40], encodedCube[49])):
        result['status'] = 'error: cube must 6 unique centers'
        
    elif(encodedCube[40] in (encodedCube[49])):
        result['status'] = 'error: cube must 6 unique centers'
          
    #ensuring that there are 6 different chars and that each str contains 9 of each char
    #Note: using the list method doesn't ensure a FIFO or FILO order, it instead randomizes it
    elif(encodedCube.count(uniqueCharsList[0]) != 9 ):    
        result['status'] = 'error: cube must have exactly 6 unique chars, and 9 of each unique chars' 
         
    elif(encodedCube.count(uniqueCharsList[1]) != 9 ):    
        result['status'] = 'error: cube must have exactly 6 unique chars, and 9 of each unique chars' 
    
    elif(encodedCube.count(uniqueCharsList[2]) != 9 ):    
        result['status'] = 'error: cube must have exactly 6 unique chars, and 9 of each unique chars' 
        
    elif(encodedCube.count(uniqueCharsList[3]) != 9 ):    
        result['status'] = 'error: cube must have exactly 6 unique chars, and 9 of each unique chars' 
        
    elif(encodedCube.count(uniqueCharsList[4]) != 9 ):    
        result['status'] = 'error: cube must have exactly 6 unique chars, and 9 of each unique chars' 
        
    elif(encodedCube.count(uniqueCharsList[5]) != 9 ):    
        result['status'] = 'error: cube must have exactly 6 unique chars, and 9 of each unique chars' 
    
    #if an error isn't raised in one of the above if-elif statements, else returns status of 'ok'        
    else:
        result['status'] = 'ok'
        
    return result
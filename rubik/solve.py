#import rubik.cube as rubik
import rubik.check as check 

# Dev Strat
#    Validate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize cube model in string
#    return string + status of 'ok'

    

def _solve(parms):
    result = {}
    
    result = check._check(parms)
    status = result.get('status', None)
    
    if (status == 'ok'):
        encodedCube = parms.get('cube',None) 
        
    
         
    return encodedCube


 

    #result = {}
    #result['solution'] = 'FfRrBbLlUuDd'        #example rotations
    #result['status'] = 'ok'     




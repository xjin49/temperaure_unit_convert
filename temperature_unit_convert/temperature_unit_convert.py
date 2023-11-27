"""
A python module for unit conversion for temperature.
"""

def k_to_c(temp):
    """Convert temperature from kelvin to celsius.
    
    PARAMETERS
    ----------
    temp : float
        Temperature in Kelvin. 
        
    RETURNS
    -------
    temp_c : float
        Temperature in Celsius. 
    """

    temp_c = temp - 273.15
    return temp_c

def c_to_k(temp):
    """Convert temperature from kelvin to celsius.
    
    PARAMETERS
    ----------
    temp : float
        Temperature in Celsius. 
        
    RETURNS
    -------
    temp_F : float
        Temperature in Kelvin. 
    """    
    temp_k = temp+273.15
    return temp_k

def temp_to_F(temp, C = True):
    """Convert temperature to Fahrenheit.
    
    PARAMETERS
    ----------
    temp : float
        Temperature in Celsius or Kelvin. 
    C    : bool, default: True
        If True, input temperature is in Celsius. If False, input temperature is in Kelvin.
    
    RETURNS
    -------
    temp_F : float
        Temperature in Fahrenheit. 
    """        
    if C:
        temp_F = (temp * 9/5) + 32 
    else:
        temp_c = k_to_c(temp)
        temp_F = (temp_c * 9/5) + 32 
    return temp_F
        

def temp_from_F(temp, C = True):
    """Convert temperature from Fahrenheit to Celsius or Kelvin.
    
    PARAMETERS
    ----------
    temp : float
        Temperature in Fahrenheit. 
    C    : bool, default: True
        If True, out temperature is in Celsius. If False, out temperature is in Kelvin.
    
    RETURNS
    -------
    temp_F : float
        Temperature in Celsius or Kelvin. 
    """   
    
    temp_c = (temp - 32) * 5/9
    if C:
        return(temp_c) 
    else:
        temp_k = c_to_k(temp_c)
    return temp_k

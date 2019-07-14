import numpy as np
import random

from replace_dicts import qwerty_replace_dict, phonetic_replace_dict, caps_replace_dict, complex_replace_dict

class weights:
    
    def __init__(self,weights):
        
        self.w_sum = np.sum(weights)
        self.w1 = weights[0]/self.w_sum
        self.w2 = (weights[1]+weights[0])/self.w_sum
        self.w3 = (weights[2]+weights[1])/self.w_sum
        self.w4 = (weights[3]+weights[2])/self.w_sum
        
def corrupt_text(text, error_rate=0.2, weight_ratios= [1,1,1,1]):
    
    scaled_weights = weights(weight_ratios)
    
    text = text.lower()
    text = list(text)
    num_chars = len(text)
    
    errors = np.floor(error_rate*num_chars)
    
    if num_chars<errors:
        
        raise Exception("Number of errors exceeds number of characters")
    
    idx = list(range(num_chars))
    random.shuffle(idx)
    
    error_indices = idx[0:errors]
    
    for i in error_indices:
        
        text[i] = corrupt_char(text[i], scaled_weights)
        
    if np.random.uniform()>scaled_weights.w4:
        
        text = transpose(text)
        
    return ''.join(text)

def corrupt_char(char, scaled_weights):
    
    if np.random.uniform()<scaled_weights.w1:

            char = spatial_replace(char)
        
    elif np.random.uniform()<scaled_weights.w2:
        
            char = phonetic_transform(char)
            
    elif np.random.uniform()<scaled_weights.w3:
            
            char = char*2
        
    elif np.random.uniform()<scaled_weights.w4:

            char = ''
            
    return char
            
def spatial_replace(char):
    
    idx = np.random.randint(len(qwerty_replace_dict[char]))
    char = qwerty_replace_dict[char][idx]
            
    return char

def phonetic_transform(char):
    
    """
    Consider using a neural net to do this as creating manual
    rules is pretty tedious and crap.
    """
    
    try:
        idx = np.random.randint(len(phonetic_replace_dict[char]))
        char = phonetic_replace_dict[char][idx]
        
    except:
        return char
    
    return char  

def transpose(text):
    
    text_len = len(text)
    
    idx = np.random.randint(1,text_len)
    
    swap = text[idx]
    text[idx] = text[idx-1]
    text[idx-1] = swap
    
    return text
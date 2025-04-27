

import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        alpha_list=[]
        for i in digits:
            alpha_list.append(list(digit_to_letters[i]))
        result = [''.join(pair) for pair in itertools.product(*alpha_list)]
        
        return result 
    
        

        
        


        
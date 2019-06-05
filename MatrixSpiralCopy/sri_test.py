import unittest
import random
from spiralCopy import spiralCopy
from model_solution.model_solution import spiralCopy as model_spiralCopy
from test_model import matrix_spiral_copy
import logging
import sys


class IterativeSortingTest(unittest.TestCase):


    def test_spiralCopy(self):
        log= logging.getLogger( "SomeTest.testSomething" )
        arr1 = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        log.info('testing my spiralCopy')
        self.assertEqual(spiralCopy(arr1),
                         [1, 2, 3, 4, 5, 10, 15, 20, 19, 18,
                          17, 16, 11, 6, 7, 8, 9, 14, 13, 12])
        log.info('test test_model spiralCopy')
        self.assertEqual(matrix_spiral_copy(arr1),
                         [1, 2, 3, 4, 5, 10, 15, 20, 19, 18,
                          17, 16, 11, 6, 7, 8, 9, 14, 13, 12])                          


        arr2 = [
        random.sample(range(200), 50),
        random.sample(range(200), 50),
        random.sample(range(200), 50),            
        random.sample(range(200), 50),
        random.sample(range(200), 50),
        random.sample(range(200), 50),
        random.sample(range(200), 50),  
        random.sample(range(200), 50),
        random.sample(range(200), 50),
        random.sample(range(200), 50),
        random.sample(range(200), 50), 
        random.sample(range(200), 50),
        random.sample(range(200), 50),
        random.sample(range(200), 50),
        random.sample(range(200), 50)]                                     
        res2 = matrix_spiral_copy(arr2) 
        log.info(f'{15 * 50}: my {len(spiralCopy(arr2))} model  {len(matrix_spiral_copy(arr2))}')
        self.assertEqual(spiralCopy(arr2),res2)

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )    
    unittest.main()        

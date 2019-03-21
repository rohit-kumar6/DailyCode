# 8.1 Question- Smallest Substring of All Characters
## Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

### For Example: input:  arr = ['x','y','z'], str = "xyyzyzyx" output: "zyx"
Come up with an asymptotically optimal solution and analyze the time and space complexities.


# 8.2 Question : Classic Cookie Problem
A two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s.
Each 1 represents choco chip, and each 0 represents other part of cookie.
A choco chip consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
The number of adjacent 1s forming a line determine its size.
Write a function that returns an array of the sizes of all line represented in the input matrix.

# 8.3 Question :  Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .
If a certain key is empty, it should be excluded from the output (see e in the example below).
### For Example:

input:  dict = {<br/>
     
       "Key1" : "1",
  <br/>
         "Key2" : {
   <br/>
             "a" : "2",
    <br/>
            "b" : "3",
   <br/>
             "c" : {
         <br/>
           "d" : "3",
        <br/>
            "e" : {
     <br/>
                   "" : "1"
     <br/>
               }
        <br/>
        }
       <br/>
     }
     <br/>
   }

<br/>
output: {
       <br/>
     "Key1" : "1",
    <br/>
        "Key2.a" : "2",
 <br/>
           "Key2.b" : "3",
   <br/>
         "Key2.c.d" : "3",
    <br/>
        "Key2.c.e" : "1"
   <br/>     }
<br/>

Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d
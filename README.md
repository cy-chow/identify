# pyDeclare
This program accepts C declarations that the user inputs to the command line 
or inside a file and translates them to plain English.
My primary reference for C declarations can be found [here](https://parrt.cs.usfca.edu/doc/how-to-read-C-declarations.html). 
<p>Try running
    
    python3 main.py

to get started.</p>

## Example Output

### Input
*example.txt*:
  1. short x                                                                          
  2. long\* x
  3. int \*\* x
  4. char x[]                                                                         
  5. int (\*x)[]                                                                       
  6. void x(long,int\*)                                                                
  7. int (\*(\*x)[])() 
  8. int (\*x[])()                                                                     
  9. long (\*x())[256]
  10. int (\*(\*x))[]  

### Output:
`short x: x is short`  
`long* x: x is pointer to long`  
`int ** x: x is pointer to pointer to int`  
`char x[]: x is an array of char`  
`int (*x)[]: x is pointer to an array of int`  
`void x(long,int*): x is a function taking long and int pointer returning void`  
`int (*(*x)[])(): x is pointer to an array of pointer to a function returning int`  
`int (*x[])(): x is an array of pointer to a function returning int`  
`long (*x())[256]: x is a function returning pointer to an array of size 256 of long`  
`int (*(*x))[]: x is pointer to pointer to an array of int`  

## Notes 
 - This program does not yet handle unsigned data type declarations.
 - The identifier for the declaration must be *x*, but you can change this in *definition.py*
 - *example.txt* provides sample C declarations to parse.

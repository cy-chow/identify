# Identify 
This program accepts C declarations that a user inputs to the command line 
or inside a file and translate them to plain English.
My primary reference for C declarations can be found [here](https://parrt.cs.usfca.edu/doc/how-to-read-C-declarations.html). 
<p>Try running
    
    python3 main.py

to get started.</p>

## Example Output
*example.txt*:
  1. short x                                                                          
  2. long x                                                                           
  3. char x[]                                                                         
  4. int (\*x)[]                                                                       
  5. void x(long,int\*)                                                                
  6. int (\*(\*x)[])() 
  7. int (\*x[])()                                                                     
  8. long (\*x())[256]

Output:
`short x: x is short`
`long x: x is long`
`char x[]: x is an array of char`
`int (*x)[]: x is pointer to an array of int`
`void x(long,int*): x is function taking long and int pointer returning void`
`int (*(*x)[])(): x is pointer to an array of pointer to function returning int`
`int (*x[])(): x is an array of pointer to function returning int`
`long (*x())[256]: x is function returning pointer to an array of size 256 of long` 

## Notes 
 - This program does not handle unsigned data type declarations.
 - The identifier for the declaration must be *x*, but you can change this in *definition.txt*
 - *example.txt* provides sample C declarations to parse.

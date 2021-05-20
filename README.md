# mycpyasm
a fully featured human readable python bytecode compiler

# note
this has been applied practically to my bytecodemacro project. Please look at that there for the most up to date version of this code. That project will also have documentation for the bytecode if you still want to use this project as a stand alone.

# what
This project describes a compiler for python bytecode that is fully featured (exception to this are in todo).          
it takes in a file, with a format similar to the output of the dis module and compiles it to valid (only tested in 3.9) cpython bytecode that can then be directly run on cpython.    

# how to install
just download all the files, the file Runner.py contains the main function that should be run to execute the compiler. If you chmod +x Runner.py you can execute it directly through ./Runner.py        

# how to use
run Runner.py with one argument being the name of the file.

# why this readme is so short
I am a bit busy rn, but I might come back, clean this up, and add real documentation. Although I might not, this github is more for a backup of some projects I have on my computer than any attempt at making real open source software, still feel free to use it and contribute if you want!           
if you want to have a crack at using this, although there is no documentation, i would recommend first reading through the dis modules commands and then take a peek at the test files (in the folder test).          
any files with the extension .cpyasm are the source files and the .pyc are the bytecode files.          
any file directly in the folder test (not in a subfolder) should work on the current version.            
the files in any embedded folders describe program that did work in work in progress versions but current do not work.            
I would recommend reading through the beforecodeobjects folder for examples on how cpyasm works at a basic level (these will not compile but they are good examples anyway).              

# todo:
  - test multiple cpyasm files working together, they might have to be all compiled separately and in that case we should be able to do it ourselves.
  - add documentation for how the structure of files work and which commands are modified in the asm.

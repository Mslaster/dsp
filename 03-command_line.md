# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cat - display a whole file in the command line
less - display a whole file seperately
echo - write to standard output
grep -search for text string
cp - copy a file
mv - move a file
rm -remove a file
sort - take standard input and sort alphabetically for output
pushd - temporarily look at a different folder
popd - return to previous folder
cd .. - go to parent folder
cd ~ - go to main folder


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls` -  lists files in current folder 
`ls -a`  - lists all files in current folder, including hidden ones
`ls -l`  - lists files in more detailed format
`ls -lh`  - lists files in detailed format and memory listing is Human readable
`ls -lah`  - lists all files, including hidden ones, in detailed, human readable format
`ls -t` - lists files in order of time created 
`ls -Glp` - lists files, without association to group name, in long format, only if in folder with a "/"



---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -c display by file's timestamp
ls -t display in order of time created from newest
ls -r file in reverse order
ls -u displays files by access time
ls -1 displays one entry per line

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs takes standard output and breaks it down to input for another command, which is not always possible to do through a regular | pipe. 

find . -name "*.java" | xargs grep "Stock"

Would first search through all .java files and than, within those files, search for the word "Stock"

 


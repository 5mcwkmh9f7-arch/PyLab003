# Lab 4 Reflection

## Encapsulation

Putting the drawing code inside functions made it a lot easier to work with.
Instead of writing the same loop over and over,
I wrote draw_polygon once and then used it for the eyes. 
Giving the code a name also made the file easier to read,
since draw_eye tells you what it does but a loop full of forward 
and left calls does not.

It also meant fixing a bug only took one edit.
The mouth was pointing the wrong way, and because that 
code was inside draw_mouth, fixing it once fixed all three pumpkins.

## Generalization

Adding parameters is what made the functions useful.
A square function with the number 100 built into it can only draw one size.
Once you pass in length, it draws any size. Same with draw_pumpkin, 
since it takes x, y, and radius, 
I could make the middle pumpkin smaller without writing new code.

## What I learned

Testing each function right after writing it helped a lot.
When I ran draw_pumpkin by itself I could see the stem was at 
the bottom instead of the top, so I knew exactly where to look. 
If I had written everything first and run it all at once,
there would have been four problems on the screen and no way to tell which 
function caused which.
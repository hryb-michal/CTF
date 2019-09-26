>Sometimes I invite a naughty script into DOM, that applies hooks on some routines and attributes.
>
>Is your browser color blind? Are you able to detect it? Just return false for emergency!
>
>https://webblind.ecsc18.hack.cert.pl

The page displays a simple editor with a snippet of code and a frame containing several colorful squares, which can be reloaded, generating a different set of those shapes.

At first sight, the presented code is supposed to count squares of a certain color and store the numbers in a dictionary, but executing the script fails each time. As we can quickly discover by peeking into the results content using `console.log(result);` just before returning its value, the number of squares doesn't match what we see on the screen.

Let's inspect this code. Some of the "puzzle" elements don't have directly declared background-color values, instead they use an aliased value inherited from <body> tag. Which works when it's to be displayed on the page, but fails to be read by our code. That could be solved by extracting the color from squares parents cssText and incrementing the number of this color occurences every time we find an alias in squares cssText.
  
Fixed code executed correctly on 100 successively generated frames, at the end displaying the flag:
  
> ecsc{0phth4lm0logist}

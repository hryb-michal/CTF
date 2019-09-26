>Sometimes I invite a naughty script into DOM, that applies hooks on some routines and attributes.
>
>Is your browser color blind? Are you able to detect it? Just return false for emergency!
>
>https://webblind.ecsc18.hack.cert.pl

The page displays a simple editor with a snippet of code and a frame containing several colorful squares, which can be reloaded, generating a different set of those shapes.

At first sight, the presented code is supposed to count squares of a certain color and store the numbers in a dictionary, but executing the script fails each time. As we can quickly discover by peeking into results content using `console.log(result);` just before returning its value, the number of squares doesn't match what we see on the screen.


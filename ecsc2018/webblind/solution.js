
if(/*cheat condition*/false)
  return false;

var puzzles = frame_window.document.getElementsByClassName("puzzle")
var result = {
  "red": 0, 
  "green": 0, 
  "blue":0
}
var alias = puzzles[0].parentElement.style[0]
var colors = ["red", "green", "blue"];
for (var color of colors){
    if(puzzles[0].parentElement.style.cssText.includes(color)) {
        var naughty = color;
    }
}

for(var puzzle of puzzles){
    if(puzzle.style.cssText.includes(alias)){
        console.log("+1");
        result[naughty]++;
    }
    else {
        var color = puzzle.style.backgroundColor;
        result[color]++;
    }
}

console.log(result);
return result;

// https://www.hackerrank.com/challenges/maximum-element/problem

function processData(input) {
  var lines = input.split("\n");
  var maxStack = [];
  for (var i = 1; i < lines.length; i++) {
    var arrLine = lines[i].split(" ").map(Number);
    var x = arrLine[1];
    switch (arrLine[0]) {
      case 1:
        //push
        var max = maxStack[maxStack.length - 1];
        if (maxStack.length > 0) {
          max < x ? maxStack.push(x) : maxStack.push(max);
        } else {
          maxStack.push(x);
        }
        break;
      case 2:
        //pop
        maxStack.pop();
        break;
      case 3:
        //print max
        console.log(maxStack[maxStack.length - 1]);
        break;
      default:
    }
  }
}

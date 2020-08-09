//https://www.hackerrank.com/challenges/jumping-on-the-cloud
//0 is safe cloud , 1 is dangerous , min moves to get to end of array , can move max 2
function jumpingOnClouds(c) {
  let jumps = 0;
  if (c.length <= 2) return 1;

  for (let i = 0; i < c.length - 2; i++) {
    if (c[i + 2] == 0 && i + 2 < c.length - 2) {
      i++;
    }
    jumps++;
  }
  return jumps;
}

console.log(jumpingOnClouds([0, 0]));

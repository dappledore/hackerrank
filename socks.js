//count the pair of socks(integers)
//https://www.hackerrank.com/challenges/sock-merchant
function sockMerchant(n, ar) {
  let socks = {};
  let pairs = 0;
  ar.forEach((sock) => {
    socks[sock] = socks[sock] || 0;
    socks[sock] += 1;
    if (socks[sock] == 2) {
      pairs += 1;
      socks[sock] = 0;
    }
  });

  //log(n^2) first attempt
  // let cnt = 0;
  // Object.keys(socks).forEach((sock) => {
  //   cnt += Math.floor(socks[sock] / 2);
  // });
  // return cnt;
  return pairs;
}

console.log(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]));

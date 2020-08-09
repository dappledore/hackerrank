// const isPrime = (n) => {
//   if (n <= 1) return false;
//   if (n === 2) return true;
//   if (n % 2 === 0) return false;
//   //goto square root of number
//   for (let i = 3, s = n ** 0.5; i < s; i += 2) {
//     if (n % i == 0) return false;
//   }
//   return true;
// };

// const nthPrime = (n) => {
//   if (n < 1) return 0;
//   let count = 0;
//   for (i = 2; ; i++) {
//     if (isPrime(i)) count++;
//     if (count == n) return i;
//   }
// };

const sieve = (n) => {
  let arr = Array(n).fill(false); //set array to all false , start with all prime
  arr[0] = arr[1] = true; //composite number
  for (let i = 2; i * i <= n; i++) {
    //any multipules of prime are not a prime
    if (!arr[i]) {
      for (let j = i * i; j <= n; j += i) {
        arr[j] = true;
      }
    }
  }
  let primes = [];
  for (i = 0; i <= n; i++) {
    if (!arr[i]) primes.push(i);
  }
  return primes[primes.length - 1];
};

// const isPrime2 = (n) =>
//   [...Array(n - 2)].map((_, i) => i + 2).filter((i) => n % i == 0).length == 0;

//console.log(isPrime(1) ? "yes" : "no");

console.log(sieve(102));

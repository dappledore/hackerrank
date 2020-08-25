// https://www.hackerrank.com/challenges/js10-class/problem

class Polygon {
  constructor(arr) {
    this.arr = arr;
  }

  perimeter() {
    return this.arr.reduce((c, i) => c + i);
  }
}

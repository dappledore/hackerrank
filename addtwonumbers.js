class ListNode {
  val = 0;
  next = null;

  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// var addTwoNumbers = function (l1, l2) { //recursive
//   let node = null;
//   const carry = arguments[2];
//   if (l1 || l2) {
//     const val1 = l1 ? l1.val : 0;
//     const val2 = l2 ? l2.val : 0;
//     const next1 = l1 ? l1.next : null;
//     const next2 = l2 ? l2.next : null;
//     const val = carry ? val1 + val2 + 1 : val1 + val2;
//     node = new ListNode(val % 10);
//     node.next = addTwoNumbers(next1, next2, val >= 10);
//   } else if (carry) {
//     node = new ListNode(1);
//     node.next = null;
//   }
//   return node;
// };

var addTwoNumbers = function (l1, l2) {
  let res = null,
    temp = null,
    prev = null;
  let carry = 0,
    sum = 0;
  while (l1 || l2) {
    sum = carry + (l1 ? l1.val : 0) + (l2 ? l2.val : 0);
    carry = sum >= 10 ? 1 : 0;
    sum = sum % 10;
    temp = new ListNode(sum);
    if (res == null) {
      res = temp;
    } else {
      prev.next = temp;
    }
    prev = temp;
    if (l1) l1 = l1.next;
    if (l2) l2 = l2.next;
  }
  if (carry) {
    temp.next = new ListNode(carry);
  }
  return res;
};

let node = new ListNode(5, new ListNode(1, new ListNode(2, null)));
let node2 = new ListNode(2, new ListNode(1, null));

console.log(addTwoNumbers(node, node2));

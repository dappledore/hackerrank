struct Stack {
  var array = [Int]()

  mutating func push(_ el:Int){
    array.append(el)
  }

  mutating func pop() -> Int? {
    return array.popLast()
  }
}

var stack = Stack()

stack.push(1)
stack.push(5)
if let a = stack.pop(), let b = stack.pop() {
  stack.push(a * b)
}
if let c = stack.pop() {
  print(c)
}
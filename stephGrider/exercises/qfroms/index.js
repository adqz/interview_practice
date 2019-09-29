// --- Directions
// Implement a Queue datastructure using two stacks.
// *Do not* create an array inside of the 'Queue' class.
// Queue should implement the methods 'add', 'remove', and 'peek'.
// For a reminder on what each method does, look back
// at the Queue exercise.
// --- Examples
//     const q = new Queue();
//     q.add(1);
//     q.add(2);
//     q.peek();  // returns 1
//     q.remove(); // returns 1
//     q.remove(); // returns 2

const Stack = require('./stack');

class Queue {
  constructor() {
    this.s1 = new Stack()
    this.s2 = new Stack()
  }
  add(newData) {
    this.s1.push(newData)
  }
  _generateQueue() {
    while(this.s1.peek()) {
      this.s2.push(this.s1.pop())
    }
  }
  _regenerateStack() {
    while(this.s2.peek()) {
      this.s1.push(this.s2.pop())
    }
  }
  remove() {
    this._generateQueue()
    let last_element = this.s2.pop()
    this._regenerateStack()
    return last_element
  }
  peek() {
    this._generateQueue()
    let last_element = this.s2.data[this.s2.data.length - 1]
    this._regenerateStack()
    return last_element
  }
  
}

module.exports = Queue;

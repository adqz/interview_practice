// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
  constructor(data, next=null){
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }
  insertFirst(data) {
    this.head = new Node(data, this.head);
  }
  size() {
    let counter = 0;
    let node = this.head;
    while(node) {
      counter++;
      node = node.next;
    }
    return counter;
  }
  getFirst() {
    return this.head;
  }
  getLast() {
    let node = this.head;
    if(!node) {
      return null;
    }
    while(node.next) {
      node = node.next;
    }
    return node
  }
  clear() {
    this.head = null;
  }
  removeFirst() {
    if (!this.head) {
      return;
    }
    this.head = this.head.next;
  }
  removeLast() {
    if(!this.head) { // empty list
      return;
    }
    if(!this.head.next) { //list with 1 element
      this.head = null;
      return;
    }
     //list with atleast 2 elements
    let previous = this.head;
    let node = previous.next;
    while (node.next) {
      previous = node
      node = previous.next
    }
    previous.next = null;
  }
  insertLast(data) {
    let lastNode = this.getLast();
    if(!lastNode) { //if chain is empty, add node to header
      this.head = new Node(data)
    } else { //if chain is not empty, add node to last node
    lastNode.next = new Node(data);
    }
  }
  getAt(n) {
    let counter = 0;
    let node = this.head;

    while(node) {
      if (counter === n) {
        return node;
      }
      counter++;
      node = node.next;
    }
    return null;
    // add a check for if n>this.size() to tell user index is invalid
  }
  removeAt(n) {
    /* EDGE CASES
      1. When linked list is empty
      2. When n === 0 (removing 1st element coz the previous of this is the head)
      3. When n > size of list
    */
   // EDGE CASES
    if (!this.head) { // 1. When linked list is empty
      return;
    }
    if (n === 0) { // 2. When n === 0 
      this.head = this.head.next;
      return;
    }
    let previous = this.getAt(n-1);
    if (!previous || !previous.next) { // 3. when n > size of list
      return;
    }
    // Normal Case
    previous.next = previous.next.next; //removing node by eliminating link to it
    
  }

  insertAt(data, n) {
    /* EDGE CASES
      1. When linked list is empty
      2. When n === 0 (removing 1st element coz the previous of this is the head)
      3. When n > size of list
    */
   if (!this.head) { // 1. When linked list is empty
    this.head = new Node(data)
    return;
   }
   if (n === 0) { // 2. When n === 0 (
     this.head = new Node(data, this.head);
     return;
   }
   
   let previous = this.getAt(n-1);
   if (!previous || !previous.next) { // 3. When n > size of list
     this.insertLast(data);
     return;
   }
   // Normal case - inserting node at middle index
   let after = previous.next;
   previous.next = new Node(data);
   previous.next.next = after;
  }
}

module.exports = { Node, LinkedList };

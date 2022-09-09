// implement a singly linked list and describe whats happening at every step

function LinkedList() {
    var length = 0
    var head = null
  
    var Node = function(element) { // use this to create nodes where we pass in the node value and the next node is null
      this.element = element
      this.next = null
    }
  
    this.size = function(){ //simply returns the length of our linked list
      return length
    }
  
    this.head = function() { // returns the head of our linked list (first item)
      return head
    }
  
    this.add = function(element) { // use this to add a node to the head of out linked list
      
      var node = new Node(element); // defining the node we want to pass in
      
      if (head === null) { // if there is no head, make node the head because its empty
        head = node
      } else { //if it isnt empty do the following
        var currentNode = head // create a current node so we can cycle through the list
  
        while(currentNode.next){ // while there is a next node, change currentNode to next
          currentNode = currentNode.next
        }
  
        currentNode.next = node //once we finish iterating through the while loop and we know the next is null, change the nextNode to node
      }
  
      length++ //then increment the length
    }
  
    this.remove = function(element){
  
      var currentNode = head;
      var previousNode;
  
      if (currentNode.element === element){ //if the head is the element we are looking for, set the head to equal the next element ??????? (so is there still a node before it pointing to it)
        head = currentNode.next
      } else {
        while(currentNode.element !== element) { //while the currentNode that were on doesnt equal the element were looking for, keep iterating
          previousNode = currentNode;
          currentNode = currentNode.next;
        }
        previousNode.next = currentNode.next //when we break the while loop (meaning current node is the one we want to delete), simply set the previous node to the next node which takes it out of the list
      }
      length --; //then decrement the length
    }
  
    this.isEmpty = function() {
      return length === 0
    }
  
    this.indexOf = function(element) {
      var currentNode = head;
      var index = -1
  
      while (currentNode){ //while currentNode doesnt equal null (meaning were not at the end of the list)
        index++; //increment (if this is first element -1 becomes 0)
        if(currentNode.element === element){
          return index; //if we find it return the index
        }
        currentNode = currentNode.next //if not keep iterating
      }
  
      return -1 //meaning its not in the list because we went through the while loop and didnt see anything
    }
  
    this.elementAt = function(index){
      var currentNode = head;
      var count = 0;
      while (count < index){ //while count (starting at 0) is lower than index, increment the count and continue to iterate through nodes
        count++;
        currentNode = currentNode.next
      }
      return currentNode.element //once count is not greater than the index provided, return the current node
    }
  
    this.addAt = function(index){
      var node = new Node(element)
  
      var currentNode = head;
      var previousNode;
      var currentIndex = 0;
  
      if (index > length){ //if index requested is larger than length return false because it doesnt exist in the list
        return false
      }
  
      if (index === 0){ //if index = 0 that means we are trying to add the element to the head node
        node.next = currentNode; //so simply make the node after ours equal the head
        head = node; //then make the head equal the node were currently on (node -> oldhead)
      } else {
        while (currentIndex < index) { //while the current index is less than index, 
          currentIndex++; //increment the index and continue iteration
          previousNode = currentNode;
          currentNode = currentNode.next
        } //once we break the loop, the currentNode = node at that index, and previousNode is the  one before it
        node.next = currentNode; //simply set the node we want to inserts next node as the currentNode, and the previous nodes next as out node (that we want to insert)
        previousNode.next = node
      }
        length++ //then increment because we added one
    }
  
    this.removeAt = function(index){
      var currentNode = head;
      var previousNode;
      var currentIndex = 0;
  
      if (index < 0 || index >= length) {
        return null //if the index is less than 0 or greater than or equal to the length, return null
      }
  
      if (index === 0){ //if the index provided is = 0, set the head to the next node after the head
        head = currentNode.next
      } else {
        while(currentIndex < index) { //while currentIndex is less than index
          currentIndex++; //increment the index and continue to iterate
          previousNode = currentNode; 
          currentNode = currentNode.next
        } //once we break the loop, the currentNode = the node at that index, and previousNode is the  one before it
        previousNode.next = currentNode.next //now simply set the previousNodes next to the currentNodes next, taking the node in the argument out of the linkedList
      }
      length--; //decrement because we just removed somthing
      return currentNode.element //return the node we just took out
    }
  
  }
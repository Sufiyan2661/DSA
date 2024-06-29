// Remove an item from an arrray with pop() and shift()

// pop() removes the elemen from the end of the array
// shif() removes the element from the beginning of the array.

// Note => neither of the method doesn`t takes parameter.

// let see with an example

let greetings = ['whats up ?','hello','see ya !']
greetings.pop()
console.log(greetings)
// o/p = [ 'whats up ?', 'hello' ]

greetings.shift()
console.log(greetings)
// o/p = [ 'hello' ]

// We can also return the value of the removed element with either methods like this 

let popped = greetings.pop()
console.log(popped)
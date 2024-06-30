// Remmove item using splice()

// Example 

let arr = ['today','was','not','so','great']
console.log(arr)
arr.splice(2,2)
console.log(arr)
// o/p = [ 'today', 'was', 'great' ]

// Its also returns a new array containing the value of the removed element.
// Example

let array = ['I','am','feeling','really','great']
let newArray = array.splice(3,2)
console.log(array,newArray)
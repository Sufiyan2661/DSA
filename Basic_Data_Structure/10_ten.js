// Check for the presence of an element with indexOf()

let fruits = ['apples','pears','oranges','peaches','pear']
console.log(fruits.indexOf('dates'))
console.log(fruits.indexOf('peaches'))
console.log(fruits.indexOf('apples'))

/*
indexOf() can be incredibly useful for quickly checking for the presence of an element on an array. We have defined a function, quickCheck, that takes an array and an element as arguments. Modify the function using indexOf() so that it returns true if the passed element exists on the array, and false if it does not
*/


const quickCheck = (arr,elem) =>{

  if(arr.indexOf(elem)=== -1){
    return false
  }else{
    return true
  }
}


console.log(quickCheck(['squash', 'onions', 'shallots'], 'squash'));
// Create a complex multi-dimensional array

let nestedArray = [
   ['deep'],
   [
    ['deeper'],['deeper']
   ],
   [
    [
        ['deepest'],['deepest']
    ],
   ]
]

console.log(nestedArray[2][1][0][0][0])
// also we can resit it if we want

nestedArray[2][1][0][0][0] = "deeper still"

console.log(nestedArray[2][1][0][0][0])
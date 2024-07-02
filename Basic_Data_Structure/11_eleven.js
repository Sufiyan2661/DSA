// Iterate through all an array`s item using for loop

const greaterThanTen = (arr) => {
    let newArr = []
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 10) {
            newArr.push(arr[i])
        }
    }
    return newArr
}

// console.log(greaterThanTen([2,12,8,14,80,1,3]))



function filteredArray(arr, elem) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i]) && arr[i].indexOf(elem) == -1) {
            newArr.push(arr[i])
        }
    }
    
    return newArr;
}

console.log(filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 3));
console.log(filteredArray([[10, 20, 30], [1, 2, 3], [4, 5, 6], [7, 8, 9]], 3));
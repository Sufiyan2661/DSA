// copy array item using slice()

let weatherCondition = ['rain','snow','sleet','hail','clear']
let todaysWeather = weatherCondition.slice(1,3)
console.log(todaysWeather)
console.log(weatherCondition)
// slice() doesn`t modify the existing array.

// We have defined a function, forecast, that takes an array as an argument. Modify the function using slice() to extract information from the argument array and return a new array that contains the string elements warm and sunny.

const forecast = (arr) =>{
    return arr.slice(2,4)
}

console.log(forecast(['cold', 'rainy', 'warm', 'sunny', 'cool', 'thunderstorms']));
// Add Key-value pairs to javascript Objects

const tekkenCharacter = {
    player: 'hworang',
    fightingStyle: 'tae kwon Doe',
    human: true

}

// if you want to add an additional property it can done by like this 

tekkenCharacter.origin = 'south Korea'

// console.log(tekkenCharacter)


/* You can also add the property with bracket notation. Bracket notation is required if your property has a space int it or if you want to use a varaible to name the property.
*/

tekkenCharacter['hair color'] = 'dyed orange'

// console.log(tekkenCharacter)

// add using variable

const eyes = 'eye color'
tekkenCharacter[eyes] = 'brown'

console.log(tekkenCharacter)
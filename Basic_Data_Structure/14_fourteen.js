// Modify an onject nested within an object

const nestedObject = {
    id: 288062695164,
    date: 'December 31, 2016',
    data: {
        totalUsers: 99,
        online: 80,
        onlineStatus: {
            active: 67,
            away: 13,
            busy: 8
        }
    }
}


// you can also acces using dot notation

console.log(nestedObject.data.totalUsers)

// it can also be changed using dot notation

nestedObject.data.onlineStatus.busy = 10

console.log(nestedObject)
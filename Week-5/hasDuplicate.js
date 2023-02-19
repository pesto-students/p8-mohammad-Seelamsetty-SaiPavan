hasDuplicate([2,3,2,1]) // true
hasDuplicate([7,4,5,3]) // false

const hasDuplicate = arr => new Set(arr).size !== arr.length
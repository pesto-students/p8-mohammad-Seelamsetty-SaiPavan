//Create a memoize function that remembers previous inputs and stores them in cache 
//so that itwon’t have to compute the same inputs more than once.
 //The function will take an unspecifiednumber of integer inputs and a reducer method.


 
 // Memoizer
 const memoizeAdd = () => {
 
    // Create cache for results
    // Empty objects
    const results = {};

    // Return function which takes
    // any number of arguments
    return (...args) => {
        // Create key for cache
        const argsKey = JSON.stringify(args);

        // Only execute func if no cached val
        // If results object does not have
        // anything to argsKey position
        if (!results[argsKey]) {
            results[argsKey] = func(...args)
        }
        return results[argsKey];
    };
};

// Wrapping memoization function
const add = memoizeAdd((num1, num2) => {
    let total = 0;
     total=num1+num2;
    return total;
});

console.log(memoizeAdd(500, 5000));
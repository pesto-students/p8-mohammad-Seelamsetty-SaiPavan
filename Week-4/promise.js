const num = 5;
// function that generates random numbers divisible by n with a default
//upper limit of 1000000
const specialRandom = (num = 1, limit = 1000000) => {
   // getting a random number
   const random = Math.random() * limit;
   // rounding it off to be divisible by num
   const res = Math.round( random / num ) * num;
   return res;
};

const myPromise = () => {
    return new Promise((resolve, reject) => {
        console.log(specialRandom(num));
        if(random % 5 ===0){
            setTimeout(() => {
       
                reject("Promise Rejected");
              }, 2000);  
        }
        else{
            setTimeout(() => {
                resolve("Promise Resolved");
              }, 1000);
            
        }     
    });
  };
  
  myPromise()
    .then((fromResolve) => {
      console.log(fromResolve);
    })
    .catch((fromReject) => {
      console.log(fromReject); // Promise Rejected
    });
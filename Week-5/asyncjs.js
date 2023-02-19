/*
promise internal states-
resolve
reject
pending
*/
/*
async function f1(){
    return 1
}
f1().then(console.log('success'));
*/
async function f(){
    let promise =new Promise((resolve,reject) => {
        setTimeout(() => resolve("done"),6000)
    });

    //promise always gets highest priority in execution
    let result = await promise;
    console.log(`success - the resuly is ${result}`);
    console.log('hello');
    console.log('Javascript');
    
}

f();


/* Asyn Await */
const url = "https://dummyurl.in/jokes/random";

const doNetworkCall = async () => {
  try {
    const response = await fetch(url);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
};

doNetworkCall();
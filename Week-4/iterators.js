let fibObj = { 
    one: 0, 
    two: 1, 
    temp: 0, 

     [Symbol.iterator](){ 
        return this; 
     }, 

    next(){ 
        this.temp = this.two; 
        this.two = this.temp + this.one; 
        this.one = this.temp; 
        return {value: this.two} 
    } 
} 

for(let I = 0 ; I < 1000; I++){ 
       consolel.log(fibObj.next().value) 
} 
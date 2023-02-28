function asyncify(generatorFunc) {
    return function asyncifiedFunc(...args) {
      const gen = generatorFunc.call(this, ...args);
  
      function processNextState(nextState) {
        const { done, value } = nextState;
  
        if (done) {
          return value;
        }
  
        if (
          typeof value === "object" &&
          typeof value.then === "function"
        ) {
          return value.then(resolvedValue => {
            return processNextState({   
              done,
              value: resolvedValue
            })
          }).catch(err => {
            // Invoke gen.throw
            return processNextState(gen.throw(err))
          });
        }
  
        return processNextState(gen.next(value));
      }
    
      try {
        const returnValue = processNextState(gen.next());
        return Promise.resolve(returnValue);
      } catch (err) {
        return Promise.reject(err);
      }
    }
  }
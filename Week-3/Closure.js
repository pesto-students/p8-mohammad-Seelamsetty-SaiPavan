//Refactor the above stack implementation, using the concept of closure,
 //such that there is noway to access items array outside of createStack() function scope:
function createStack() {
    const items = [];
    return {
      push(item) {
        items.push(item);
      },
      pop() {
        return items.pop();
      }
    };
  }
  const stack = createStack();
  stack.push(110);
  stack.push(75);
  stack.pop(); // => 75
  stack.items; // => undefined
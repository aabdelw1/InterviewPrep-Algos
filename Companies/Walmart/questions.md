# Questions

1. How to use the npm package "Request"

- The request module is used to make HTTP calls. It is the simplest way of making HTTP calls in node.js using this request module. It follows redirects by default. 
- Note: As of Feb 11th, 2020, request is fully deprecated.
- Feature of Request module:
- It is easy to get started and easy to use.
- It is widely used and popular module for making HTTP calls.


2. What is a reducer?
- The reducer is nothing else but a simple function that accepts two arguments and base on those two arguments, returns a new state value.


3. What is async, await, and callback in node?
- A callback function is a function passed into another function as an argument, which is called (or executed) inside the otherFunction.
- So the basic way to handle asynchronous operations is through callbacks. But when working with a lot of dependent asynchronous operations, you quickly end up in callback hell.

- The async function declaration defines an asynchronous function, which returns an AsyncFunction object.
- Async/await is actually built on top of promises. It cannot be used with plain callbacks or node callbacks.
- The word “async” before a function means one simple thing: a function always returns a promise. If the code has return <non-promise> in it, then JavaScript automatically wraps it into a resolved promise with that value.
- The keyword await makes JavaScript wait until that promise settles and returns its result.


Use Callbacks if you got no other choice or only handle one async operation. The code will then still be perfectly manageable and understandable. Callback functions aren’t bad per se — there just exist better alternatives in many cases.

async/ await is an awesome tool for cases where you don’t really want or need to use observables but still want to use promises. You can write “synchronous” code with async/ await and handle your promise chains even easier.

 

4. What is middleware in NodeJS and tell me an example?

Middleware functions are functions that have access to the request object (req), the response object (res), and the next middleware function in the application’s request-response cycle. The next middleware function is commonly denoted by a variable named next.

Middleware functions can perform the following tasks:

Execute any code.
Make changes to the request and the response objects.
End the request-response cycle.
Call the next middleware function in the stack.
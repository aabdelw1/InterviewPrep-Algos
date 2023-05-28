//Set object
const array = [1, 2, 3, 4, 4, 5, 2, 1];
const uniqueArray = [...new Set(array)];
console.log(uniqueArray); // [1, 2, 3, 4, 5]

//filter method

const array = [1, 2, 3, 4, 4, 5, 2, 1];
const uniqueArray = array.filter((value, index, self) => {
  return self.indexOf(value) === index;
});
console.log(uniqueArray); // [1, 2, 3, 4, 5]


//reduce method
const array = [1, 2, 3, 4, 4, 5, 2, 1];
const uniqueArray = array.reduce((a, c) => {
  if (!a.includes(c)) {
    a.push(c);
  }
  return accumulator;
}, []);
console.log(uniqueArray); // [1, 2, 3, 4, 5]

// different types
const array = [1, 'apple', 2, 'banana', 2, 'apple', { name: 'John' }, { name: 'John' }];
const uniqueArray = [...new Set(array.map(JSON.stringify))].map(JSON.parse);
console.log(uniqueArray);
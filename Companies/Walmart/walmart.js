
//"This is it"

let findCommonCharacters = (str) => {
  let words = str.split(" ")
  let minLen = words[0].length

  let res = []
  let minWord = words[0]
  for(let i = 0; i < words.length; i++){
    if(words[i].length < minLen){
      minWord = words[i]
      minLen = words[i].length
    }
  }

  console.log("minLne", minLen)
  for(let i = 0; i < minLen; i++){
    let curChar = minWord[i]
    console.log("curChar", curChar)
    for(let j = 0; j < words.length;j++){
      if(words[j].indexOf(curChar) == -1){
        return res
      }
    }

    res.push(curChar)
  }
  return res
}

var commonChars = function(words) {
  const arr = []
  for(let w of words[0]) {
     if (words.every(a => a.includes(w))){
          arr.push(w)
          words = words.map((a) => a.replace(w, ""));
     }
  }
  return arr;
};

var longestCommonPrefix = function(arr) {
  let i = 1;
  let prf = arr[0];
  while(i < arr.length){
      if(!arr[i].startsWith(prf)){
          prf = prf.slice(0, -1)
      }else{
          i++
      }
  }
  return prf
};



function removeDuplicates(arr) {
  let set = new Set()
  arr.forEach(el => set.add(el))
  return set
}

function printEndInFront(arr) {
  let prefix = arr.slice(0,5)
  let end = arr.slice(5)
  return [...end, ...prefix]
}

const testArray = [1,2,3,4,5,6,7,8]

console.log(removeDuplicates(testArray))
console.log(printEndInFront(testArray))
console.log(findCommonCharacters("This is it"))


// The string
// 'The quick brown fox jumps over the lazy dog';

// The array of replacement objects
// [ { start: 16, word: 'fox', replacement: 'elephant' }]; 

// Result
// 'The quick brown elephant jumps over the lazy dog'


const replacement = [ { start: 16, word: 'fox', replacement: 'elephant' }, { start: 16, word: 'cat', replacement: 'owl' }, { start: 40, word: 'dog', replacement: 'elephant' }]; //m
const s = 'The quick brown fox jumps over the lazy dog'; //n


const replace = (s, replacement) => {
        
   if(replacement.length == 0){
       return s
   }

   const replacementMap = {}
   for(var i = 0; i < replacement.length; i++){     
       replacementMap[replacement[i].start] = {
           word: replacement[i].word,
           replace: replacement[i].replacement 
       }
   }
   let newString = "";
   for(var j=0; j<s.length; j++){
       if(replacementMap[j]){
        if(s.substring(j, j + replacementMap[j].word.length) == replacementMap[j].word){
            newString += replacementMap[j].replace
            j = j + replacementMap[j].word.length -1 
        }
       } else{
            newString += s[j]
    }
   }
   console.log(newString)
}

replace(s, replacement)
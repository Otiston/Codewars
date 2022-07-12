function spinWords(input){
var rever = function(el,index,array){
  if(el.split('').length >= 5){
      return el.split('').reverse().join('');
  } else { return el }
}
return(input.split(' ').map(rever).join(' '))
}
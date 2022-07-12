function highAndLow(numbers){
  var arr = numbers.split(' ')
  arr = arr.splice(0).sort(function(a,b){return a-b})
  return [arr[arr.length-1],arr[0]].join(' ')
}
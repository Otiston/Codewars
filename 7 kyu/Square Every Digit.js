function squareDigits(num){
var dig = num.toString().split('')
var res = []
for (var i = 0; i < dig.length; i++){
  res.push(Math.pow(dig[i], 2))
  }
return parseInt(res.join(''))
}
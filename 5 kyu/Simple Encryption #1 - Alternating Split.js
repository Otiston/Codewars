function encrypt(text, n) {
if(text ==null){return text}else{var t = text.split``}
var resu1 = []
var resu2 = []
if(n!=null){
for(var i = 0; i < n; i++){
  t.forEach(function(lettre,i){
     if(Number.isInteger((i+1)/2)) {
       resu1.push(lettre)
     }else{resu2.push(lettre)}
  })
  t = []
  t.push(resu1,resu2)
  t = t.join(',')
  t = t.split(',')
  resu1 = []
  resu2 = []
  text = t.join``
}}
return text
}

function decrypt(text, n) {
if(text ==null){return text}else{var l = Math.trunc(text.length/2)}
var res = []
if(n!=null){
for(var i = 0; i < n; i++){
  var t = text.split``
  var resu1 = t.splice(l)
      for (var ii = 0; ii <= l;ii++){
        if (resu1[ii] != null){res.push(resu1[ii])}
        if (t[ii] != null){res.push(t[ii])}
      }
  text = res.join``
  res = []
}}
return text
}
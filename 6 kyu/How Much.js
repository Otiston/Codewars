function howmuch(m, n) {
  var mcar
  var mboat
  var money
  var range = [m, n]
  var res = []
  var resu = []
  
  range.sort(function(a,b){
  return a - b
  })
  
  console.log(range)
  
  for (var i = range[0]; i <= range[1]; i++){
    if (Math.trunc(i/9) > 0)
      for (var ii = 1; ii <= Math.trunc(i/7); ii++){
        if ( i - 7*ii == 2){
          for (var iii = 1; iii <= Math.trunc(i/9); iii++){
            if (i - 9*iii == 1){
              resu = ["M: "+i,"B: "+ii,"C: "+iii]
              res.push(resu)
            }
          }
        }
      }
    }
    return(res)
    console.log(res)
  }
  
function array_diff(a, b) {
  var res = []
  for (var i = 0;i<a.length;i++){
    if (b.indexOf(a[i]) < 0){
      res.push(a[i])
    }  
  }
  return res
}
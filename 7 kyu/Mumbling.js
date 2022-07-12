function accum(s) {
  var res=[]
  var get = s.toLowerCase().split('')
  for(var i=0;i<get.length;i++){
    var temp = []
    for(var ii=0; ii<i+1;ii++){
      if(ii == 0){
        temp.push(get[i].toUpperCase())
        }else{temp.push(get[i])}
    }
    res.push(temp.join(''))
  }
  return res.join('-')
}
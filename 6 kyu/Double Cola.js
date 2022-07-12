function whoIsNext(names, r){
var o = []

names.forEach(name=>{
  o.push({
  name:name,
  val:1
  })
})

while (r!=0){
  if(o[0].val<r){
    r -= o[0].val
    o.push(o[0])
    o.shift()
    o[o.length-1].val = 2*o[o.length-1].val
  }else{return o[0].name}
}
}

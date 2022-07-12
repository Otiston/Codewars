function towerBuilder(nFloors) {
var tow = ["*"]
var tower =[]
  for(var i = 1; i < nFloors; i++){
    tow.push("**")
  }
var towi = tow.join``.split``

  for(var i = 0; i < nFloors; i++){
  
    if (towi.length >= 1){
      tower.unshift(towi.join``)
      towi.splice(i,1," ")
      towi.splice(towi.length-1-i,1," ")
    }
  }
return tower
}
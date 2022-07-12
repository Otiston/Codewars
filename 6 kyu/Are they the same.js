function comp(ar1, ar2){
  if(ar1 == null || ar2 == null || ar1.length != ar2.length){return false}
  for (var i=0;i<ar1.length;i++){
    if(ar2.indexOf(Math.pow(ar1[i],2))<0){return false}
      else{
     ar2.splice(ar2.indexOf(Math.pow(ar1[i],2)),1)
      }
    }
  return true;
}
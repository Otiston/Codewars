function queueTime(customers, n) {
if (n>customers.length){n=customers.length}
var count = 0
  while(isNaN(customers[0])==false){
    for(var i=0; i<n; i++){
      customers[i] = customers[i] - 1
    }
    for(var i=n-1; i>=0; i--){
      if(customers[i]<=0){
          customers.splice(i,1)
      }
    }
    count++
  }
return(count)
}
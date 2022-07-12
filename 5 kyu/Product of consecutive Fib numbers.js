function productFib(prod){
var fib=[0,1]
  for(var i=1; prod>=(fib[i]*fib[i-1]);i++){
    if(prod == fib[i]*fib[i-1]){
      return [fib[i-1],fib[i],true]
    }
  fib.push(fib[i]+fib[i-1])
  }
  return [fib[fib.length-2],fib[fib.length-1],false]
}
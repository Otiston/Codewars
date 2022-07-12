function seven(m) {

var num = m.toString();
var chi = num.split('');
var count = 0;
var res = null;
var save = null;
var last = null;
var num2 = null;

if (m>0){
  do{
    last = chi[chi.length-1]
    chi.pop()
    num = chi.join('')
    m = num - 2*last
    num = m.toString();
    chi = num.split('');
    count++;
  }while(chi.length > 2)
}
  res = [parseInt(m,10), count];
  return(res);
  
}
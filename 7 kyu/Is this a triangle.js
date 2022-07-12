function isTriangle(a,b,c){
var num = [a,b,c].splice(0).sort(function(a,b){return a-b});
return num[2] >= num[1]+num[0] ? false : true;
}
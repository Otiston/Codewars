function duplicateEncode(word){
   var dat = word.toLowerCase().split('')
   var res = []
   for(var i=0;i<dat.length;i++){
     if(dat.indexOf(dat[i])<i){
     res.push(")")
     }
     else {      
       if(dat.indexOf(dat[i],i+1)>0){
       res.push(")")
       }else{res.push("(")}
       }
   }
   return res.join('')           
}
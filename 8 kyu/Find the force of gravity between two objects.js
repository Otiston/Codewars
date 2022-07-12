solution = (arr_val, arr_unit) => {
//  console.log(arr_val[0],arr_val[1],arr_val[2]);
//  console.log(arr_unit[0],arr_unit[1],arr_unit[2]);

var mo1 = arr_val[0];
var mo2 = arr_val[1];
var d = arr_val[2];
var G = 0;
  
  if(arr_unit[0] == "g"){
  mo1 = mo1 / 1e3
  }
  else if(arr_unit[0] == "mg"){
  mo1 = mo1 / 1e6
  }
  else if(arr_unit[0] == "μg"){
  mo1 = mo1 / 1e9
  }
  else if(arr_unit[0] == "lb"){
  mo1 = mo1 * 0.453592
  }
  
    if(arr_unit[1] == "g"){
    mo2 = mo2 / 1e3
  }
  else if(arr_unit[1] == "mg"){
  mo2 = mo2 / 1e6
  }
  else if(arr_unit[1] == "μg"){
  mo2 = mo2 / 1e9
  }
  else if(arr_unit[1] == "lb"){
  mo2 = mo2 * 0.453592
  }
  
      if(arr_unit[2] == "cm"){
  d = d / 1e2
  }
  else if(arr_unit[2] == "mm"){
  d = d / 1e3
  }
  else if(arr_unit[2] == "μm"){
  d = d / 1e6
  }
  else if(arr_unit[2] == "ft"){
  d = d * 0.3048
  }
  
  G = (6.67e-11*mo1*mo2)/(d*d);
  console.log(G);
  return(G)
};
predicate units(var int:amount, 
                var int:unit_size, 
                var bool: round_up, 
                var int:units ) = 
let {
  constraint units = amount div unit_size + if round_up then amount mod unit_size > 0 else 0 endif;
} in true;



predicate act_conveyance_duty(var bool: non_commercial, 
                              var bool: eligible_owner_occupier, 
                              var int:price, 
                              var float:duty) = 
let {
  constraint eligible_owner_occupier -> non_commercial;
  constraint price >= 0;
  constraint duty >= 0;
  var int: num_units;
  int: unit = 100;
  constraint duty = 
  if non_commercial then
    if eligible_owner_occupier then
      if price > 0       /\ price <=260000  
          /\ units(price, unit, true, num_units) then num_units * 60 else 
      if price > 260000  /\ price <=300000  
          /\ units(price-260000, unit, true, num_units)  then 1560.00  + num_units * 2.20 else 
      if price > 300000  /\ price <=500000  
          /\ units(price-300000, unit, true, num_units)  then 2440.00  + num_units * 3.40 else 
      if price > 500000  /\ price <=750000  
          /\ units(price-500000, unit, true, num_units)  then 9240.00  + num_units * 4.32 else 
      if price > 750000  /\ price <=1000000 
          /\ units(price-750000, unit, true, num_units)  then 20040.00 + num_units * 5.90 else 
      if price > 1000000 /\ price <=1455000 
          /\ units(price-1000000, unit, true, num_units) then 34790.00 + num_units * 6.40 else 
      if price > 1445000                    
          /\ units(price, unit, true, num_units) then num_units * 4.54 
      else -1 endif endif endif endif endif endif endif
    else % not eligible_owner_occupier
      if price > 0       /\ price <=200000  
          /\ units(price, unit, true, num_units)         then num_units * 120 else 
      if price > 200000  /\ price <=300000  
          /\ units(price-200000, unit, true, num_units)  then 2400.00  + num_units * 2.20 else 
      if price > 300000  /\ price <=500000  
          /\ units(price-300000, unit, true, num_units)  then 4600.00  + num_units * 3.40 else 
      if price > 500000  /\ price <=750000  
          /\ units(price-500000, unit, true, num_units)  then 11400.00 + num_units * 4.32 else 
      if price > 750000  /\ price <=1000000 
          /\ units(price-750000, unit, true, num_units)  then 22200.00 + num_units * 5.90 else 
      if price > 1000000 /\ price <=1455000 
          /\ units(price-1000000, unit, true, num_units) then 36950.00 + num_units * 6.40 else 
      if price > 1445000                    
          /\ units(price, unit, true, num_units)         then num_units * 4.54 
      else -1 endif endif endif endif endif endif endif
    endif
  else % commercial
    if price > 0         /\ price <= 1700000 then 0 else
    if price > 1700000                      
          /\ units(price, unit, true, num_units)         then num_units * 5.00 else -1 endif endif
  endif
} 
in true;
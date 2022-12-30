predicate range2(var float: from_start,
                var float: to_stop,
                var int: n,
                var int: nth,
                var float: nth_value) =
let {
  constraint n > 0;
  constraint 0 <= nth /\ nth <= n-1;
  constraint nth_value = from_start + (to_stop-from_start) / (n-1) * nth ;

} in true;
constraint nth_value < 13.0;
n = 5 ;
from_start = 10;
to_stop = 20;


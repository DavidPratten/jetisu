predicate range(var float: from_start,
                var float: to_stop,
                var int: n,
                var int: nth,
                var float: nth_value) =
let {
  constraint n > 0;
  constraint 0 <= nth /\ nth <= n-1;
  constraint nth_value = from_start + (to_stop-from_start) / (n-1) * nth ;
} in true;
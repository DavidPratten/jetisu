predicate australian_gst(var float: price,
                         var float: ex_gst_amount,
                         var float: gst_amount) =
let {
    constraint price/11 = gst_amount;
    constraint ex_gst_amount = price-gst_amount;
    }
in true;
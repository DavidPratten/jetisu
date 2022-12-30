predicate new_birthday_money(
    var int: age,
    var bool: good_behaviour,
    var float: birthday_money) =
let {
    constraint birthday_money = if good_behaviour then age*20.00 else 0.00 endif
} in true;
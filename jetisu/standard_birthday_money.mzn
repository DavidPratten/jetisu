predicate standard_birthday_money(
        var int: age,
        var float: birthday_money) =
let {
    constraint birthday_money = age*10.00; % constraints express a relationship
} in true;
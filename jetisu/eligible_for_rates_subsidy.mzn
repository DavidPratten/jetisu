predicate eligible_for_rates_subsidy(var bool: is_ratepayer,
                                     var bool: is_residential_property,
                                     var bool: usual_place_of_residence,
                                     var bool: is_retirement_subsidy,
                                     var bool: is_eligible) =
let {
    constraint is_eligible = (is_ratepayer /\ is_residential_property /\ usual_place_of_residence);
    constraint is_eligible -> not is_retirement_subsidy;
    }
in true;
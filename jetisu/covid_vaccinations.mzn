predicate covid_vaccinations(var int: age,
                var int: recommended_doses,
                var int: booster_doses,
                var int: vaccine_doses,
                var bool: immunocompromised_disability,
                var int: months_since_last_dose_at_least,
                var bool: covid_vaccination_eligibility,
                var bool: covid_vaccination_up_to_date
                ) =
let {
  par int: highest_number_of_months_since_last_dose_that_we_care_about = 6;
  par int: highest_number_of_vaccine_doses_that_we_care_about = 5;

  constraint age >= 0 /\ age <=115;
  constraint vaccine_doses >= 0 /\ vaccine_doses <= highest_number_of_vaccine_doses_that_we_care_about;
  constraint vaccine_doses = 0 -> months_since_last_dose_at_least = highest_number_of_months_since_last_dose_that_we_care_about;
  constraint covid_vaccination_up_to_date -> not covid_vaccination_eligibility;
  constraint months_since_last_dose_at_least >= 0 /\ months_since_last_dose_at_least <=highest_number_of_months_since_last_dose_that_we_care_about;
  constraint recommended_doses = if     age <   5              then 0
                                 elseif age >=  5 /\ age <= 11 then 2 + if immunocompromised_disability then 1 else 0 endif
                                 elseif age >= 12 /\ age <= 15 then 2 + if immunocompromised_disability then 1 else 0 endif
                                 elseif age >= 16 /\ age <= 29 then 2 + if immunocompromised_disability then 1 else 0 endif
                                 elseif age >= 30 /\ age <= 49 then 2 + if immunocompromised_disability then 1 else 0 endif
                                 else 2 + if immunocompromised_disability then 1 else 0 endif
                                 endif;
constraint booster_doses = if     age <   5              then 0
                                 elseif age >=  5 /\ age <= 11 then 0
                                 elseif age >= 12 /\ age <= 15 then 0
                                 elseif age >= 16 /\ age <= 29 then 1
                                 elseif age >= 30 /\ age <= 49 then 1
                                 else 2
                                 endif;

constraint covid_vaccination_eligibility = (months_since_last_dose_at_least >= 3 /\ (recommended_doses+booster_doses > vaccine_doses));
constraint covid_vaccination_up_to_date = (recommended_doses + booster_doses <= vaccine_doses) /\ ((recommended_doses + booster_doses > vaccine_doses) -> (months_since_last_dose_at_least <= 6));
} in true;
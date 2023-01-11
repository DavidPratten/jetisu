enum work_location_enum = { new_south_wales, victoria, western_australia};
enum work_sector_enum = {education, aged_care, healthcare, custodial, emergency_services, disability_services,  other };

predicate covid_vaccinations_and_work(
    var work_location_enum: work_location,
    var work_sector_enum: work_sector,
    var bool: specialist_school,
    var bool: aged_care_facility,
    var bool: disability_worker_in_school,
    var bool: private_home_only,
    var bool: nsw_health_worker,
    var bool: covid_vaccination_work_mandatory,
    var int: covid_vaccination_work_recommended_doses
    ) =
let {
constraint (covid_vaccination_work_recommended_doses > 0) <-> covid_vaccination_work_mandatory;
constraint disability_worker_in_school -> (work_sector = education);
constraint specialist_school -> (work_sector = education);
constraint aged_care_facility -> (work_sector = aged_care);
constraint nsw_health_worker -> (work_sector = healthcare /\ work_location = new_south_wales);
constraint private_home_only -> (work_sector != custodial);
constraint covid_vaccination_work_recommended_doses =
  if work_location = new_south_wales then
    if work_sector = education then
      if disability_worker_in_school then
        3
      else
        0
      endif
    elseif work_sector = aged_care then
      if aged_care_facility then
        3
      else
        2
      endif
    elseif work_sector = disability_services then
      3
    elseif work_sector = healthcare then
      if nsw_health_worker then
        3
      else
        0
      endif
    else
      0
    endif
  elseif  work_location = victoria then
    if work_sector = education then
      if specialist_school then
        3
      else
        0
      endif
    elseif work_sector = aged_care then
      if aged_care_facility then
        3
      else
        0
      endif
    elseif work_sector = custodial then
      3
    elseif work_sector = emergency_services then
      3
    elseif work_sector = disability_services then
      3
    elseif work_sector = healthcare then
      3
    elseif work_sector = other then
      0
    else
      0
    endif
  elseif  work_location = western_australia then
    if work_sector = aged_care then
      if private_home_only then
        0
      else
        3
      endif
    elseif work_sector = disability_services then
      if private_home_only then
        0
      else
        3
      endif
    elseif work_sector = healthcare then
      if private_home_only then
        0
      else
        3
      endif
    elseif work_sector = other then
      0
    else
      0
    endif
  else
    0
  endif;
} in true;
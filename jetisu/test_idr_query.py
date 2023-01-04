from jetisu.idr_query import idr_query, idr_test_res_sort

def test_idr_779c4c4437():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'new_south_wales' and work_sector = 'education' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school and not NSW_health_worker;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_8cf6c5e4d6():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'new_south_wales' and work_sector = 'education' and not specialist_school and not aged_care_facility and not private_home_only and disability_worker_in_school and not NSW_health_worker;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_25ecd837f4():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'new_south_wales' and work_sector = 'aged_care' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school and not NSW_health_worker;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 2,)])) #OpenFisca has 3


def test_idr_27f5fc7737():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'new_south_wales' and work_sector = 'aged_care' and not specialist_school and aged_care_facility and not private_home_only and not disability_worker_in_school and not NSW_health_worker;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)])) #OpenFisca has 2


def test_idr_d215ef1efe():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'new_south_wales' and work_sector = 'disability_services' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school and not NSW_health_worker;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_a804e12acd():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'new_south_wales' and work_sector = 'healthcare' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school and not NSW_health_worker;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_1e6faaafd3():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'new_south_wales' and work_sector = 'healthcare' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school and NSW_health_worker;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)])) #Open Fisca has 2


def test_idr_759fdd7e05():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'education' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_0e5aeda14a():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'education' and specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_ccfc72abad():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'aged_care' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_ff6c3a243b():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'aged_care' and not specialist_school and aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_39175ae158():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'custodial' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_ecb3d3ca89():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'emergency_services' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_801edd720f():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'disability_services' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_97a1275a44():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'healthcare' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_8270d50dab():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'victoria' and work_sector = 'other' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_8ca185cf29():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'western_australia' and work_sector = 'aged_care' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_6156129e26():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'western_australia' and work_sector = 'aged_care' and not specialist_school and not aged_care_facility and private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_ba53fe09ca():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'western_australia' and work_sector = 'disability_services' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_78919e5e14():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'western_australia' and work_sector = 'disability_services' and not specialist_school and not aged_care_facility and private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_91db09afd5():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'western_australia' and work_sector = 'healthcare' and not specialist_school and not aged_care_facility and not private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(True, 3,)]))


def test_idr_6d6236eb3a():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'western_australia' and work_sector = 'healthcare' and not specialist_school and not aged_care_facility and private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))


def test_idr_ba0365d9ba():
    res = idr_query(
        """select covid_vaccination_work_mandatory, covid_vaccination_work_recommended_doses from covid_vaccinations_and_work where work_location = 'western_australia' and work_sector = 'other' and not specialist_school and not aged_care_facility and private_home_only and not disability_worker_in_school;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('covid_vaccination_work_mandatory', 'covid_vaccination_work_recommended_doses',), [(False, 0,)]))
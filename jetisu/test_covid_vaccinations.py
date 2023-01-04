from jetisu.idr_query import idr_query, idr_test_res_sort

def test_idr_184be70233():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 0 and not immunocompromised_disability;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_d3ef4c1c7e():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_9dc8a437e9():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_00041c57fb():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 2 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_be058ce264():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 3 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)])) # OpenFisca has True


def test_idr_b88995cf46():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 4 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_1ff4664d0d():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_fb815f734c():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_42b7d256f5():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 4 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)])) # OpenFisca has True


def test_idr_a3f59998a7():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 40 and vaccine_doses = 5 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_310c4e8b10():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 10 and vaccine_doses = 0 and not immunocompromised_disability;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_c0346cfc37():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 10 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_c13b9fd4b2():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 10 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_ac56cfd86f():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 10 and vaccine_doses = 2 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_8ccd8478ce():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 10 and vaccine_doses = 2 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_3c313ff8ab():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 10 and vaccine_doses = 2 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_e13d7afde0():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 10 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_9d15e0ecb5():
    res = idr_query("""select distinct covid_vaccination_eligibility from covid_vaccinations where age = 4;""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_580c31e5a9():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 60 and vaccine_doses = 0 and not immunocompromised_disability;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_dfcd177769():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 60 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_a808ceb066():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 60 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_9576042cf1():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 60 and vaccine_doses = 4 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_7396c82cf2():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 60 and vaccine_doses = 4 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_bc59053bbf():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 60 and vaccine_doses = 4 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_995ab0c225():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 60 and vaccine_doses = 5 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_905bb01165():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 15 and vaccine_doses = 0 and not immunocompromised_disability;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_de2970d2f4():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 15 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_f117cfe3e6():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 15 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_9a5d7f86da():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 15 and vaccine_doses = 2 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_327122763f():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 15 and vaccine_doses = 2 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_8ab9b8bde7():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 15 and vaccine_doses = 2 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_3b8469f4c8():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 15 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_097dd05d06():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 25 and vaccine_doses = 0 and not immunocompromised_disability;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_72dd5aef15():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 25 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_83a91c8b20():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 25 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_6195660306():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 25 and vaccine_doses = 3 and not immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_2cd4230275():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 25 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(True,)]))


def test_idr_01560cea0f():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 25 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))


def test_idr_c6120df634():
    res = idr_query(
        """select distinct covid_vaccination_eligibility from covid_vaccinations where age = 25 and vaccine_doses = 5 and immunocompromised_disability and months_since_last_dose_at_least = 4;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_eligibility',), [(False,)]))

# up_to_date tests

def test_idr_28c771bb2c():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 40 and vaccine_doses = 0 and not immunocompromised_disability;""", #OpenFisca had date of last dose
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_3bc12633ad():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 40 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_f301e6edd5():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 40 and vaccine_doses = 2 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_d8837d6d7e():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 40 and vaccine_doses = 3 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_65a3ae09b2():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 40 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_1b18304bba():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 40 and vaccine_doses = 4 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)])) #OpenFisca had False


def test_idr_487ab00794():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 40 and vaccine_doses = 5 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_f3c0fc5574():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 10 and vaccine_doses = 0 and not immunocompromised_disability ;""", # OpenFisca had date of last dose
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_26c4234dd0():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 10 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_96055c7ba3():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 10 and vaccine_doses = 2 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_81db33b2ff():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 10 and vaccine_doses = 2 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_2acf455afb():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 10 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_de36ec94c8():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 60 and vaccine_doses = 0 and not immunocompromised_disability ;""",  # OpenFisca had date of last dose
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_bc4c9d6b73():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 60 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_1cb403db13():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 60 and vaccine_doses = 4 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_626b7f5d9f():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 60 and vaccine_doses = 4 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_6ee4b9f2b8():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 60 and vaccine_doses = 5 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_bf6b6d3f6b():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 15 and vaccine_doses = 0 and not immunocompromised_disability ;""",   # OpenFisca had date of last dose
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_7f7a36627f():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 15 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_af36847a88():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 15 and vaccine_doses = 2 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_7f5b158d4f():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 15 and vaccine_doses = 2 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_74c170f97f():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 15 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_836b0da32a():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 25 and vaccine_doses = 0 and not immunocompromised_disability;""",   # OpenFisca had date of last dose
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_a947a1717c():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 25 and vaccine_doses = 1 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_bdcf9d10f7():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 25 and vaccine_doses = 3 and not immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


def test_idr_5cf55e8935():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 25 and vaccine_doses = 3 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(False,)]))


def test_idr_c710bc32cf():
    res = idr_query(
        """select covid_vaccination_up_to_date from covid_vaccinations where age = 25 and vaccine_doses = 5 and immunocompromised_disability and months_since_last_dose_at_least = 2;""",
        'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('covid_vaccination_up_to_date',), [(True,)]))


from jetisu.idr_query import idr_query, idr_test_res_sort


def test_idr_4c8196e3fb():
    res = idr_query("""select * from new_birthday_money where age = 10 ;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(
        (('age', 'good_behaviour', 'birthday_money'), [(10.0, False, 0), (10.0, True, 200)]))


def test_idr_4cbd6b19e0():
    res = idr_query("""select good_behaviour from new_birthday_money
    where age = 10
        and birthday_money = 200;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('good_behaviour',), [(True,)]))


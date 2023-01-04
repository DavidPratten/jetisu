from jetisu.idr_query import idr_query, idr_test_res_sort

def test_idr_f6a1458c80():
    res = idr_query("""select * from standard_birthday_money where age = 10;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('age', 'birthday_money'), [(10.0, 100.0)]))


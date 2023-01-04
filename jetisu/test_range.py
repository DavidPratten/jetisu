from jetisu.idr_query import idr_query, idr_test_res_sort


def test_idr_83827ed0a8():
    res = idr_query("""select * from range where N=5 and From_Start=10 and To_Stop = 20;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('from_start', 'to_stop', 'n', 'nth', 'nth_value'),
                                                        [(10.0, 20.0, 5.0, 0, 10), (10.0, 20.0, 5.0, 1, 12.5),
                                           (10.0, 20.0, 5.0, 2, 15), (10.0, 20.0, 5.0, 3, 17.5),
                                           (10.0, 20.0, 5.0, 4, 20)]))


def test_idr_4346617aaa():
    res = idr_query("""select * from range where N=5 and To_Stop = 20 and nth_Value=15.0;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('from_start', 'to_stop', 'n', 'nth', 'nth_value'),
                                                        [(15, 20.0, 5.0, 0, 15.0), (13.3333333333, 20.0, 5.0, 1, 15.0),
                                           (10, 20.0, 5.0, 2, 15.0), (0, 20.0, 5.0, 3, 15.0)]))


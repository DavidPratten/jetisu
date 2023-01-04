from jetisu.idr_query import idr_query, idr_test_res_sort

def test_idr_60cade641e():
    res = idr_query("""select * from australian_gst where price = 110;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('price', 'ex_gst_amount', 'gst_amount'), [(110.0, 100.0, 10.0)]))


def test_idr_c46f0fe5f7():
    res = idr_query("""select * from Australian_GST where price=100 and ex_gst_amount=1 and gst_amount=1;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('price', 'ex_gst_amount', 'gst_amount'), []))


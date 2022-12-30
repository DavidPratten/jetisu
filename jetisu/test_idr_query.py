from jetisu.idr_query import idr_query


def sorted_res(res):
    return (res[0], sorted(res[1], key=lambda element: "".join([str(x) for x in element])))


def test_idr_d750d38a4a():
    res = idr_query("""select price, duty from ACT_Conveyance_Duty where price = 1200000 and eligible_owner_occupier;
""", 'data')
    assert sorted_res(res) == sorted_res((('price', 'duty'), [(1200000.0, 47590)]))


def test_idr_65378a8e35():
    res = idr_query("""select eligible_owner_occupier, duty
    from ACT_Conveyance_Duty
    where price = 1200000 and non_commercial;
""", 'data')
    assert sorted_res(res) == sorted_res((('eligible_owner_occupier', 'duty'), [(True, 47590), (False, 49750)]))


def test_idr_347d205d95():
    res = idr_query("""
select * from ACT_Conveyance_Duty where price = 1200000;

""", 'data')
    assert sorted_res(res) == sorted_res((('non_commercial', 'eligible_owner_occupier', 'price', 'duty'),
                                          [(False, False, 1200000.0, 0), (True, True, 1200000.0, 47590),
                                           (True, False, 1200000.0, 49750)]))


def test_idr_689c1ce3d5():
    res = idr_query("""
select * from ACT_Conveyance_Duty where price = 2000000;

""", 'data')
    assert sorted_res(res) == sorted_res((('non_commercial', 'eligible_owner_occupier', 'price', 'duty'),
                                          [(True, True, 2000000.0, 90800), (True, False, 2000000.0, 90800),
                                           (False, False, 2000000.0, 100000)]))


def test_idr_4ab4e9269f():
    res = idr_query("""
select price from ACT_Conveyance_Duty where duty = 50150 and eligible_owner_occupier;

""", 'data')
    assert sorted_res(res) == sorted_res((('price',),
                                          [(1240000,), (1239901,), (1239902,), (1239903,), (1239904,), (1239905,),
                                           (1239906,), (1239907,), (1239908,), (1239909,), (1239910,), (1239911,),
                                           (1239912,), (1239913,), (1239914,), (1239915,), (1239916,), (1239917,),
                                           (1239918,), (1239919,), (1239920,), (1239921,), (1239922,), (1239923,),
                                           (1239924,), (1239925,), (1239926,), (1239927,), (1239928,), (1239929,),
                                           (1239930,), (1239931,), (1239932,), (1239933,), (1239934,), (1239935,),
                                           (1239936,), (1239937,), (1239938,), (1239939,), (1239940,), (1239941,),
                                           (1239942,), (1239943,), (1239944,), (1239945,), (1239946,), (1239947,),
                                           (1239948,), (1239949,), (1239950,), (1239951,), (1239952,), (1239953,),
                                           (1239954,), (1239955,), (1239956,), (1239957,), (1239958,), (1239959,),
                                           (1239960,), (1239961,), (1239962,), (1239963,), (1239964,), (1239965,),
                                           (1239966,), (1239967,), (1239968,), (1239969,), (1239970,), (1239971,),
                                           (1239972,), (1239973,), (1239974,), (1239975,), (1239976,), (1239977,),
                                           (1239978,), (1239979,), (1239980,), (1239981,), (1239982,), (1239983,),
                                           (1239984,), (1239985,), (1239986,), (1239987,), (1239988,), (1239989,),
                                           (1239990,), (1239991,), (1239992,), (1239993,), (1239994,), (1239995,),
                                           (1239996,), (1239997,), (1239998,), (1239999,)]))


def test_idr_fe0f141905():
    res = idr_query("""
select non_commercial,
    eligible_owner_occupier,
    min(price) min_price,
    max(price) max_price
from ACT_Conveyance_Duty
where duty = 140740
group by non_commercial,
    eligible_owner_occupier;

""", 'data')
    assert sorted_res(res) == sorted_res((('non_commercial', 'eligible_owner_occupier', 'min_price', 'max_price'),
                                          [(False, False, 2814701, 2814800), (True, False, 3099901, 3100000),
                                           (True, True, 3099901, 3100000)]))


def test_idr_83827ed0a8():
    res = idr_query("""select * from range where N=5 and From_Start=10 and To_Stop = 20;
""", 'data')
    assert sorted_res(res) == sorted_res((('from_start', 'to_stop', 'n', 'nth', 'nth_value'),
                                          [(10.0, 20.0, 5.0, 0, 10), (10.0, 20.0, 5.0, 1, 12.5),
                                           (10.0, 20.0, 5.0, 2, 15), (10.0, 20.0, 5.0, 3, 17.5),
                                           (10.0, 20.0, 5.0, 4, 20)]))


def test_idr_4346617aaa():
    res = idr_query("""select * from range where N=5 and To_Stop = 20 and nth_Value=15.0;
""", 'data')
    assert sorted_res(res) == sorted_res((('from_start', 'to_stop', 'n', 'nth', 'nth_value'),
                                          [(15, 20.0, 5.0, 0, 15.0), (13.3333333333, 20.0, 5.0, 1, 15.0),
                                           (10, 20.0, 5.0, 2, 15.0), (0, 20.0, 5.0, 3, 15.0)]))


def test_idr_60cade641e():
    res = idr_query("""select * from australian_gst where price = 110;
""", 'data')
    assert sorted_res(res) == sorted_res((('price', 'ex_gst_amount', 'gst_amount'), [(110.0, 100.0, 10.0)]))


def test_idr_c46f0fe5f7():
    res = idr_query("""select * from Australian_GST where price=100 and ex_gst_amount=1 and gst_amount=1;
""", 'data')
    assert sorted_res(res) == sorted_res((('price', 'ex_gst_amount', 'gst_amount'), []))


def test_idr_f6a1458c80():
    res = idr_query("""select * from standard_birthday_money where age = 10;
""", 'data')
    assert sorted_res(res) == sorted_res((('age', 'birthday_money'), [(10.0, 100.0)]))


def test_idr_4c8196e3fb():
    res = idr_query("""select * from new_birthday_money where age = 10 ;
""", 'data')
    assert sorted_res(res) == sorted_res(
        (('age', 'good_behaviour', 'birthday_money'), [(10.0, False, 0), (10.0, True, 200)]))


def test_idr_4cbd6b19e0():
    res = idr_query("""select good_behaviour from new_birthday_money
    where age = 10
        and birthday_money = 200;
""", 'data')
    assert sorted_res(res) == sorted_res((('good_behaviour',), [(True,)]))

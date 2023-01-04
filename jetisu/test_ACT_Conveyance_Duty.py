from jetisu.idr_query import idr_query, idr_test_res_sort


def test_idr_d750d38a4a():
    res = idr_query("""select price, duty from ACT_Conveyance_Duty where price = 1200000 and eligible_owner_occupier;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('price', 'duty'), [(1200000.0, 47590)]))


def test_idr_0a5180a61c():
    res = idr_query("""select price, duty from ACT_Conveyance_Duty where price = 1200000 and not non_commercial;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('price', 'duty'), [(1200000.0, 0.0)]))


def test_idr_65378a8e35():
    res = idr_query("""select eligible_owner_occupier, duty
    from ACT_Conveyance_Duty
    where price = 1200000 and non_commercial;
""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('eligible_owner_occupier', 'duty'), [(True, 47590), (False, 49750)]))


def test_idr_347d205d95():
    res = idr_query("""
select * from ACT_Conveyance_Duty where price = 1200000;

""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('non_commercial', 'eligible_owner_occupier', 'price', 'duty'),
                                                        [(False, False, 1200000.0, 0), (True, True, 1200000.0, 47590),
                                           (True, False, 1200000.0, 49750)]))


def test_idr_689c1ce3d5():
    res = idr_query("""
select * from ACT_Conveyance_Duty where price = 2000000;

""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('non_commercial', 'eligible_owner_occupier', 'price', 'duty'),
                                                        [(True, True, 2000000.0, 90800), (True, False, 2000000.0, 90800),
                                           (False, False, 2000000.0, 100000)]))


def test_idr_4ab4e9269f():
    res = idr_query("""
select price from ACT_Conveyance_Duty where duty = 50150 and eligible_owner_occupier;

""", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort((('price',),
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
    assert idr_test_res_sort(res) == idr_test_res_sort((('non_commercial', 'eligible_owner_occupier', 'min_price', 'max_price'),
                                                        [(False, False, 2814701, 2814800), (True, False, 3099901, 3100000),
                                           (True, True, 3099901, 3100000)]))



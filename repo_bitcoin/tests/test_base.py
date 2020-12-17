from repo_bitcoin.base import add_int


def test_add_int():
    res = add_int(1, 2)
    assert res == 3
    
df = pd.DataFrame(list(zip(I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,X)), columns = ['I1', 'I2', 'I3', 
                                                             'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'X'])

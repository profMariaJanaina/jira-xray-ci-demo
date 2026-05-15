from calculator import soma, subtrai
@pytest.mark.xray(test_key="QTS-6")
def test_QTS6_Soma():
    assert soma(2,3) == 5
    
def test_QT9_subtrai():
    assert subtrai(5,3) == 2

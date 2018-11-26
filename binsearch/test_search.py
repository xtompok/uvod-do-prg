from search import bin_search

def test_bin_search():
    assert bin_search([],0,len([]),4) == False

def test_beyond_limits():
    l = [1,4,6,7]
    assert bin_search(l,0,len(l),0) == False
    assert bin_search(l,0,len(l),20) == False

def test_middle():
    assert bin_search([1,3,5],0,len([1,3,5]),3) == True

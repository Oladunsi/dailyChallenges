def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []
        

class TestDataUniqueValues(object):
    data = [i for i in range(5)]
    data = data[::-1]
   
    @staticmethod
    def get_array():
        Uniquedata = list(set(TestDataUniqueValues().data))
        # complete this function
        if  len(Uniquedata) >= 2:
            return Uniquedata

    @staticmethod
    def get_expected_result():
        Uniquedata  = list(set(TestDataUniqueValues().data))
        # complete this function
        if len(Uniquedata) >= 2:
            return minimum_index(Uniquedata)

class TestDataExactlyTwoDifferentMinimums(object):
    data = [i for i in range(5)]
    data = data[::-1]
    data.insert(2,0)


    @staticmethod
    def get_array():
        # complete this function
        IndexTwo = TestDataExactlyTwoDifferentMinimums().data
        
        if minimum_index(IndexTwo) == 2:
            return IndexTwo
        

    @staticmethod
    def get_expected_result():
        IndexTwo = TestDataExactlyTwoDifferentMinimums().data        
        # complete this function
        return minimum_index(IndexTwo) 


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")


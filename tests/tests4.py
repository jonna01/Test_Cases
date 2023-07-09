import tests3

def test_string_1():
    ## Testing String Validation with ab string
    assert tests3.string_validation_on_success("ab") == True
    
def test_string_2():
    ## Testing String Validation with za string
    assert tests3.string_validation_on_success("za") == True

def test_string_3():
    ## Testing String Validation with zx string
    assert tests3.string_validation_on_failure("zx") == True

def test_string_4():
    ## Testing String Validation with aab string
    assert tests3.string_validation_on_failure("aab") == True
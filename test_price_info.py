import price_info as pi

def test_total_cost_shopping():
    result = pi.total_cost_shopping()
    assert (result == 46.75)
def test_cost_of_fruits():
    input_quant = 5
    fruit = "orange"
    result = pi.cost_of_fruits(fruit, input_quant)
    assert (result == 7)
import price_info

print("test price info")

def test_total_cost_shopping():
  
    result = price_info.total_cost_shopping()
    assert (result==46.75)

def test_cost_of_fruit():

    input_quant = 5
    input_fruit = "apple"
    result = price_info.cost_of_fruits(input_fruit,input_quant)
    assert (result == 12)
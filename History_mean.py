def initialize(context):
    context.jpm = sid(25006)
    context.xli = sid(19657)

def handle_data(context, data):
    price_history  = history(100, '1d', 'price')  
    mean = price_history.mean() 
    price_jpm = mean[context.jpm]    
    price_xli = mean[context.xli]
    diff_prices  =    price_jpm  -   price_xli 

    if price_jpm > diff_prices:  
        order(context.jpm, 10)

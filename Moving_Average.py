'''

http://www.tradingmarkets.com/recent/short_term_trading_strategies_that_work_7_stocks_you_need_to_know__axp_cop_dis_f_ibm_nke_ups_-1113144.html

1. Only buy stocks trading above their 200-day moving averages.
Going back to 1995, the average stock has had a 5-day gain of 0.28% 
when trading above the 200-day moving average.
Below the 200-day moving average, the average 5-day gain drops to 0.18%.

'''
def initialize(context): 
    #Execute one security at a time 
    context.security = sid(679) #American Express 
#    context.security = sid(18034) #Ford
#    context.security = sid(33472)  #NIKE
#    context.security = sid(3766)  #IBM
#    context.security = sid(2190) #Walt Disney
#    context.security = sid(23998) #ConcoPhillips
#    context.security = sid(20940) #United Parcel Services    

def handle_data(context, data):
    average_price = data[context.security].mavg(200)
    current_price = data[context.security].price  
    cash = context.portfolio.cash
    log.info(cash)
    if current_price > average_price:   
        number_of_shares = int(cash/current_price)
        order(context.security, +number_of_shares)
        log.info("Buying %s" % (context.security.symbol))  
    elif current_price < average_price:
        order_target(context.security, 0)
        log.info("Selling %s" % (context.security.symbol))
    #record(stock_price=data[context.security].price)

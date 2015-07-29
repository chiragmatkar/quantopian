#Calculate SP 500 Function
def get_SP500():
    fundamentals = init_fundamentals()
    sp_500 = get_fundamentals(
                        query(fundamentals.valuation.market_cap,
                             fundamentals.company_reference.primary_exchange_id)
                        .filter(fundamentals.valuation.market_cap > 4e9)
                        .filter(fundamentals.company_reference.country_id == "USA")
                        .filter(or_(fundamentals.company_reference.primary_exchange_id == "NAS", fundamentals.company_reference.primary_exchange_id == "NYS"))
                        .order_by(fundamentals.valuation.market_cap.desc())
                        .limit(500),
                        "2015-05-31")  # S&P 500 rebalances on an as needed basis, so we'll just use today
    z=sp_500[-1:]
    symbols = [equity.symbol for equity in z.columns]
    return   symbols

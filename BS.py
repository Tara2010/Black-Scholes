from scipy.stats import norm
def call_price(S,K,T,r,vol):
    d1 = (log(S/K)+(r+vol**2/2)*T)/(vol*sqrt(T))
    d2 = d1-vol*sqrt(T)
    price = S*norm.cdf(d1)-K*e**(-r*T)*norm.cdf(d2)
    return price
    

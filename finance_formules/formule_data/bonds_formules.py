from core_forules import calculate_present_value_annuity_factor_end_year_payment, calculate_the_discount_factor

def zero_coupon_bond_yield_to_maturity(n, N, po):
    """
    Calculate the yield to maturity (YTM) for a zero-coupon bond.

    Args:
        Nominal (float): The value of the bond.
        Present value (float): The current price of the bond.
        periods (int): The number of periods until maturity.

    Returns:
        float: The yield to maturity (YTM) as a decimal (e.g., 0.05 for 5%).
    """

    r = (N / po) ** (1 / n) - 1
    return round(r, 3)

def calculate_zero_coupon_bond_price(n, N, r):
    price = N/(1 + r) **n
    return price

def calculate_coupon_bond_price(n, N, c, r):
    """
    Calculate the price of a coupon bond.

    Args:
        n (int): The number of periods until maturity.
        N (float): The face value (or par value) of the bond.
        c (float): The coupon rate (as a decimal, e.g., 0.05 for 5%).
        r (float): The yield to maturity (as a decimal, e.g., 0.05 for 5%).

    Returns:
        float: The price of the coupon bond.
    """
    c = N * c # Calculate the coupon payment.
    if c == r: # If the coupon rate equals the yield, the price equals the face value.
        return N

    price = c * calculate_present_value_annuity_factor_end_year_payment(r, n) + N * calculate_the_discount_factor(r, n)
    return price

def calculate_coupon_bond_yield_to_maturity(c, N, p, n, payment_period=None):
    """
        Calculate the approximate yield to maturity (YTM) for a coupon bond.

        Args:
            c (float): Annual coupon rate (e.g., 0.05 for 5%).
            N (float): Face value of the bond.
            p (float): Current price of the bond.
            n (int): Number of years to maturity.
            payment_period (int, optional): If provided, indicates the payment period (e.g., 6 for semi-annual).

        Returns:
            float: Approximate yield to maturity (YTM).
        """

    if payment_period is not None:
        n = n * 12 / payment_period
        c = (c * N) / (12 / payment_period)
    else:
        c = c * N

    ytm = (c + (N - p) / n) / ((N + p) / 2)
    return round(ytm, 5)


# print(zero_coupon_bond_yield_to_maturity(3, 1000, 793.83))
# print(calculate_coupon_bond_price(5, 1000, 0.2, 0.18))
# print(calculate_coupon_bond_yield_to_maturity(0.08, 1000, 1080, 5, 3))

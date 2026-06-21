def get_link_len(stroke):
    ratio = stroke / 100
    a = ratio * 26  # ecc
    b = ratio * 80  # ternary link len - rocker side
    c = ratio * 90  # rocker len
    d = ratio * 37.5  # rocker y
    e = ratio * 117.5  # rocker x
    f = ratio * 117.5  # ternary link len - conrod side
    g = ratio * 117.5  # conrod len
    h = ratio * 0  # slide offset
    tht = 134 # ternary link angle deg

    link_lst = [a, b, c, d, e, f, g, h, tht]
    return link_lst

# all dims in mm
def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    b = 1
    while h > window:
        h *= bounce
        if h > window:b += 2
    return b
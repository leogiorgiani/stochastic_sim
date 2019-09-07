def chisq(X, n_div=10):
    n = len(X)
    exp = n / n_div

    obs = [0 for i in range(n_div)]

    for i in X:
        obs[int(i*n_div)] += 1

    chi = 0
    for i in range(n_div):
        chi += (obs[i] - exp)**2

    return chi/exp
    
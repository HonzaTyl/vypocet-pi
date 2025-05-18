# Výpočet π pomocí Leibnizovy řady
def calculate_pi(n_terms=5):
    pi = 0
    for k in range(n_terms):
        pi += ((-1) ** k) / (2 * k + 1)
    return 4 * pi

if __name__ == "__main__":
    print("Odhad π:", calculate_pi(5))

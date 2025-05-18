# pi_calculation.py

import random

def calculate_pi_leibniz(n_terms: int = 1000000) -> float:
    """Calculate pi using Leibniz series."""
    pi = 0.0
    for k in range(n_terms):
        pi += ((-1) ** k) / (2 * k + 1)
    return 4 * pi


def calculate_pi_nilakantha(n_terms: int = 1000000) -> float:
    """Calculate pi using Nilakantha series."""
    pi = 3.0
    sign = 1
    for k in range(2, 2 + 2 * n_terms, 2):
        pi += sign * (4 / (k * (k + 1) * (k + 2)))
        sign *= -1
    return pi


def calculate_pi_monte_carlo(n_samples: int = 1000000) -> float:
    """Estimate pi using Monte Carlo method."""
    inside = 0
    for _ in range(n_samples):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / n_samples


def compute_area(radius: float, pi_value: float) -> float:
    """Compute area of a circle with given radius and pi."""
    return pi_value * radius * radius

# Alias for backward compatibility
calculate_pi = calculate_pi_leibniz

def get_user_choice() -> int:
    print("Vyberte algoritmus pro výpočet π:")
    print("1) Leibnizova řada")
    print("2) Nilakantha řada")
    print("3) Monte Carlo")
    while True:
        choice = input("Zadejte číslo (1-3): ")
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Neplatná volba, zkuste to znovu.")


def main():
    choice = get_user_choice()
    n = int(input("Zadejte počet iterací/vzorků: "))
    radius = float(input("Zadejte poloměr kruhu: "))
    if choice == 1:
        pi = calculate_pi_leibniz(n)
        alg = "Leibnizova řada"
    elif choice == 2:
        pi = calculate_pi_nilakantha(n)
        alg = "Nilakantha řada"
    else:
        seed = input("Chcete nastavit seed? (enter pro skip): ")
        if seed:
            random.seed(int(seed))
        pi = calculate_pi_monte_carlo(n)
        alg = "Monte Carlo"
    area = compute_area(radius, pi)
    print("\nVýsledky:")
    print(f"Algoritmus: {alg}")
    print(f"Iterace/vzorky: {n}")
    print(f"Odhad π: {pi:.6f}")
    print(f"Poloměr: {radius:.6f}")
    print(f"Plocha kruhu: {area:.6f}")

if __name__ == "__main__":
    main()

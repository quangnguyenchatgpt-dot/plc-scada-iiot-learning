"""Numerical derivative lab for week 01 (Python standard library only)."""

def f(x: float) -> float:
    return x**3 - 4*x**2 + 2*x


def analytic_derivative(x: float) -> float:
    return 3*x**2 - 8*x + 2


def forward_difference(x: float, step: float) -> float:
    return (f(x + step) - f(x)) / step


def central_difference(x: float, step: float) -> float:
    return (f(x + step) - f(x - step)) / (2 * step)


if __name__ == "__main__":
    for x in (0.0, 2.0):
        expected = analytic_derivative(x)
        print(f"x={x}, analytical={expected:.6f}")
        for h in (0.1, 0.01, 0.001):
            fd = forward_difference(x, h)
            cd = central_difference(x, h)
            print(
                f"  h={h}: forward={fd:.6f}, central={cd:.6f}, "
                f"error_forward={abs(fd-expected):.6f}, "
                f"error_central={abs(cd-expected):.6f}"
            )

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def system(t, y):
    x, v = y
    return [v, -x]


def main():
    result = solve_ivp(
        system,
        (0, 20),
        [1.0, 0.0],   # x(0)=1, v(0)=0
        t_eval=[i * 0.05 for i in range(401)],
    )

    if not result.success:
        raise RuntimeError(result.message)

    x_values = result.y[0]
    v_values = result.y[1]

    print("Final x:", x_values[-1])
    print("Final v:", v_values[-1])

    plt.plot(result.t, x_values, label="x(t)")
    plt.plot(result.t, v_values, label="v(t)")
    plt.xlabel("t")
    plt.legend()
    plt.title("Simple harmonic oscillator")
    plt.show()


if __name__ == "__main__":
    main()
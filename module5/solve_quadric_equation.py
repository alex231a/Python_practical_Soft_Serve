import cmath


def solve_quadric_equation(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a == 0:
            raise ZeroDivisionError("Zero Division Error")

        discriminant = (b ** 2) - (4 * a * c)
        sqrt_discriminant = cmath.sqrt(discriminant)

        x1 = (-b - sqrt_discriminant) / (2 * a)
        x2 = (-b + sqrt_discriminant) / (2 * a)

        return f"The solution are x1={x1} and x2={x2}"

    except ZeroDivisionError as e:
        return str(e)

    except ValueError:
        return "Could not convert string to float"


# Example usage:
print(solve_quadric_equation(1, 5, 6))  # Output: The solutions are x1=(-2-0j) and x2=(-3+0j)
print(solve_quadric_equation(0, 8, 1))  # Output: Zero Division Error
print(solve_quadric_equation(1, "abc", 5))  # Output: Could not convert string to float







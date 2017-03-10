import math

def rata(c, d, n, p):
    """Calculator pentru credite

    Args:
        c - Credit (e.g 10000)
        d - Dobanda Anuala (e.g 0.30)
        n - Numar Ani (e.g. 1)
        p - Perioade pe an (e.g 12)

    Returns:
        Rata lunara
    """
    return c * d / (p*(1- pow((1+(d/p)), (-n*p))))

def main():
    rata(c, d, n, p)

if __name__ == '__main__':
    main()

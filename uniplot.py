def clamped_cubic_interpolation(x, y, smoothness=100):
    """
    Use this function to obtain the cubic interpolation of a set of data points.
    
    Example:

    ```
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4, 5, 6]
    y = [0.13, 0.27, 2.10, 0.52, 0.23, 0.13]

    plt.plot(x, y, 'o', label='Data points')
    x_plt, y_plt = clamped_cubic_interpolation(x, y)
    plt.plot(x_plt, y_plt, '-', label='Cubic interpolation')

    plt.show()
    ```
    """
    from numpy import linspace
    from scipy.interpolate import CubicSpline
    xnew = linspace(x[0], x[-1], num=len(x)*smoothness, endpoint=True)
    f_cubic = CubicSpline(x, y, bc_type='clamped')
    return xnew, f_cubic(xnew)

def loose_interpolation(x, y, smoothness=100):
    """
    Use this function to obtain a loose interpolation of a set of data points.
    The interpolation will not necessarily go through all the data points, but
    will try to go as close to all as possible, while maintainig smoothness.
    
    Example:

    ```
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4, 5, 6]
    y = [0.13, 0.27, 2.10, 0.52, 0.23, 0.13]

    plt.plot(x, y, 'o', label='Data points')
    x_plt, y_plt = loose_interpolation(x, y)
    plt.plot(x_plt, y_plt, '-', label='Loose interpolation')

    plt.show()
    ```
    """
    from numpy import linspace
    from csaps import csaps
    xs = linspace(x[0], x[-1], len(x)*smoothness, endpoint=True)
    return xs, csaps(x, y, xs, smooth=0.85)

def monotonic_interpolation(x, y, smoothness=100):
    """
    Use this function to obtain a tight interpolation of a set of data points,
    with monotonic polynomials interpolating between each pair of data points.
    This interpolation is similar to the one obtained when plotting data in 
    Excel.
    
    Example:
    
    ```
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4, 5, 6]
    y = [0.13, 0.27, 2.10, 0.52, 0.23, 0.13]

    plt.plot(x, y, 'o', label='Data points')
    x_plt, y_plt = monotonic_interpolation(x, y)
    plt.plot(x_plt, y_plt, '-', label='Monotonic interpolation')

    plt.show()
    ```
    """
    from scipy.interpolate import PchipInterpolator 
    from numpy import linspace
    xi = linspace(x[0], x[-1], len(x)*smoothness, endpoint=True)
    f = PchipInterpolator(x, y)
    yi = f(xi)
    return xi, yi


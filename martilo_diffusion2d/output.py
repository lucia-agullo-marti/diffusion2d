import matplotlib.pyplot as plt

def create_plot(fig,fig_counter,u,T_cold,T_hot,n,dt):
    """
    Creates one plot for one time stamp.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The matplotflib figure to which the subplot will be added.
    subplot_index : int
        The index (1-4) of the subplot position within the figure.
    u : numpy.ndarray
        The 2D temperature array at the current time step.
    T_cold : float
        Minimum temperature value for color scaling.
    T_hot : float
        Maximum temperature value for color scaling.
    n : int
        Current time step index.
    dt : float
        Time step size (s).

    Returns
    ----------
    ax : matplotlib.axes._axes.Axes
        The subplot axis created for this time step.
    im : matplotlib.image.AxesImage
        The image object representing the temperature field.
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))

    return ax, im


def output_plots(fig,im):
    """
    Outputs all four plots as one figure with a shared color bar.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure containing all subplots.
    im : matplotlib.image.AxesImage
        The last image object used to generate the color bar scale.

    Returns
    ----------
    None
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad = 20)
    fig.colorbar(im,cax=cbar_ax)
    plt.show()
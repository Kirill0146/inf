def G(g):
    """Строит графики зависимости V(t), r(t)"""

    import matplotlib.pyplot as plt
    import numpy as np

    print(g.t_t)
    #subplot 1
    sp = plt.subplot(211)
    plt.plot(g.t_t, g.V_t)
    plt.ylabel(r'$V, м/с$') #подпись по Y
    #plt.title(r'$V(t)$')
    plt.grid(True)

    #subplot 2
    sp = plt.subplot(212)
    plt.plot(g.t_t, g.r_t,'g')
    plt.xlabel(r'$t, с$') #подпись по X
    plt.ylabel(r'$r, м$') #подпись по Y
    plt.grid(True)
    #plt.title(r'$r(t)$')

    plt.show()

from os import unlink
from random import randint
from re import compile, search, DOTALL

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from spb import PB

svg_rgx = compile(r'<svg(.*)</svg>', DOTALL)


def _set_defaults(**kwargs):
    kwargs['backend'] = kwargs.get('backend', PB)
    kwargs['show'] = False
    return kwargs

def create_svg(plot):
    svg = ''
    fname = f"{randint(1, 999999)}.svg"
    plot.save(fname, format='svg')
    with open(fname, 'rb') as fp:
        out = fp.read()
    txt = out.decode('utf-8')
    match = search(svg_rgx, txt)
    if match:
        raw = match.group().strip().replace("\\n", " ")
        svg = raw.strip()
    unlink(fname)
    return svg

def mpl_axes(step=1.0, box_aspect=1.0, axis_arrows=True, grid_lines=None, xticks_off=False, yticks_off=False):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(MultipleLocator(step))
    ax.yaxis.set_major_locator(MultipleLocator(step))
    ax.set_box_aspect(box_aspect)
    if xticks_off:
        ax.tick_params(
            axis='x',
            labelsize='0',
            length=0
        )
    if yticks_off:
        ax.tick_params(
            axis='y',
            labelsize='0',
            length=0
        )
    if grid_lines in ('solid', 'dashed', 'dashdot', 'dotted'):
        ax.grid(True, linestyle=grid_lines)
    if axis_arrows:
        ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    return ax

import sys
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_pdf import PdfPages


df = pd.read_csv(sys.argv[1], sep='\s+')
filename, file_extension = os.path.splitext(sys.argv[1])

f, axis = plt.subplots(2, 1, sharex=True)

plotcm='tab10'
plotlog=False

df.plot(kind='bar', logy=plotlog, ax=axis[0], ec='k', lw=0.2, colormap=plotcm, width=0.7)
df.plot(kind='bar', logy=plotlog, ax=axis[1], ec='k', lw=0.2, colormap=plotcm, width=0.7)

plt.axhline(1, color='k', lw=1.0, ls='dotted')
plt.xticks(rotation=45)

axis[0].set_ylim(12, 24)
axis[1].set_ylim(0, 6)
axis[1].legend().set_visible(False)

axis[0].xaxis.tick_top()
axis[0].spines['bottom'].set_visible(False)
axis[1].spines['top'].set_visible(False)
axis[0].tick_params(labeltop='off')
axis[1].xaxis.tick_bottom()

# print axis[0].get_yticks()
yticks = axis[0].get_yticks()
yticks = map(lambda x: str(int(x)) + "x", yticks)
for i in range(len(yticks)):
    if i % 2:
        yticks[i] = ""
axis[0].set_yticklabels(yticks)

# print axis[1].get_yticks()
yticks = axis[1].get_yticks()
yticks = map(lambda x: str(int(x)) + "x", yticks)
for i in range(len(yticks)):
    if not i % 2:
        yticks[i] = ""
axis[1].set_yticklabels(yticks)


d = .015

kwargs = dict(transform=axis[0].transAxes, color='k', clip_on=False)
axis[0].plot((-d,+d),(-d,+d), **kwargs)
axis[0].plot((1-d,1+d),(-d,+d), **kwargs)

kwargs.update(transform=axis[1].transAxes)
axis[1].plot((-d,+d),(1-d,1+d), **kwargs)
axis[1].plot((1-d,1+d),(1-d,1+d), **kwargs)

plt.tight_layout()

pp = PdfPages(filename + '.pdf')
plt.savefig(pp, format='pdf')
pp.close()

plt.show()

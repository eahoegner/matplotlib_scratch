# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
data = np.random.random((10,50))

# %%
layout = [
    ["B", "C"],
    ["A", "A"]
]

fig, axd = plt.subplot_mosaic(layout, figsize=(7,5))

axd['A'].imshow(data, cmap="grey")
axd['A'].set_title('2D plot')

axd['B'].hist(data[0], color="green")
axd['B'].set_title('Histogram')

axd['C'].plot(data[0], data[1], color="purple")
axd['C'].set_title("Line plot");

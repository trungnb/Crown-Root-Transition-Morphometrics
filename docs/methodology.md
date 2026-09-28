# Methods represented in the notebooks

1. Use CT/NIfTI images and existing tooth masks. Crop and align teeth by their principal axes.
2. Apply binary erosion to construct outer shells with thicknesses from one to five voxels.
   Export per-slice shell counts, mean / standard deviation / minimum / maximum HU and `z_mm`.
3. Compare profiles across shell thicknesses. In the ratio notebooks, use shell-3 profiles
   and search within 10–90% of the profile for two stable regions separated by a transition.
4. Score candidate splits using differences between regional mean / maximum HU,
   within-region variability, and a position weight. The maximum transition fraction
   depends on tooth type: 0.25 for incisors, 0.20 for canines / premolars, 0.15 for molars.
5. Use profile direction to assign the crown side. The saved numerator is crown **plus
   transition**, divided by the root extent; calculate slice-based and millimetre-based ratios.
6. Separately inspect a single tooth through mask hole filling, cropping, PCA alignment
   and interactive Matplotlib / Plotly slice views in `Pulp.ipynb`.

## Saved-result presentation
The README uses only `crown_root_ratio_dynamic_10_90.csv` and its Person2 counterpart.
Other historical ratio variants remain in the author's local archive; they are not pooled.
`ratio_summary.csv` computes count, median, minimum and maximum from the saved millimetre
ratio column. This is a descriptive summary of existing values, not a new CEJ analysis.

The figure shows all 16 ratios for each case. Connecting lines join the same FDI tooth
number across two different cases; they are not longitudinal changes. The HU panel
uses the upper right central incisor (FDI 11), shell thickness three voxels. Its `z_mm`
axis is shifted to start at zero independently in each case, without recalculating alignment.

The original notebook heuristics are preserved. This release does not establish
anatomical CEJ accuracy, agreement with a reference rater, or clinical utility.

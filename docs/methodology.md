# Methods represented in the notebooks

These notebooks preserve an early exploratory implementation. The workflow is CEJ-oriented,
but the detected transition should be interpreted as an **intensity-derived crown–root
transition proxy**, not as a validated anatomical CEJ.

1. Use CT/NIfTI images and existing tooth masks. Crop and align teeth by their principal axes.
2. Apply binary erosion to construct outer shells with thicknesses from one to five voxels.
   Export per-slice shell counts, mean / standard deviation / minimum / maximum intensity and
   the historical `z_mm` field.
3. Compare profiles across shell thicknesses. In the ratio notebooks, use shell-3 profiles
   and search within 10–90% of the profile for two stable regions separated by a transition.
4. Score candidate splits using differences between regional mean / maximum intensity,
   within-region variability, and a position weight. The maximum transition fraction
   depends on tooth type: 0.25 for incisors, 0.20 for canines / premolars, 0.15 for molars.
5. Use profile direction to assign the crown side. The saved numerator is crown **plus
   transition**, divided by the root extent; calculate slice-based and historical
   millimetre-labelled ratios.
6. Separately inspect a single tooth through mask hole filling, cropping, PCA alignment
   and interactive Matplotlib / Plotly slice views in `Pulp.ipynb`.

## Important methodological limitations

The original implementation is preserved rather than retrospectively rewritten.

- PCA is calculated from voxel-index coordinates rather than explicitly from physical/world
  coordinates. This can matter when voxel spacing is anisotropic.
- After rotation, the historical code derives `z_mm` using the original image z-spacing.
  Therefore the saved millimetre-labelled lengths and ratios are exploratory outputs rather
  than validated physical morphometric measurements.
- Shell thickness is defined by erosion iterations in voxels rather than by a physical
  surface distance in millimetres.
- The shell-intensity volume is interpolated during rotation. Boundary interpolation may
  influence the profile used by the subsequent transition heuristic.
- The 10–90% search range, minimum stable-region length, position weighting, and
  tooth-type-specific transition fractions are hand-crafted prototype assumptions.
- No anatomical CEJ reference annotation was used to estimate localisation error, agreement,
  sensitivity, specificity, or clinical utility.

For a future validated implementation, the geometry should be represented in physical
coordinates or resampled to an isotropic grid, shell thickness should be defined in
millimetres, intensity features should be made robust to acquisition effects, and transition
locations should be compared with independent anatomical reference annotations.

## Saved-result presentation

The README uses only `crown_root_ratio_dynamic_10_90.csv` and its Person2 counterpart.
Other historical ratio variants remain in the author's local archive; they are not pooled.
`ratio_summary.csv` computes count, median, minimum and maximum from the saved
`crown_root_ratio_mm` column. This is a descriptive summary of existing values, not a new
CEJ analysis.

The figure shows all 16 ratios for each case, including extreme values. These values are
retained to expose prototype failure modes rather than filtered according to anatomical
plausibility. Connecting lines join the same FDI tooth number across two different cases;
they are not longitudinal changes. The intensity-profile panel uses the upper right central
incisor (FDI 11), shell thickness three voxels. Its `z_mm` axis is shifted to start at zero
independently in each case, without recalculating alignment.

The original notebook heuristics are preserved. This release does not establish anatomical
CEJ accuracy, validated crown–root morphometry, agreement with a reference rater, or clinical
utility.

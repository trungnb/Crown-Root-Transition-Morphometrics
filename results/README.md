# Saved results

| File | Contents | Original source |
|---|---|---|
| [Person1 ratios](crown_root_ratio_dynamic_10_90.csv) / [Person2 ratios](P2/crown_root_ratio_dynamic_10_90.csv) | 16 saved crown–root ratios per case; historical dynamic 10–90% variant | `ratio1.ipynb` / `ratio2.ipynb` |
| [Descriptive summary](ratio_summary.csv) | Count, median, minimum and maximum of saved `crown_root_ratio_mm` values | Saved ratio tables |
| [Person1 profile](3/upper_right_central_incisor_fdi11.csv) / [Person2 profile](P2/3/upper_right_central_incisor_fdi11.csv) | Per-slice intensity profile for FDI 11; shell thickness three voxels | `CEJ1.ipynb` / `CEJ2.ipynb` |
| [Overview SVG](figures/prototype-overview.svg) | Saved profiles and ratios | `scripts/render_figures.py` and selected CSVs |

Column names are preserved from the historical notebooks. `crown_trans_mm` includes the
transition zone; `root_mm` is the saved root extent; `crown_root_ratio_mm` is their saved
ratio, already rounded in the original export; and `trans_ratio_used` records the
tooth-type transition fraction.

The `*_mm` names are historical labels. Because the original prototype performed PCA in
voxel-index space and then used the source image z-spacing after rotation, these values should
not be treated as validated physical morphometric measurements. The detected transition is
also not a reference anatomical CEJ.

Large or anatomically implausible ratios are intentionally retained as prototype failure cases.
No outlier filtering or retrospective correction was applied for this portfolio release.
Profile statistics describe outer-shell voxels per slice. No raw images are published.

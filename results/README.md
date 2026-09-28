# Saved results

- [Person1 ratios](crown_root_ratio_dynamic_10_90.csv) and [Person2 ratios](P2/crown_root_ratio_dynamic_10_90.csv): 16 teeth each, historical dynamic 10–90% search variant.
- [Descriptive summary](ratio_summary.csv): count / median / minimum / maximum of the stored `crown_root_ratio_mm` column.
- [Person1 example intensity profile](3/upper_right_central_incisor_fdi11.csv) and [Person2 example intensity profile](P2/3/upper_right_central_incisor_fdi11.csv): FDI 11, shell thickness three voxels.
- [Overview SVG](figures/prototype-overview.svg): current portfolio figure rendered from these saved tables. `scripts/render_figures.py` contains the reproducible plotting logic.

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

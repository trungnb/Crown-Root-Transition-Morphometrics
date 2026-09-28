# Saved results

- [Person1 ratios](crown_root_ratio_dynamic_10_90.csv) and [Person2 ratios](P2/crown_root_ratio_dynamic_10_90.csv): 16 teeth each, dynamic 10–90% search variant.
- [Descriptive summary](ratio_summary.csv): count / median / minimum / maximum of the stored `crown_root_ratio_mm` column.
- [Person1 example HU profile](3/upper_right_central_incisor_fdi11.csv) and [Person2 example HU profile](P2/3/upper_right_central_incisor_fdi11.csv): FDI 11, shell thickness three voxels.
- [Overview PNG](figures/prototype-overview.png) / [SVG](figures/prototype-overview.svg): rendered with `scripts/render_figures.py` from these tables.

Ratio columns preserve historical names. `crown_trans_mm` includes the transition zone;
`root_mm` is the root extent. `crown_root_ratio_mm` is their saved ratio, already rounded
in the original export. `trans_ratio_used` records the tooth-type transition fraction.
Profile statistics describe outer-shell voxels per slice. No raw images are published.

# Data and notebook provenance

Packaged on 2026-09-28 from the author's existing project notebooks and saved result files.
No segmentation, model training, evaluation, or reproduction run was performed.

## Notebooks

Original analysis cell sources, parameters, and order are unchanged. Publication clears
session metadata, widget state, and output previews; no output cells are retained. The
`original SHA-256` values refer to local author backups that are not distributed. Hashes
identify the compared files; they do not establish that the historical analysis can be
reproduced.

| Notebook | Original SHA-256 | Published SHA-256 |
|---|---|---|
| `notebooks/CEJ1.ipynb` | `d43d1665f79f1d0905ee67573cb076e2c98ded63eb8cd09d9d71512130539b25` | `7aed77227370a3608cc0777e2a668c3d17b3091c933fe503d2057419601261b9` |
| `notebooks/CEJ2.ipynb` | `811595a3af250d866f2d443378f7c48f1b3ddbdc8a92eb860119c665fde3b6fe` | `c6576b64d0cbc717bfbdd7a5227dbceda3514238e4967fc9232d8d7a1dfb52e3` |
| `notebooks/ratio1.ipynb` | `92ac488a00c0ef0b8ac16a948b2d393fae002c3c67c9e5fcb59cb3c575b862ff` | `8e580fae70898a6aa96fd2933a65533c559749c1c615766c7afcff6c3bb97f1c` |
| `notebooks/ratio2.ipynb` | `48562edc75067e6d391a058191ca1e981bba33112f75cc29a1bb6423cc81b8d2` | `e32bc1cff7c1c590b7482cef85d7fde749725d98fb8eea5d34cb20f883d142a3` |
| `notebooks/Pulp.ipynb` | `57954ea7e42979677fc451bf153a3ddb3f93fb80706ff49b21a5b9bfcd6814ba` | `6689f580bbc9966adeb940c60f8210311f68e9447cca6b6e979e84e2ffa42df5` |

## Saved tables

The four profile and ratio source CSVs are existing saved files, byte-for-byte unchanged.
`results/ratio_summary.csv` is a descriptive aggregation of the saved `crown_root_ratio_mm`
values. These hashes fingerprint the published files; they do not identify the original
image acquisition, execution date, hardware, or analysis package versions.

| Published CSV | SHA-256 |
|---|---|
| `results/crown_root_ratio_dynamic_10_90.csv` | `575692c2470dcf2cd0a63ac56cee91828d4cfd9774f5b0d2eac25a4b9acf470b` |
| `results/P2/crown_root_ratio_dynamic_10_90.csv` | `5ce19415ecca6e1edc576cfe4bb8d182d052808f36b08867d6cc78fd2b84da31` |
| `results/3/upper_right_central_incisor_fdi11.csv` | `01eab8532b5cdff6043ddc476e17a0780ce7d20f3558e68574762d51e75d859c` |
| `results/P2/3/upper_right_central_incisor_fdi11.csv` | `2accc016a5838b2eba9af47b1aa18c14a5f4b1bbf84b80dab6db4712642090a0` |
| `results/ratio_summary.csv` | `fff022d6f49d4e4b68ce2d43b623dd8fa5f495f6acf19008835056c82524acd2` |

## Figure and publication scope

`results/figures/prototype-overview.svg` was rendered by `scripts/render_figures.py` from
the two selected FDI 11 profile CSVs and two dynamic 10–90% ratio CSVs. The renderer shifts
each saved `z_mm` profile to its own zero and formats the chart; it does not run image
processing or recalculate ratios. Figure and table interpretation is documented in the
[project README](../README.md).

Raw CT scans, tooth masks, acquisition/consent records, unrelated notebooks, and local
backups are excluded. The input data version is not established by the published tables.
See [`LICENSE`](../LICENSE) for reuse status. Code links to external packages or datasets
do not transfer their licenses.

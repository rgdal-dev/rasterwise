# AVISO mean dynamic topography (CNES-CLS09, RIO07 Mediterranean): lon-major grids that GDAL georeferences with latitude as x

Two of AVISO's auxiliary mean dynamic topography (MDT) products are stored lon-major, (lon, lat): CNES-CLS09 v1.1 (global, 1/4 degree) and RIO07 (Mediterranean, 1/8 degree). The archive holds private copies of them. Their axes are regular, unlike the old AVISO Mercator grid. That makes things worse: GDAL hands back a tidy geotransform with latitude across and longitude down, and nothing errors. The CNES-CLS13 successor is CF, stored (time, lat, lon), and reads correctly.

| canonical_path | sha256 | size |
|---|---|---|
| raad/aviso-mdt/mdt_cnes_cls2009_global/mdt_cnes_cls2009_global_v1.1.nc | 38db0841edef | 50822704 |
| raad/aviso-mdt/mdt_cnes_cls2009_global/mdt_cnes_cls2009_global_v1.1.ascii | 72254e15b429 | 62944900 |
| raad/aviso-mdt/mdt_cnes_cls2009_global/readme_mdt_cnes_cls2009_global_v1.1_nc.txt | dd5ce265446f | 3786 |
| raad/aviso-mdt/mdt_cnes_cls2009_global/readme_mdt_cnes_cls2009_global_v1.1_ascii.txt | a29d3f2e347b | 3964 |
| raad/aviso-mdt/mdt_rio2007_mediterranean/mdt_rio2007_mediterranean.nc | fd6105f271f3 | 525376 |
| raad/aviso-mdt/mdt_rio2007_mediterranean/mdt_rio2007_mediterranean.ascii | 3b4f12347880 | 1204942 |
| raad/aviso-mdt/mdt_rio2007_mediterranean/readme_mdt_rio2007_mediterranean_nc.txt | 82401b811631 | 1204 |
| raad/aviso-mdt/mdt_rio2007_mediterranean/readme_mdt_rio2007_mediterranean_ascii.txt | 9a7aff2d78c6 | 1172 |
| raad/aviso-mdt/mdt_cnes_cls2013_global.nc | ade511135fb7 | 24912636 |

## What's wrong

- **Lon-major.** `Grid_000k(NbLongitudes, NbLatitudes)`: latitude is the fastest-varying dimension. CLS09 has 7 grids (height, U, V, three errors, a 0/1 flag); RIO07 has 3 (H, U, V).
- **A transposed geotransform with no warning.** The axes are regular (CLS09: 0.25 degree, latitude -89.875..89.875, longitude 0.125..359.875; RIO07: 0.125 degree), so GDAL's classic view builds a geotransform. For CLS09 it is 720 x 1440 with origin (-90, 360): x is latitude and y is descending longitude. No CRS is set, so assigning EPSG:4326 gives a wrong map that looks normal.
- **RIO07 longitudes run past 360**: 355 to 396.875 (5 W to 36.875 E), in both the netCDF and the ascii file.
- **CLS09 height has two 9999 cells** at 279.875 E, 2.875 S and 2.625 S. U, V and the errors are ordinary values there. 9999 is the readme's ascii "default value"; it is not the netCDF `_FillValue` (1.84467e19).
- **Coverage.** CLS09 data stop at 80.125 N, not the readme's 80.625 N. In RIO07, H is valid at 16902 cells but U and V only at 15557.
- **The ascii forms** list the netCDF values exactly (max difference 0), lon-major with latitude ascending, fill cells omitted. RIO07's ascii keeps only cells with valid U/V, so 1345 heights are dropped, and its readme names a different file (`cmdt_riomed.asc`).
- **The readmes are ISO-8859-1** (degree and one-quarter signs), not UTF-8.
- **CNES-CLS13 fixed the layout**: CF-1.6, int32 (time, lat, lon) with `scale_factor` 1e-4, bounds and a sphere `crs`. Leftover faults: `lat_bnds` pairs are upper-then-lower, `err_v` has units "m", and `time` has no coordinate variable. Its mean is referenced to 1993-2012; CLS09's is 1993-1999.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07:

```sh
gdalmdimtranslate mdt_cnes_cls2009_global_v1.1.nc mdt09.tif \
  -array "name=Grid_0001,transpose=[1,0],view=[::-1,:]"
gdal_translate mdt09.tif mdt09_ll.tif -a_srs EPSG:4326 -a_ullr 0 90 360 -90

gdalmdimtranslate mdt_rio2007_mediterranean.nc rio.tif \
  -array "name=Grid_0001,transpose=[1,0],view=[::-1,:]"
gdal_translate rio.tif rio_ll.tif -a_srs EPSG:4326 -a_ullr -5.0625 46.0625 36.9375 29.9375
```

Each output equals the stored array transposed with latitude reversed. 3000 random stored (lon, lat) pairs each fell in a cell holding the matching value. For CLS09 height, also treat 9999 as missing. The CRS label is nominal: CLS09 and RIO07 declare none. CNES-CLS13 reads correctly by default (3000 random cells matched). CLS13 minus the corrected CLS09 has mean -0.015 m and s.d. 0.053 m over common cells, which confirms the orientation.

## Related

- [../aviso-mercator-as-lonlat/](../aviso-mercator-as-lonlat/): the same lon-major AVISO layout on a Mercator grid (no geotransform there, so the problem is at least visible)
- [../acc-fronts-mercator/](../acc-fronts-mercator/)
- regular-in-what: [costumes table](https://hypertidy.github.io/regular-in-what/03-costumes.html)

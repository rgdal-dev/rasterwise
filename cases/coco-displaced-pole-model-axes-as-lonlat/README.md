# COCO Southern Ocean ice-ocean output: displaced-pole model coordinates labelled as longitude and Mercator-spaced latitude

Daily sea ice concentration (`ai`) and thickness (`hi`) from the COCO ice-ocean model, Southern Ocean configuration, 2016, with the model's static grid files (`geoinfo/`). They come from a user's research working area, held as a private copy. The data files carry 1D `longitude`/`latitude` axes that look like the old AVISO Mercator grid: uniform longitude, Mercator-spaced latitude. They are not geographic. They are the model's own coordinates, whose south pole has been moved to 82 S, 45 E. Take them as lon/lat and cells land a median 45 degrees of arc from where they belong. The true positions are in separate 2D files, and those turn out to be regular in a short PROJ pipeline.

| canonical_path | sha256 | size |
|---|---|---|
| raad/coco-ice-ocean/output/concentration/ai.2016.nc | fc71d8b64fe1 | 70439503 |
| raad/coco-ice-ocean/output/thickness/hi.2016.nc | 36f263eb52a8 | 77214426 |
| raad/coco-ice-ocean/geoinfo/lon0.nc ... lon4.nc | cdc8a718b5fc f0ba9ade0349 2f4b076d0c60 665a4a26399f 672d6bfbe9a8 | ~791 KB each |
| raad/coco-ice-ocean/geoinfo/lat0.nc ... lat4.nc | 8e4c2eb4f759 c82d55ed0359 15011641947e 0dc1dd63d66d 8dd05c7aa000 | ~730 KB each |
| raad/coco-ice-ocean/geoinfo/angle.nc | 87a1732e70b4 | 908842 |
| raad/coco-ice-ocean/geoinfo/xscale.nc, yscale.nc | f2712fda3118 b89f15767ebd | 632658, 629395 |
| raad/coco-ice-ocean/geoinfo/mask.nc, depth.nc, draft.nc | 4aaeec41061d 25c37a705f48 d6d1f4c8d878 | 28881, 470339, 36871 |

## What's wrong

- **Model coordinates in a lon/lat costume.** `longitude(1024)` is 0.176 to 359.82 in steps of 360/1024; `latitude(384)` is -80.28 to -34.61, with a constant step of 0.272250 degrees in spherical Mercator y (relative spread 1.5e-4). Units say `degrees_east` and `degrees_north`. The real centres (`lon0`/`lat0`) reach -88.24 to -28.40 latitude, and column 0 is at about 226 E. Using the 1D axes moves cells a median 44.6 degrees of arc (max 105) and up to 8 degrees in latitude.
- **GDAL takes the bait.** Its classic view of `ai`/`hi` has no geotransform and GEOLOCATION metadata pointing at the 1D axes with EPSG:4326. It also reports NoData 9.96921e+36, which the files never hold.
- **What the grid really is.** In a spherical south polar stereographic plane, every row of `lon0`/`lat0` is a circle (relative residual < 1e-6) and all rows share one centre, the point 82.0 S, 45.0 E. Polar angle about that centre = 1D longitude - 135 degrees. Radius = 1.0024425 * tan(pi/4 + lat/2), with lat the 1D latitude. So the grid is a displaced-pole grid, uniform in angle and log-radius. A sphere rotation does not fit it (1.78 degrees off at worst). It is not tripolar. The constants are fitted; no file states them.
- **Not square in model space.** The y step is 0.7744 of the x step, and `yscale/xscale` is 0.7744 everywhere. The AVISO grid has equal steps.
- **Five lon/lat pairs = centre plus four corners.** In model-index units, 0 is the centre, 1 is (-1/2, -1/2), 2 is (+1/2, -1/2), 3 is (+1/2, +1/2) and 4 is (-1/2, +1/2). All five files carry the same centre 1D axes, which is why `lon4.nc`/`lat4.nc` were flagged as Mercator-spaced.
- **angle** (units "-", actually radians) is the model +column direction, counterclockwise from true east, up to 54.9 degrees. **xscale/yscale** are cell widths in metres.
- **mask**: 0 land, 1 ocean, 2 under an ice shelf (= `draft > 0`). **hi** never goes below 10.0, and it is exactly 10.0 wherever `ai == 0`, land included. There is no fill, so mask with `ai > 0`.
- **Time** is "secs since 0000-1-1" from 0 in each yearly file. The year exists only in the file name, and cftime refuses the reference year.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07. Give one day the model plane (x = model lon - 180 in degrees, y = Mercator y of model lat in degrees), then warp with the pipeline:

```sh
gdal_translate -b 201 -a_nodata none \
  -a_srs "+proj=merc +lon_0=180 +R=57.29577951308232 +no_defs" \
  -a_ullr -180 -36.7961890970 180 -141.3402971898 \
  hi.2016.nc hi_d201_model.tif
gdalwarp -s_srs "+proj=merc +lon_0=180 +R=57.29577951308232 +no_defs" \
  -t_srs EPSG:3031 -te -7500000 -7500000 7500000 7500000 -tr 5000 5000 -r near \
  -ct "+proj=pipeline +step +inv +proj=merc +lon_0=180 +R=57.29577951308232 +step +proj=stere +lat_0=-90 +lon_0=135 +R=0.5 +k_0=1.0024425 +step +proj=affine +xoff=0.0494457 +yoff=0.0494457 +step +inv +proj=stere +lat_0=-90 +lon_0=0 +R=0.5 +step +proj=stere +lat_0=-90 +lat_ts=-71 +lon_0=0 +ellps=WGS84" \
  -dstnodata -9999 hi_d201_model.tif hi_3031.tif
```

The pipeline reproduces `lon0`/`lat0` at all 393216 centres to within 6.5 m. 3000 random cells with `hi != 10`, each looked up in `hi_3031.tif` at its true position, all held the stored value. GDAL's classic read already flips the rows north-up. The -180 shift keeps the 0/360 seam from splitting the source: without it, half the grid came out empty. The generic alternative, using `lon0`/`lat0` as 2D geolocation, is untested here, and so is rotating ui/vi with `angle`.

## Related

- [../aviso-mercator-as-lonlat/](../aviso-mercator-as-lonlat/): Mercator-spaced latitude that is real geography; here the same costume hides a model coordinate system
- [../acc-fronts-mercator/](../acc-fronts-mercator/)
- [../cm21-tripolar-nominal-axes/](../cm21-tripolar-nominal-axes/): another ocean model whose 1D axes are not the true positions
- [../cryosat2-sea-ice-cryptic-curvilinear/](../cryosat2-sea-ice-cryptic-curvilinear/): 2D lon/lat that reduce to a CRS and an extent
- regular-in-what: [costumes table](https://hypertidy.github.io/regular-in-what/03-costumes.html)

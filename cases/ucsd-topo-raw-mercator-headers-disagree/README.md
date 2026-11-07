# UCSD global 1-minute topography: a headerless spherical Mercator grid whose ERS header, hand-written VRTs and netCDF all describe it differently

The UCSD global 1-minute topography (predicted bathymetry plus land) is
distributed as `topo_N.img`, a raw big-endian Int16 array with no header, on
a spherical Mercator grid. Over the versions it has come in three storage
forms: the raw array alone (costume A), the raw array with an ER Mapper
header (meant as costume B, but GDAL gets no geotransform from it), and,
from version 19.1, a netCDF on regular lon/lat (costume C). The netCDF is not
the same grid: it is a resample. A set of hand-written VRTs in the mirror's
hidden `.vrt/` directory puts cells up to 11 km out in latitude.

| canonical_path | sha256 | size |
|---|---|---|
| `raad/ucsd-global-topo-1min/topo_19.1.img` | `0804ca23ec39` | 746,496,000 |
| `raad/ucsd-global-topo-1min/topo_19.1.img.ers` | `c655276530af` | 822 |
| `raad/ucsd-global-topo-1min/topo_19.1.nc` | `a8744b2763ea` | 548,098,492 |
| `raad/ucsd-global-topo-1min/topo_27.1.img` | `477d7e804c65` | 746,496,000 |
| `raad/ucsd-global-topo-1min/topo_27.1.nc` | `254ed798d283` | 553,799,095 |
| `raad/ucsd-global-topo-1min/README_V19.1.txt` | `3c5a9030c220` | 17,413 |
| `raad/ucsd-global-topo-1min/.gmtcommands4` | `1063fe8c5fdc` | 85 |
| `raad/ucsd-global-topo-1min/.vrt/topo_19.1.vrt` | `ca35b9544ef0` | 873 |
| `raad/ucsd-global-topo-1min/.vrt/topo_19.1atlantic.vrt` | `ee410a420ea7` | 1,415 |
| `raad/ucsd-global-topo-1min/.vrt/topo_20.1.vrt` | `c975a7d309ad` | 551 |
| `raad/ucsd-global-topo-1min/.vrt/topo_20.1_atlantic.vrt` | `96f682741270` | 1,092 |

## What's wrong

Checked on the bytes on 2026-11-07, versions 19.1 and 27.1.

- **Raw, no header.** 21600 x 17280 Int16, big-endian, row 0 at the north.
  Read little-endian the values fill the whole Int16 range; big-endian they
  run about -10100 to 5700 m. Odd values mark cells constrained by a
  sounding; even values are predicted.
- **The grid.** Spherical Mercator, square pixels of one arcminute of
  longitude. Columns: centres at (j + 0.5)/60 degrees E, 0 to 360. Rows:
  equal steps in Mercator y, 8640 above and 8640 below the equator, so the
  edges are 80.738 N and 80.738 S. On EPSG:3857 the pixel is
  1855.3248465545596 m and y spans +-16030006.674 m. Checked against the
  producers' own `.nc` (RMS 0.9 to 3.2 m in four sample windows after
  warping; a quarter-cell shift makes it worse), and the leftover
  `.gmtcommands4` region snaps to exact row edges.
- **The README hides the layout.** Its format paragraph still describes the
  2-minute version 5.2 grid (6336 x 10800, +-72.006). The 1-minute numbers
  (21600 x 17280, +-80.738) and the byte order are in the version 9.1 change
  notes further down.
- **The ERS header is old and incomplete.** One 822-byte header, identical
  for 17.1, 18.1, 19.1 and 20.1, written for version 9.2 (LastUpdated
  2005). Versions 23.1 to 27.1 have none. It describes the raw layout
  correctly (GDAL's values equal the raw bytes) and says MRWORLD on a
  sphere with 1853.247 m cells, but has no RegistrationCoord, so GDAL
  returns a pixel-coordinate geotransform `(0, 1, 0, 0, 0, 1)`.
- **The `.nc` is a different grid.** `grdsample -R-180/180/-80/80 -I1m`:
  21600 x 9600 float32 on regular lon/lat, -180 to 180, 80 S to 80 N. It
  drops the rows beyond 80 degrees, rotates longitude by 180 degrees,
  interpolates the values, and so loses the odd/even sounding flag.
- **The hand-written VRTs misplace it.** All use pixels of 1855.325 x
  1850.436 m (not square) and a top edge of 15987768 m.
  - `topo_18.1.vrt`, `topo_19.1.vrt` and their atlantic variants use a
    6370997 m sphere: the right edge lands at 360.40 E, and latitude is off
    by up to 6.4 km.
  - `topo_20.1.vrt` and `topo_20.1_atlantic.vrt` use EPSG:3857: longitude
    is right, but latitude is off by up to 11.1 km (12 rows at 60 degrees),
    and the top edge is 80.677 N.
  - Warped to lon/lat they differ from the `.nc` by RMS 646 m (19.1) and
    319 m (20.1) off Japan, against 3 m for the correct grid.
  - `topo_18.1_unpolished.vrt` points at a file that does not exist.
- **Current GDAL refuses them anyway.** They reference `../topo_N.img` from
  a VRTRawRasterBand, and GDAL now rejects raw sources outside the VRT's
  directory unless `GDAL_VRT_RAWRASTERBAND_ALLOWED_SOURCE` is set.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07.

With the `.ers` (17.1 to 20.1), give GDAL the right grid:

```
gdal_translate -of VRT -a_srs EPSG:3857 \
  -a_ullr 0 16030006.674231391 40075016.686 -16030006.674231391 \
  topo_19.1.img.ers topo_19.1_0360.vrt
```

This runs 0 to 360 E; gdalwarp requests west of 0 came back as zeros. For -180 to 180,
swap the halves, as the atlantic VRTs do but with the correct geotransform:

```xml
<VRTDataset rasterXSize="21600" rasterYSize="17280">
  <SRS>EPSG:3857</SRS>
  <GeoTransform>-20037508.342789244, 1855.3248465545596, 0, 16030006.674231391, 0, -1855.3248465545596</GeoTransform>
  <VRTRasterBand dataType="Int16" band="1">
    <SimpleSource>
      <SourceFilename relativeToVRT="0">/abs/path/topo_19.1.img.ers</SourceFilename>
      <SourceBand>1</SourceBand>
      <SrcRect xOff="10800" yOff="0" xSize="10800" ySize="17280"/>
      <DstRect xOff="0" yOff="0" xSize="10800" ySize="17280"/>
    </SimpleSource>
    <SimpleSource>
      <SourceFilename relativeToVRT="0">/abs/path/topo_19.1.img.ers</SourceFilename>
      <SourceBand>1</SourceBand>
      <SrcRect xOff="0" yOff="0" xSize="10800" ySize="17280"/>
      <DstRect xOff="10800" yOff="0" xSize="10800" ySize="17280"/>
    </SimpleSource>
  </VRTRasterBand>
</VRTDataset>
```

`gdalwarp -t_srs EPSG:4326 -tr 0.016666666666666666 0.016666666666666666
-r cubic` from this reproduces `topo_19.1.nc` to RMS 0.9 to 3.2 m in four
5 x 5 degree windows.

Without a header (23.1 onward), describe the raw bytes yourself, using the
same SRS and geotransform, and allow the raw source:

```xml
<VRTRasterBand dataType="Int16" band="1" subClass="VRTRawRasterBand">
  <SourceFilename relativeToVRT="0">/abs/path/topo_27.1.img</SourceFilename>
  <ImageOffset>0</ImageOffset>
  <PixelOffset>2</PixelOffset>
  <LineOffset>43200</LineOffset>
  <ByteOrder>MSB</ByteOrder>
</VRTRasterBand>
```

```
gdalwarp --config GDAL_VRT_RAWRASTERBAND_ALLOWED_SOURCE ALL ...
```

For 27.1 this matches `topo_27.1.nc` to RMS 2.0 to 7.5 m (one Antarctic
window has a 531 m maximum difference; not investigated).

Any sphere works if the pixel is 2 pi R / 21600 in both directions;
EPSG:3857 is convenient because its inverse gives the grid's latitudes
exactly. Keep the Int16 if you need the sounding flag. The `.nc` is fine if
a resampled regular lon/lat grid to +-80 degrees is what you want.

## Links

- https://topex.ucsd.edu/pub/global_topo_1min/ (the source directory)
- https://hypertidy.github.io/regular-in-what/03-costumes.html
- https://gdal.org/drivers/raster/vrt.html#vrtrawrasterband_restricted_access

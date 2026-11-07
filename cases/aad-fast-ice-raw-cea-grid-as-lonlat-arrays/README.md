# AAD MODIS 20-day fast ice: headerless images stored south-up, geolocated by raw lat/lon arrays that are a 2 km cylindrical equal-area grid

Maps of East Antarctic landfast sea ice from the AAD public services
fast-ice dataset (modis_20day_fast_ice): 159 headerless byte images, plus a
pair of headerless float32 arrays giving the latitude and longitude of
every pixel. The images are costume A, the lat/lon pair costume E. The pair
is in fact separable (1D in disguise) and is an exact 2000 m grid in WGS84
Lambert cylindrical equal-area with standard parallel 65 S, so 3.6 million
stored coordinates reduce to a CRS and a geotransform. The rows are stored
south to north.

| canonical_path | sha256 | size |
|---|---|---|
| `raad/aad-modis-20day-fast-ice/imgs/2000_061-080_sqc.img` | `710a226e331a` | 1,827,500 |
| `raad/aad-modis-20day-fast-ice/imgs/2008_341-366_sqc.img` | `ddbb7f8b46a6` | 1,827,500 |
| `raad/aad-modis-20day-fast-ice/geo/lats.img` | `9ea0d2cfeeea` | 7,310,000 |
| `raad/aad-modis-20day-fast-ice/geo/lons.img` | `57c853e81268` | 7,310,000 |
| `raad/aad-modis-20day-fast-ice/geo/coastmask.img` | `8c6573fc07b2` | 3,655,000 |
| `raad/aad-modis-20day-fast-ice/README` | `48abaf47c29e` | 5,266 |
| `raad/aad-modis-20day-fast-ice/readme.txt` | `1c5fd359d929` | 3,493 |

## What's wrong

Checked on the bytes on 2026-11-07, all 159 images.

- **Only the README knows the shape.** Images: 4300 x 425, 8-bit, classes
  0 ocean/pack ice, 1 continent and ice shelves, 2 fast ice (MODIS),
  3 fast ice (AMSR-E), 4 fast ice (previous/next composite). No byte
  order for the float arrays (they are little-endian), and nothing about
  row order.
- **2D lat/lon that is really 1D.** Latitude is constant along rows,
  longitude constant down columns. Longitude is uniform (0.0423949 degree
  steps from 10 W to 172.26 E). Latitude (71.99 S to 63.5 S) is neither
  uniform nor Mercator: it is linear in WGS84 authalic latitude, i.e.
  cylindrical equal-area.
- **A regular grid, recovered.** In `+proj=cea +lat_ts=-65 +datum=WGS84`
  the cell centres sit within 0.36 m (x) and 0.43 m (y) of an exact
  2000 m square grid. Spherical EASE-Grid (EPSG:3410) is off by 48 m;
  EPSG:6933 fits as well but with 4090.5 x 977.9 m pixels. The grid is
  anchored on round lon/lat (10 W, 63.5 S), not round metres.
- **South-up storage.** Row 0 is 71.99 S. Read as north-up, the map is
  upside down: in storage order land fills the southern rows and the
  expected class appears at nine of ten sampled points; flipped, six of
  those nine are wrong.
- **An undocumented mask, the other way up.** `geo/coastmask.img` is not
  in either readme. It is Int16 little-endian, 0/1, stored north to south;
  flipped, it equals class 1 of the images.
- **A promised file that is not there.** Both readmes say the `.gpd` grid
  point descriptor "used to build the projection is also included". It is
  not, so the CRS here is inferred from the coordinates (the 65 S standard
  parallel from square pixels).
- **A marker pixel.** The last byte of each image (the north-east corner,
  open ocean) is class 3, 4 or 1 in 135 of 159 images.

## How to read it

Verified with GDAL 3.14.0dev on 2026-11-07. One VRT per image, with a
negative line offset to flip it north-up:

```xml
<VRTDataset rasterXSize="4300" rasterYSize="425">
  <SRS>+proj=cea +lat_ts=-65 +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs</SRS>
  <GeoTransform>-472755.311, 2000, 0, -13426012.821, 0, -2000</GeoTransform>
  <VRTRasterBand dataType="Byte" band="1" subClass="VRTRawRasterBand">
    <SourceFilename relativeToVRT="0">/abs/path/imgs/2000_061-080_sqc.img</SourceFilename>
    <ImageOffset>1823200</ImageOffset>
    <PixelOffset>1</PixelOffset>
    <LineOffset>-4300</LineOffset>
    <ByteOrder>LSB</ByteOrder>
  </VRTRasterBand>
</VRTDataset>
```

Open it with `--config GDAL_VRT_RAWRASTERBAND_ALLOWED_SOURCE ALL` unless the
VRT is in the same directory as the `.img`.

- `lats.img` / `lons.img`: Float32, PixelOffset 4, LineOffset -17200,
  ImageOffset 7292800. GDAL's pixel centres, transformed to lon/lat,
  reproduce them to under 0.5 m.
- `coastmask.img`: Int16, PixelOffset 2, LineOffset 8600, ImageOffset 0
  (no flip needed).
- `gdalwarp -t_srs EPSG:3031 -tr 2000 2000 -r near` from the image VRT
  works (1720 x 2918 output).

## Links

- https://data.aad.gov.au/metadata/records/modis_20day_fast_ice
- https://doi.org/10.4225/15/5667AC726B224
- https://hypertidy.github.io/regular-in-what/03-costumes.html

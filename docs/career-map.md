# Career map

## Files and layout

- Wrapper page: `_pages/careermap.html` at `/careermap/`
- Embedded map: `_pages/careermap-map.html` at `/careermap/map.html`
- Work and education data: `_data/cv.json`
- Header visibility: `careermap_link` in `_config.yml` and the Career Map entry in `_data/navigation.yml`

The map reads `education` and `work` entries with a nonempty `address`. Entries sharing an identical address are grouped into one blue marker. Field work sites are a separate list in the map page and use purple markers.

## Add or edit a work or education location

Add an entry to the appropriate array in `_data/cv.json`, or add an `address` to an existing entry. A work entry follows this shape:

```json
{
  "company": "Example institution",
  "position": "Researcher",
  "location": "Department of Physics",
  "startDate": "2026",
  "endDate": "",
  "summary": "Research appointment.",
  "highlights": [],
  "address": "City, Region, Country, Postal code"
}
```

Education entries use `institution` and `area` for their popup labels instead of `company` and `position`. Copy an existing education entry to retain the CV's other fields. Keep addresses consistent when multiple roles should share one marker.

Add the matching work or education information to `_pages/cv.md` if you use the CV sync script. It preserves manual addresses only when identifying fields match: education uses `institution`, `area`, and `endDate`; work uses `company`, `position`, `startDate`, and `endDate`. If those fields change, check and restore the address after syncing.

The map first checks `knownCoordinatesByAddress` in `_pages/careermap-map.html`. To avoid geocoding a known location, add an entry with exactly the same address and coordinates in `[latitude, longitude]` order. Unknown addresses are looked up when the map loads. Prefer known coordinates when a location is ambiguous.

To remove a location from the map while keeping its CV entry, remove its `address` or set it to `""`. To remove the CV entry too, delete the object from the JSON array and update `_pages/cv.md` so a future sync does not recreate it. A shared marker remains while another entry uses that address.

## Add or remove a field work site

Edit the `fieldWorkLocations` array in `_pages/careermap-map.html`. Add an object like this:

```javascript
{
  name: "Field site name",
  coordinates: [63.82, 20.30],
  description: "Field work: Brief description and dates."
}
```

Coordinates are `[latitude, longitude]`. An `address` can replace `coordinates` when the site needs geocoding. Delete the object's entry to remove the marker, and keep commas valid between array entries. Field work sites are independent of `_data/cv.json` and its sync script.

## Hide or remove the map page

Set `careermap_link: false` in `_config.yml` to hide the header link. The map page remains accessible through its URL. Restore `true` to show the link again.

To remove the map entirely, remove its navigation entry and delete both `_pages/careermap.html` and `_pages/careermap-map.html`. Remove `.github/workflows/refresh_map.yml` too, because it expects the map source file to exist. Keep `_data/cv.json` if the CV page still uses it.

## Validate and preview

Validate the JSON before building:

```bash
/Users/danywaller/code/venvs/webpae/bin/python -m json.tool _data/cv.json > /dev/null
```

Run `./preview.sh` and open `/careermap/`. Activate map interaction, inspect marker locations and popups, and check that the work and education entries also look correct on `/cv-json/`.

The map data is embedded during the Jekyll build, so changes appear after rebuilding. The existing `.github/workflows/refresh_map.yml` also updates a source marker when `_data/cv.json` changes; the map does not need a separate generated data file.

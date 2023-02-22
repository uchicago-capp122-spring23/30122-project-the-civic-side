import geopandas
import pathlib
filename= pathlib.Path("cleanzipcodes_geopandas.py").parent /"Shape Files/Boundaries - Ward Precincts (2012-2022)/geo_export_c1120613-195d-4306-86e8-8406a30ee539.shp"
precincts = geopandas.read_file(filename)
zipfile = pathlib.Path("cleanzipcodes_geopandas.py").parent /"Shape Files/Chicagozipshape/geo_export_a5b7e796-fdb8-4ec5-9369-cbebeb1ef23f.shp"
zips= geopandas.read_file(zipfile)
overlap= geopandas.sjoin(precincts, zips)
trimmed_overlap = overlap[["ward","precinct","zip"]]
trimmed_overlap.to_csv("datasets/matched_zipcode_precinct.csv")
#how do I make sure these relationships are unique?
#how do I pick shape files? Any way to look without doing a full import?
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from geodatasets import get_path
import folium

def main():
    # world = geopandas.read_file(get_path("naturalearth.land"))
    map = folium.Map(location=[13.406, 80.110], tiles="CartoDB Positron", zoom_start=9)
    # ax = map.plot()
    plt.show()

if __name__ == "__main__":
    main()

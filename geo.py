import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

if __name__ == '__main__':
    nyc = gpd.read_file(gpd.datasets.get_path('nybb'))
    nyc = nyc.to_crs(epsg=3857)
    ax = nyc.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
    ctx.add_basemap(ax)
    plt.show()

config = {'version': 'v1', 'config': {'visState': {'filters': [], 'layers': [{'id': 'hylbwoe', 'type': 'point', 'config': {'dataId': 'schools', 'label': 'Schools - Fiber Dist.', 'color': [30, 150, 190], 'highlightColor': [252, 242, 26, 255], 'columns': {'lat': 'Latitude', 'lng': 'Longitude', 'altitude': None}, 'isVisible': True, 'visConfig': {'radius': 6, 'fixedRadius': False, 'opacity': 0.8, 'outline': False, 'thickness': 2, 'strokeColor': None, 'colorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#FFC300', '#F1920E', '#E3611C', '#C70039', '#900C3F', '#5A1846'], 'reversed': True}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radiusRange': [0, 50], 'filled': True}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': 'Fiber Node Distance, km', 'type': 'real'}, 'colorScale': 'quantile', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear'}}, {'id': '4jero29', 'type': 'point', 'config': {'dataId': 'schools', 'label': 'Schools - Cell Tower Dist.', 'color': [30, 150, 190], 'highlightColor': [252, 242, 26, 255], 'columns': {'lat': 'Latitude', 'lng': 'Longitude', 'altitude': None}, 'isVisible': False, 'visConfig': {'radius': 6, 'fixedRadius': False, 'opacity': 0.8, 'outline': False, 'thickness': 2, 'strokeColor': None, 'colorRange': {'name': 'ColorBrewer OrRd-6', 'type': 'sequential', 'category': 'ColorBrewer', 'colors': ['#fef0d9', '#fdd49e', '#fdbb84', '#fc8d59', '#e34a33', '#b30000'], 'reversed': False}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radiusRange': [0, 50], 'filled': True}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': 'Cell Tower Distance, km', 'type': 'real'}, 'colorScale': 'quantile', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear'}}, {'id': 'hbylzzo', 'type': 'point', 'config': {'dataId': 'schools', 'label': 'Schools - 4G', 'color': [179, 173, 158], 'highlightColor': [252, 242, 26, 255], 'columns': {'lat': 'Latitude', 'lng': 'Longitude', 'altitude': None}, 'isVisible': False, 'visConfig': {'radius': 6, 'fixedRadius': False, 'opacity': 0.8, 'outline': False, 'thickness': 2, 'strokeColor': None, 'colorRange': {'name': 'Custom Palette', 'type': 'custom', 'category': 'Custom', 'colors': ['#00939C', '#C22E00']}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radiusRange': [0, 50], 'filled': True}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': '4G Coverage', 'type': 'string'}, 'colorScale': 'ordinal', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear'}}, {'id': '6zc1e8', 'type': 'geojson', 'config': {'dataId': 'subdivision_stats', 'label': 'Regional - Unconnected Sch., %', 'color': [18, 147, 154], 'highlightColor': [252, 242, 26, 255], 'columns': {'geojson': 'WKT'}, 'isVisible': False, 'visConfig': {'opacity': 1, 'strokeOpacity': 0.8, 'thickness': 0.5, 'strokeColor': [214, 214, 213], 'colorRange': {'name': 'ColorBrewer Greys-6', 'type': 'singlehue', 'category': 'ColorBrewer', 'colors': ['#f7f7f7', '#d9d9d9', '#bdbdbd', '#969696', '#636363', '#252525']}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radius': 10, 'sizeRange': [0, 10], 'radiusRange': [0, 50], 'heightRange': [0, 500], 'elevationScale': 5, 'enableElevationZoomFactor': True, 'stroked': True, 'filled': True, 'enable3d': False, 'wireframe': False}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': '% Of Unconnected Schools In The Subdivision', 'type': 'real'}, 'colorScale': 'quantile', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear', 'heightField': None, 'heightScale': 'linear', 'radiusField': None, 'radiusScale': 'linear'}}, {'id': 'nv2vfre', 'type': 'geojson', 'config': {'dataId': 'subdivision_stats', 'label': 'Regional - Av. Fiber Dist.', 'color': [18, 147, 154], 'highlightColor': [252, 242, 26, 255], 'columns': {'geojson': 'WKT'}, 'isVisible': False, 'visConfig': {'opacity': 1, 'strokeOpacity': 0.8, 'thickness': 0.5, 'strokeColor': [205, 225, 244], 'colorRange': {'name': 'ColorBrewer Blues-6', 'type': 'singlehue', 'category': 'ColorBrewer', 'colors': ['#08519c', '#3182bd', '#6baed6', '#9ecae1', '#c6dbef', '#eff3ff'], 'reversed': True}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radius': 10, 'sizeRange': [0, 10], 'radiusRange': [0, 50], 'heightRange': [0, 500], 'elevationScale': 5, 'enableElevationZoomFactor': True, 'stroked': True, 'filled': True, 'enable3d': False, 'wireframe': False}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': '% Of 4G Covered Schools', 'type': 'real'}, 'colorScale': 'quantile', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear', 'heightField': None, 'heightScale': 'linear', 'radiusField': None, 'radiusScale': 'linear'}}, {'id': 'zpg82dr', 'type': 'geojson', 'config': {'dataId': 'subdivision_stats', 'label': 'Regional - Av. Cell Tower Dist.', 'color': [18, 147, 154], 'highlightColor': [252, 242, 26, 255], 'columns': {'geojson': 'WKT'}, 'isVisible': False, 'visConfig': {'opacity': 1, 'strokeOpacity': 0.8, 'thickness': 0.5, 'strokeColor': [205, 225, 244], 'colorRange': {'name': 'Ocean Green 6', 'type': 'sequential', 'category': 'Uber', 'colors': ['#93CFBF', '#72BFC4', '#52AEC9', '#4095B5', '#3A748A', '#37535E'], 'reversed': True}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radius': 10, 'sizeRange': [0, 10], 'radiusRange': [0, 50], 'heightRange': [0, 500], 'elevationScale': 5, 'enableElevationZoomFactor': True, 'stroked': True, 'filled': True, 'enable3d': False, 'wireframe': False}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': 'Avg. Cell Tower Distance, km', 'type': 'real'}, 'colorScale': 'quantile', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear', 'heightField': None, 'heightScale': 'linear', 'radiusField': None, 'radiusScale': 'linear'}}, {'id': 'hpeatpw', 'type': 'geojson', 'config': {'dataId': 'subdivision_stats', 'label': 'Regional - 4G', 'color': [18, 147, 154], 'highlightColor': [252, 242, 26, 255], 'columns': {'geojson': 'WKT'}, 'isVisible': False, 'visConfig': {'opacity': 1, 'strokeOpacity': 0.8, 'thickness': 0.5, 'strokeColor': [18, 92, 119], 'colorRange': {'name': 'ColorBrewer Greens-6', 'type': 'singlehue', 'category': 'ColorBrewer', 'colors': ['#edf8e9', '#c7e9c0', '#a1d99b', '#74c476', '#31a354', '#006d2c'], 'reversed': False}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radius': 10, 'sizeRange': [0, 10], 'radiusRange': [0, 50], 'heightRange': [0, 500], 'elevationScale': 5, 'enableElevationZoomFactor': True, 'stroked': True, 'filled': True, 'enable3d': False, 'wireframe': False}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': '% Of 4G Covered Schools', 'type': 'real'}, 'colorScale': 'quantile', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear', 'heightField': None, 'heightScale': 'linear', 'radiusField': None, 'radiusScale': 'linear'}}], 'interactionConfig': {'tooltip': {'fieldsToShow': {'schools': [{'name': 'Source School ID', 'format': None}, {'name': 'School Name', 'format': None}, {'name': 'Internet Availability', 'format': None}, {'name': 'Fiber Node Distance, km', 'format': None}, {'name': 'Cell Tower Distance, km', 'format': None}, {'name': '4G Coverage', 'format': None}, {'name': 'Population Within The 1 km Radius Zone', 'format': None}], 'subdivision_stats': [{'name': 'Subdivision Name', 'format': None}, {'name': 'Number Of Schools', 'format': None}, {'name': '% Of Unconnected Schools In The Subdivision', 'format': '.1%'}, {'name': 'Avg. Fiber Node Distance, km', 'format': None}, {'name': 'Avg. Cell Tower Distance, km', 'format': None}, {'name': '% Of 4G Covered Schools', 'format': '.1%'}, {'name': 'Avg. Population Around Schools within 1km', 'format': None}]}, 'compareMode': False, 'compareType': 'absolute', 'enabled': True}, 'brush': {'size': 0.5, 'enabled': False}, 'geocoder': {'enabled': False}, 'coordinate': {'enabled': False}}, 'layerBlending': 'normal', 'splitMaps': [], 'animationConfig': {'currentTime': None, 'speed': 1}}, 'mapState': {'bearing': 0, 'dragRotate': False, 'latitude': -14.936754298489257, 'longitude': -58.09087520350815, 'pitch': 0, 'zoom': 3.785476299338243, 'isSplit': False}, 'mapStyle': {'styleType': 'dark', 'topLayerGroups': {'border': True, 'label': True}, 'visibleLayerGroups': {'label': True, 'road': True, 'border': True, 'building': True, 'water': True, 'land': False, '3d building': False}, 'threeDBuildingColor': [9.665468314072013, 17.18305478057247, 31.1442867897876], 'mapStyles': {}}}}
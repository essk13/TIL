/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React, {useState, useEffect} from 'react';
import {StyleSheet, View} from 'react-native';
import MapboxGL from '@react-native-mapbox-gl/maps';
import Geolocation from 'react-native-geolocation-service';

MapboxGL.setAccessToken(
  'pk.eyJ1Ijoic29vaHdhbiIsImEiOiJjbDJuM242enowNnc0M2ZtZjh5ejFtMDltIn0.47CV1MNQaI1oHidzfEcbFA',
);

const App = () => {
  const [coordinates, setCoordinates] = useState([128.4202, 36.1107]);
  const [route, setRoute] = useState({
    type: 'FeatureCollection',
    features: [
      {
        type: 'Feature',
        properties: {},
        geometry: {
          type: 'LineString',
          coordinates: [],
        },
      },
    ],
  });

  useEffect(() => {
    getLocation();
  }, []);

  // My Geolocation (GPS)
  const getLocation = () => {
    Geolocation.getCurrentPosition(
      position => {
        if (route.features[0].geometry.coordinates === []) {
          route.features[0].geometry.coordinates.push(coordinates);
        } else if (
          coordinates !== [position.coords.longitude, position.coords.latitude]
        ) {
          route.features[0].geometry.coordinates.push(coordinates);
        }
        setCoordinates([position.coords.longitude, position.coords.latitude]);
      },
      error => {
        // See error code charts below.
        console.log(error.code, error.message);
      },
      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
    );
  };

  const renderAnnotations = () => {
    return (
      <MapboxGL.PointAnnotation
        key="pointAnnotation"
        id="pointAnnotation"
        coordinate={[74, 27]}>
        <View
          style={{
            height: 30,
            width: 30,
            backgroundColor: 'red',
            borderRadius: 50,
            borderColor: '#fff',
            borderWidth: 3,
          }}
        />
      </MapboxGL.PointAnnotation>
    );
  };

  return (
    <View style={styles.page}>
      <View style={styles.container}>
        <MapboxGL.MapView style={styles.map}>
          <MapboxGL.Camera zoomLevel={13} centerCoordinate={coordinates} />
          <MapboxGL.PointAnnotation coordinate={coordinates} />
          <View>{renderAnnotations()}</View>
          <MapboxGL.ShapeSource id="line1" shape={route}>
            <MapboxGL.LineLayer
              id="linelayer1"
              style={{
                lineColor: 'red',
                lineWidth: 5,
                lineCap: 'round',
                lineJoin: 'round',
              }}
            />
          </MapboxGL.ShapeSource>
        </MapboxGL.MapView>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  page: {
    flex: 1,
  },
  container: {
    height: '100%',
    width: '100%',
    flex: 1,
  },
  markerContainer: {
    alignItems: 'center',
    width: 60,
    backgroundColor: 'transparent',
    height: 70,
  },
  map: {
    flex: 1,
  },
  textContainer: {
    backgroundColor: 'white',
    borderRadius: 10,
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
  },
  text: {
    textAlign: 'center',
    paddingHorizontal: 5,
    flex: 1,
  },
  icon: {
    paddingTop: 10,
  },
});

export default App;

// setTimeout(
//   () =>
//     Geolocation.getCurrentPosition(
//       position => {
//         if (route.features[0].geometry.coordinates.length === 0) {
//           setCoordinates([
//             position.coords.longitude,
//             position.coords.latitude,
//           ]);
//           if (coordinates[0] === 0 && coordinates[0] === 0) {
//             console.log('없어');
//           } else {
//             console.log('first' + coordinates);
//             const newRoute = route;
//             newRoute.features[0].geometry.coordinates.push(coordinates);
//             setRoute(newRoute);
//             console.log(route.features[0].geometry.coordinates);
//           }
//         } else if (
//           coordinates[0] !== position.coords.longitude &&
//           coordinates[0] !== position.coords.latitude
//         ) {
//           if (coordinates[0] === 0 && coordinates[0] === 0) {
//             console.log('없어');
//           } else {
//             console.log('next' + coordinates);
//             const newRoute = route;
//             newRoute.features[0].geometry.coordinates.push(coordinates);
//             setRoute(newRoute);
//             console.log(route.features[0].geometry.coordinates);
//           }
//         }
//         setCoordinates([position.coords.longitude, position.coords.latitude]);
//       },
//       error => {
//         // See error code charts below.
//         console.log(error.code, error.message);
//       },
//       {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
//     ),
//   5000,
// );

/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React, {Component} from 'react';
import type {Node} from 'react';
import {StyleSheet, Text, View, Image} from 'react-native';

class Lemon extends Component {
  render() {
    let img = '';
    if (this.props.type == 'one') {
      img = require('./assets/lemon.png');
    } else {
      img = require('./assets/doctor.png');
    }

    return (
      <View>
        <Image source={img} style={{width: 105, height: 100}} />
      </View>
    );
  }
}

const App: () => Node = () => {
  return (
    <View style={styles.container}>
      <Lemon type={'one'} />
      <Text style={styles.hello}>Lemonaid</Text>
      <Lemon type={'two'} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  hello: {
    fontSize: 30,
    fontWeight: '600',
    color: 'black',
  },
});

export default App;

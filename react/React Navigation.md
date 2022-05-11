[TOC]

# 리액트 네비게이션으로 여러 화면 관리하기

> react-navigation 라이브러리를 통해 화면을 전환하는 방법 학습 (LearnReactNavigation 프로젝트)



## react-navigation 설치 및 적용

> LearnReactNavigation 프로젝트를 생성한 뒤 라이브러리 설치

### @react-native/native 모듈 설치

```bash
$ npm install @react-navigation/native
```

### react-navigation 의존 라이브러리 설치

```bash
$ npm install react-native-screens react-native-safe-area-context
```

### 라이브러리 적용

> NavigationContainer 컴포넌트를 불러와 앱 전체를 감싸줌

**App.js**

```js
import React from 'react';
import {NavigationContainer} from '@react-navigation/native';

function App() {
  return <NavigationContainer>{/* 내비게이션 설정 */}</NavigationContainer>;
}

export default App;
```



## 기본적인 사용법

> 브라우저의 History 와 같은 스택 자료구조를 구현하기 위해 Native Stack Navigator 를 사용

### 네이티브 스택 네비게이터

> 안드로이드는 Fragment, iOS는 UINavigationController 를 사용해 일반 네이티브 앱과 동일한 방식으로 화면을 관리

#### 라이브러리 추가 설치

```bash
$ npm install @react-navigation/native-stack
```

**App.js**

> createNativeStackNavigator 를 사용하여 Stack 객체를 생성 (Stack.Navigator, Stack.Screen 포함)

- **initialRouteName** : 기본적으로 보여줄 화면의 이름 (초기 화면, 설정하지 않으면 첫 번째 화면)

- **name** : 화면의 이름을 설정하는 Props (다른 화면으로 이동하거나 현재 화면을 조회할 때 사용)

- **Screen** 으로 사용된 컴포넌트는 **'navigation, route' Props**를 받아옴

  - **navigation**

    > navigate, push, pop, popToTop 등의 함수를 사용할 수 있으며 파라미터를 설정할 수도 있음

    - **navigate** : 동일한 화면에서 파라미터만 변하는 경우 스택을 쌓지 않음
    - **push** : 동일한 화면이라도 스택이 쌓여가면서 화면이 전환됨

    ```js
    navigation.navigate('Detail')
    navigation.navigate('Detail', {id: 1})
    navigation.push('Detail', {id: 2})
    ```

    - **pop** : 이전 화면으로 이동
    - **popToTop** : 가장 첫 번째 화면으로 이동

    ```js
    navigation.pop()
    navigation.popToTop()
    ```

  - **route**

    > route Props 는 객체 타입으로 다음과 같은 정보가 들어있음

    ```js
    {
    	"key": "Detail-vgDx8-H-8e7oao6a3xJz7",
    	"name": "Detail",
    	"params": {"id": 1}
    }
    ```

**App.js**

```js
import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import HomeScreen from './screens/HomeScreen';
import DetailScreen from './screens/DetailScreen';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Detail" component={DetailScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

**screens/HomeScreen.js**

```js
import React from 'react';
import {View, Button} from 'react-native';

function HomeScreen({navigation}) {
  return (
    <View>
      <Button
        title="Detail 1 열기"
        onPress={() => navigation.push('Detail', {id: 1})}
      />
      <Button
        title="Detail 2 열기"
        onPress={() => navigation.push('Detail', {id: 2})}
      />
      <Button
        title="Detail 3 열기"
        onPress={() => navigation.push('Detail', {id: 3})}
      />
    </View>
  );
}

export default HomeScreen;
```

**screens/DetailScreen.js**

```js
import React from 'react';
import {View, Text, StyleSheet, Button} from 'react-native';

function DetailScreen({route, navigation}) {
  return (
    <View style={styles.block}>
      <Text style={styles.text}>id: {route.params.id}</Text>
      <View style={styles.buttons}>
        <Button
          title="다음"
          onPress={() => navigation.push('Detail', {id: route.params.id + 1})}
        />
        <Button title="뒤로가기" onPress={() => navigation.pop()} />
        <Button title="처음으로" onPress={() => navigation.popToTop()} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  (...)
});

export default DetailScreen;
```



## 헤더 커스터마이징

### 타이틀 텍스트 변경

### 헤더 스타일 변경

### 헤더 영역에 다른 컴포넌트 보여주기

### 헤더 숨기기

> Screen 의 options 중 **headerShown 값을 false 로 설정**하여 헤더 숨기기

- **iOS** 의 경우 StatusBar 영역을 침범할 수 있어 **SafeAreaView 컴포넌트를 사용**해야 함

  > **react-navigation 에 react-native-safe-area-context 가 내장**되어 있어 따로 설치하지 않아도 됨

**App.js**

```js
<Stack.Screen
	name="Headerless"
	component={HeaderlessScreen}
	options={{
    headerShown: false,
  }}
/>
```

### 헤더와 관련한 설정을 모든 화면에 적용

> Stack.Navigator 에 screenOptions 라는 Props 설정

**App.js**

```js
<Stack.Navigator
  initialRouteName="Home"
  screenOptions={{
    headerShown: false,
  }}>
```



## 다양한 네비게이터

> react-navigation 의 스택 네비게이터 외에 다양한 특성을 가진 네비게이터 활용

### 드로어 네비게이터 (Drawer Navigator)

> 좌측 또는 우측에 사이드바를 만들고 싶을 때 사용

#### 라이브러리 설치

- **react-native-gesture-handler** : 드로어 네비게이터에서 사용자 제스처를 인식

- **react-native-reanimated** : 내장된 효과보다 더욱 개선된 성능의 애니메이션 효과 구현

  > 현재 react-native-gesture-handler, react-native-reanimated 를 설치하면 오류 발생

```bash
$ npm install @react-navigation/drawer react-native-gesture-handler react-native-reanimated
```

#### 드로어 커스터마이징

### 하단 탭 네비게이터 (Bottom Tab Navigator)

> 하단에 탭을 보여주는 네비게이터 (https://reactnavigation.org/docs/bottom-tab-navigator/)

#### 라이브러리 설치

```bash
$ npm install @react-navigation/bottom-tabs react-native-vector-icons
```

- **Tab.Navigator** 가 **Tab.Screen** 을 감싸는 구조
- **tabBarIcon** 에는 함수 컴포넌트가 들어가고, 'focused, color, size' 를 Props 로 받아옴

#### 하단 탭 커스터마이징

> Tab.Navigator 의 screenOptions Props 를 통해 하단 탭에 대한 설정 커스터마이징

- **tabBarActiveTintColor** : 활성화된 항목의 아이콘과 텍스트 색상
- **tabBarActiveBackgroundColor** : 활성화된 항목의 배경색
- **tabBarInactiveTintColor** : 비활성화된 항목의 아이콘과 텍스트 색상
- **tabBarInactiveBackgroundColor** : 비활성화된 항목의 배경색
- **tabBarShowLabel** : 항목에서 텍스트의 가시성 설정 (기본값 : true)
- **tabBarShowIcon** : 항목에서 아이콘의 가시성 설정 (기본값 : false)
- **tabBarStyle** : 하단 탭 스타일
- **tabBarLabelStyle** : 텍스트 스타일
- **tabBarItemStyle** : 항목 스타일
- **tabBarLabelPosition** : 텍스트 위치 'beside-icon' (아이콘 우측) / 'below-icon' (아이콘 하단)
- **tabBarAllowFontScaling** : 시스템 폰트 크기에 따라 폰트 크기를 키울지 결정 (기본값 : true)
- **tabBarSafeAreaInset** : SafeAreaView의 forceInset 을 덮어쓰는 객체 (기본값 : {bottom: 'always', top: 'never'})
- **tabBarKeyboardHidesTabBar** : 키보드가 나타날 때 하단 탭을 가릴지 결정 (기본값 : false)

**App.js**

```js
import {NavigationContainer} from '@react-navigation/native';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

<NavigationContainer>
  <Tab.Navigator
    initialRouteName="Home"
    screenOptions={{
      tabBarActiveTintColor: '#fb8c00',
      tabBarShowLabel: false,
    }}>
    <Tab.Screen
      name="Home"
      component={HomeScreen}
      options={{
        title: '홈',
        tabBarIcon: ({color, size}) => (
          <Icon name="home" color={color} size={size} />
        ),
      }}
    />
    <Tab.Screen name="Search" component={SearchScreen} />
    <Tab.Screen name="Notification" component={NotificationScreen} />
    <Tab.Screen name="Message" component={MessageScreen} />
  </Tab.Navigator>
</NavigationContainer>
```

#### 스택 네비게이터와 하단 탭 네비게이터 함께 사용하기



### 머티리얼 상단 탭 네비게이터 (Material Top Tab Navigator)

### 머티리얼 하단 탭 네비게이터 (Material Bottom Tab Navigator)

> 하단에만 나타나며, 활성화된 탭에 따라 물결 효과와 함께 전체 탭의 배경색을 변경할 수 있음

- **react-native-paper** : 리액트 네이티브에서 머티리얼 디자인을 사용할 수 있는 라이브러리

  > https://callstack.github.io/react-native-paper/

```bash
$ npm install @react-navigation/material-bottom-tabs react-native-paper
```


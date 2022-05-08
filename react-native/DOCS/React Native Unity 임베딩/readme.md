# React Native에 Unity 임베딩

> Develop Environment
> 
> OS : Window 10
> 
> React-native : 0.68.1
> 
> Unity : 21.3.1f1
> 
> plugin : [@azesmway/react-native-unity](https://github.com/azesmway/react-native-unity)



### Installation

> 본 문서는 RN 프로젝트가 생성되어있다는 전제하에 작성되었다.

- **@azesmway/react-native-unity 라이브러리 설치**
  
  프로젝트 콘솔에서 하단 코드 입력
  
  ```bash
  $ npm install @azesmway/react-native-unity
  
  or
  
  $ yarn add @azesmway/react-native-unity
  ```



### Unity 세팅

1. **Build Setting**
   
   > File → Build Setting → Android
   
   - Export Project: 체크

2. **Resolution and Presentation**
   
   > Eidt → Project Settings → Player → Resolution and Presentation
   
   - FullscreenMode: Windowed 선택
   
   - Hide Navigation Bar: 체크 해제
   
   - Render outside safe area: 체크 해제

3. **Other Settings**
   
   > Eidt → Project Settings → Player → Other Settings
   
   - Scripting Backend: IL2CPP 선택
   
   - ARM64: 체크

4. **Export**
   
   > File → Build Setting → Build



### React Native Project에 Unity build 파일 이동

1. **Directory**
   
   - Root 디렉토리 → unity/builds/android 디렉토리 생성
   
   - android/app 디렉토리 → libs 디렉토리 생성

2. **Files**
   
   - unity/builds/android 디렉토리에 Export 한 Unity 파일 이동
   
   - unity/builds/android 의 local.properties 파일 android 디렉토리에 **복사**
   
   - unity/builds/android/unityLibrary/libs 하위 파일 android/app/libs로 **복사**



### Build Settings

1. **android/app/build.gradle**
   
   아래 코드 추가
   
   ```groovy
   android{
       ...
       defaultConfig {
       ...
           // Unity NDK
           ndk {
               abiFilters "armeabi-v7a", "arm64-v8a"
           }
       }
   }
   
   dependencies {
       ...
       // Unity Library
       implementation project(':unityLibrary')
       implementation files("${project(':unityLibrary').projectDir}/libs/unity-classes.jar")
       ...
   }
   ```

2. **android/build.gradle**
   
   아래 코드 추가
   
   ```groovy
   allprojects {
       repositories {
           flatDir {
               dirs "$rootDir/app/libs"
           }
       }
   }
   ```

3. **android/gradle.properties**
   
   아래 코드 추가
   
   ```properties
   unityStreamingAssets=.unity3d
   ```

4. **android/settings.gradle**
   
   아래 코드 추가
   
   ```groovy
   include ':unityLibrary'
   project(':unityLibrary').projectDir=new File('..\\unity\\builds\\android\\unityLibrary')
   ```

5. **android/app/src/main/res/values/string.xml**
   
   아래 코드 추가
   
   ```xml
   <string name="game_view_content_description">Game view</string>
   <string name="unity_root">unity_root</string>
   ```

6. **android/app/src/main/AndroidMainfest.xml**
   
   아래 코드 추가
   
   ```xml
   <application
     ...
     android:extractNativeLibs="true" >
     <activity
       android:name=".MainActivity"
       ...
       android:hardwareAccelerated="true" >
     ...
     </activity>
   </application>
   ```

7. **unity/builds/android/unityLibrary/build.gradle**
   
   아래 코드 수정 (SDK 최소버전을 21로 수정)
   
   ```groovy
   android {
       ...
       defaultConfig {
           minSdkVersion 21 // 22 → 21
           ...
       }
   }
   ```

8. **\<option> unity/builds/android/unityLibrary/src/main/AndroidManifest.xml**
   
   아래 코드 삭제
   
   ```xml
   <!-- <activity> 안의 android:theme="@style/UnityThemeSelector" 삭 -->
   <intent-filter>
     <action android:name="android.intent.action.MAIN" />
     <category android:name="android.intent.category.LAUNCHER" />
   </intent-filter>
   ```



### Licenses

> 경로의 {UserName}은 사용자 계정명, 유니티 폴더의 {UnityVersion}은 사용하는 유니티 버전명으로 확인

1. AndroidStudio → SDK Manager → **Google Play Licensing Library** 설치

2. C:\Users\{UserName}\AppData\Local\Android\Sdk 경로의 **licenses 폴더 복사**

3. C:\Program Files\Unity\Hub\Editor\{UnityVersion}\Editor\Data\PlaybackEngines\AndroidPlayer\SDK 경로에 복사한 **licenses 폴더 붙여넣기**



### React Native Code

> Unity 화면을 띄울 컴포넌트 파일에서 아래와 같은 형식으로 코드 작성
> 
> (Typescript(.tsx) 사용 가능)

1. **App.js 코드 수정**
   
   ```js
   import React, {useRef, useEffect} from 'react';
   import {View} from 'react-native';
   import UnityView from '@azesmway/react-native-unity';
   
   interface IMessage {
     gameObject: string;
     methodName: string;
     message: string;
   }
   
   function Unity() {
     const unityRef = useRef();
     const message: IMessage = {
       gameObject: 'gameObject',
       methodName: 'methodName',
       message: 'message',
     };
     // RN to Unity Message
     useEffect(() => {
       setTimeout(() => {
         if (unityRef && unityRef.current) {
           unityRef.current.postMessage(
             message.gameObject,
             message.methodName,
             message.message,
           );
         }
       }, 6000);
     }, []);
   
     return (
       <View style={{flex: 1}}>
         <UnityView
           ref={unityRef}
           style={{flex: 1}}
           onUnityMessage={result =>
             console.log('onUnityMessage', result.nativeEvent.message)
           }
         />
       </View>
     );
   }
   
   export default Unity;
   ```



### RN 과 Unity 소통

1. **Unity to RN**
   아래 스크립트 생성 후 {보낼 메시지}에 원하는 내용 전달
   
   ```csharp
   // Unity에서 메시지 전달
   using System;
   using System.Collections;
   using System.Collections.Generic;
   using System.Runtime.InteropServices;
   using UnityEngine.UI;
   using UnityEngine;
   
   public class NativeAPI {
   #if UNITY_IOS && !UNITY_EDITOR
     [DllImport("__Internal")]
     public static extern void sendMessageToMobileApp(string message);
   #endif
   }
   
   public class ButtonBehavior : MonoBehaviour
   {
     public void ButtonPressed()
     {
       if (Application.platform == RuntimePlatform.Android)
       {
         using (AndroidJavaClass jc = new AndroidJavaClass("com.azesmwayreactnativeunity.ReactNativeUnityViewManager"))
         {
           jc.CallStatic("sendMessageToMobileApp", "{보낼 메시지}");
         }
       }
       else if (Application.platform == RuntimePlatform.IPhonePlayer)
       {
         #if UNITY_IOS && !UNITY_EDITOR
           NativeAPI.sendMessageToMobileApp("The button has been tapped!");
         #endif
       }
     }
   }
   ```
   
   ```js
   // RN에서 메시지 수신
   <UnityView
     ref={unityRef}
     style={{flex: 1}}
     // 메시지 수신 위치
     onUnityMessage={result =>
       console.log('onUnityMessage', result.nativeEvent.message)
     }
   />
   ```

2. **RN to Unity**
   
   아래 코드를 통해 메시지 전달
   
   > 'gameObject': 전달 받을 오브젝트 명칭
   > 
   > 'methodName': 전달 받을 스크립트 내 메서드 명칭
   > 
   > 'message': 보낼 메시지
   
   ```js
   // React Native에서 메시지 전송
   interface IMessage {
     gameObject: string;
     methodName: string;
     message: string;
   }
   
   function Unity() {
     const unityRef = useRef();
     const message: IMessage = {
       gameObject: 'GameObject',
       methodName: 'RNScript',
       message: 'message',
     };
     // RN to Unity Message
     useEffect(() => {
       setTimeout(() => {
         if (unityRef && unityRef.current) {
           unityRef.current.postMessage(
             message.gameObject,
             message.methodName,
             message.message,
           );
         }
       }, 6000);
     }, []);
   ```
   
   ```csharp
   // Unity에서 메시지 수신
   using System.Collections;
   using System.Collections.Generic;
   using UnityEngine;
   
   public class RNScript : MonoBehaviour
   {
       public void MessageRN(string message)
       {
           print("UNITY Recived message: " + message);
       }
   }
   ```



### 참고문서

1. [[CodeLog/codelog.log] react native에서 unity 임베딩하기](https://velog.io/@codelog/react-native-%EC%97%90%EC%84%9C-unity-%EC%9E%84%EB%B2%A0%EB%94%A9%ED%95%98%EA%B8%B0)

2. [[Dokon Jang/프로그래머의 꿈] minSdkVersion 오류 해결 방법](https://docko.tistory.com/entry/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4-minSdkVersion-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95)

3. [[JAVART/IT는 커피가 필수야] [Unity] Android Sdk 라이센스 문제로 인한 빌드 실패](https://javart.tistory.com/130)

4. [[hemish/사소한 코딩] Failure to initialize 에러](https://birthbefore.tistory.com/15)

5. [[Stack Overflow] NDK is not configured issue in android studio](https://stackoverflow.com/questions/29122903/ndk-is-not-configured-issue-in-android-studio)

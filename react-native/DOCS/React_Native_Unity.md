# React Native에 Unity 임베딩

> Develop Environment
> 
> OS : Window 10
> 
> React-native : 0.68.1
> 
> Unity : 21.3.1f1
> 
> plugin : @azesmway/react-native-unity



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

4. **OnEvent Code**
   
   > Unity 프로젝트 내 C# Script
   > 
   > 내 경우 버튼 생성 후 해당 버튼에 적용하였다.
   
   ```csharp
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
           jc.CallStatic("sendMessageToMobileApp", "The button has been tapped!");
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

5. **Export**
   
   > File → Build Setting → Build



### React Native Project에 Unity build 파일 이동

1. **Directory**
   
   - Root 디렉토리 → unity/builds/android 디렉토리 생성
   
   - android/app 디렉토리 → libs 디렉토리 생성

2. **Files**
   
   - unity/builds/android 디렉토리에 Export 한 Unity 파일 이동
   
   - unity/builds/android 의 local.properties 파일 android 디렉토리에 **복사**
   
   - unity/builds/android/unityLibrary/libs 하위 파일 android/app/libs로 **복사**



### Gradle Settings

1. **android/app/build.gradle**
   
   ```json
   defaultConfig {
       ...
       ndk {
           abiFilters "armeabi-v7a", "arm64-v8a"
       }
   }
   ```
   
   

# Debug APK

*Step 1:* Go to the root of the project in the terminal and run the below command:

`react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res`

*Step 2:* Go to android directory:

`cd android`

*Step 3:* Now in this `android` folder, run this command

`./gradlew assembleDebug`

There! you’ll find the apk file in the following path:  
`yourProject/android/app/build/outputs/apk/debug/app-debug.apk`

# Release APK

> **Step 1. Generate a keystore**

You will need a Java generated signing key which is a keystore file used to generate a React Native executable binary for Android. You can create one using the *keytool* in the terminal with the following command

`keytool -genkey -v -keystore your_key_name.keystore -alias your_key_alias -keyalg RSA -keysize 2048 -validity 10000`

`keytool -list -v -keystore "keyname.keystore" -alias aliasname`

Once you run the keytool utility, you’ll be prompted to type in a password. **Make sure you remember the password*

You can change ***your_key_name*** with any name you want, as well as ***your_key_alias***. This key uses key-size 2048, instead of default 1024 for security reason.

> **Step 2. Adding Keystore to your project**

Firstly, you need to copy the file *your_key_name.keystore* and paste it under the ***android/app*** directory in your React Native project folder.

On Terminal:

`mv my-release-key.keystore /android/app`

You need to open your *android\app\build.gradle* file and add the keystore configuration. There are two ways of configuring the project with keystore. First, the common and unsecured way:

build.gradle - keystore Configuration

This is not a good security practice since you store the password in plain text. Instead of storing your keystore password in .gradle file, you can stipulate the build process to prompt you for these passwords if you are building from the command line.

To prompt for password with the Gradle build file, change the above config as:

Release Bundle Configuration Command

> **Step 3. Release APK Generation**

Place your terminal directory to *android* using:  
`cd android`

For Windows,  
`./gradlew assembleRelease`

For Linux and Mac OSX:  
`./gradlew assembleRelease`

As a result, **the APK creation process is done**. You can find the generated APK at *android/app/build/outputs/apk/app-release.apk*. This is the actual app, which you can send to your phone or upload to the Google Play Store. Congratulations, you’ve just generated a React Native Release Build APK for Android.

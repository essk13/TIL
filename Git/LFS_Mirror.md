## [Git] 100MB 이상 파일(커밋)이 존재하는 Repository Mirror

### 1️⃣ 일반적인 Mirroring

1. **옮기려는 Repository 클론 받기 (--mirror 필수)**
   
   ```git
   $ git clone --mirror {old-repository.git}
   ```

2. **옮기려는 Repository로 이동**
   
   ```git
   $ cd {old-repository.git}
   ```

3. **새로운 Repository로 옮기기**
   
   ```git
   $ git push --mirror {new-repository.git}
   ```



### 2️⃣ 100MB가 넘는 파일을 지닌 Repository Mirroring

- Github는 각 파일의 상한선이 100MB로 이를 넘어서는 용량의 파일은 업로드 시 에러가 발생한다. 이를 해결하기 위해서 LFS(Large File Storage)를 통해 대용량 파일을 관리할 수 있다. LFS는 사이트에서 설치하거나 Git bash 창에서 설치할 수 있다.
  
  - [LFS 다운로드](https://git-lfs.github.com/)
  
  - ```git
    $ git lfs install
    ```

- 이미 커밋이 존재하는 경우 이전의 기록들을 제거해야 미러링이 가능하다. 이를 위해서 BFG Repo-Cleaner를 사용하였다. BFG 사용 시 명령어에 {bfs.jar}이 있는데 이 부분은 자신이 다운로드 한 파일명으로 수정해서 사용하면 된다.
  
  - [BFG Repo-Cleaner by rtyley](https://rtyley.github.io/bfg-repo-cleaner/)



**2-1**

- 나는 해당 방법으로 해결하였지만 나에게 맞지 않았던 다른 방법도 하단에 함께 작성해두겠다.
1. **옮기려는 Repository 클론 받기 (--mirror 필수)**
   
   ```git
   $ git clone --mirror {old-repository.git}
   ```

2. **옮기려는 Repository로 이동**
   
   ```git
   $ cd {old-repository.git}
   ```

3. **100MB를 초과하는 파일 제거**
   
   - 나는 bfg-1.14.0.jar을 사용하였기 때문에 해당 명령어를 사용하였다.
     
     이후 {old-repository}.git.bfg-report라는 폴더가 생성된다.
   
   ```git
   java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 100M {old-repository.git}
   ```
   
   - 3-1. **These are your protected commits**
     
     - 위와 같은 에러가 발생한다면 protected commit까지 제거해주는 명령어를 추가한다. (--no-blob-protection)
     
     ```git
     java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 100M --no-blob-protection 
     {old-repository.git}
     ```

4. **새로운 Repository로 옮기기**
   
   ```git
   $ git push --mirror {new-repository.git}
   ```



**2-2**

- 내가 실패했던 방법 (아마 protected commits 때문일 것으로 생각한다.)
1. **옮기려는 Repository 클론 받기 (--mirror 필수)**
   
   ```git
   $ git clone --mirror {old-repository.git}
   ```

2. **옮기려는 Repository로 이동**
   
   ```git
   $ cd {old-repository.git}
   ```

3. **커밋 히스토리 내 대용량 파일 tracking**
   
   - "*.{zip, jar}"과 같이 여러 확장자를 함께 적용하거나 "file.zip"과 같이 특정 파일 하나를 지정할 수 있다.
   
   - 모든 커밋 메시지를 확인하기 때문에 시간이 오래 소요될 수 있다.
   
   ```git
   $ git filter-branch --tree-filter 'git lfs track "*.{확장자명}"' -- --all
   ```

4. **bfg.jar을 이용하여 tracking한 파일들을 LFS로 변경**
   
   - bfg.jar 앞에 다운받은 경로를 작성하거나 .jar 파일을 클론한 레포지토리에 이동시키면 된다. 이후 {old-repository}.git.bfg-report라는 폴더가 생성된다.
     
     예시) ~/download/bfg-1.14.0.jar
   
   ```git
   java -jar bfg-1.14.0.jar --convert-to-git-lfs '*.확장자명'
   ```

5. **새로운 Repository로 옮기기**
   
   ```git
   $ git push --mirror {new-repository.git}
   ```



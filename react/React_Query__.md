[TOC]

# :cherry_blossom: React Query (리액트 쿼리)

> Hook 을 기반으로 API 를 연동할 수 있는 라이브러리
> 
> https://react-query.tanstack.com/

## React Query 를 사용하는 이유

### 기존의 데이터 로딩 로직

- **로딩, 결과, 오류를 위한 상태를  직접 관리**해줘야 함
- 다른 화면으로 이동하여 컴포넌트가 사라질 때 상태 또한 사라짐
  - 기존에 받아온 응답 결과를 사용할 수 없음. 즉, **캐싱되지 않음**
  - 그렇다고 Context, Redux 등의 라이브러리로 관리하는 경우 코드가 많아짐

```js
function MyComponent() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const fetchData = useCallback(() => {
    setLoading(true);
    try {
      const posts = await getPosts();
      setData(posts);
    } catch (e) {
      setError(e);
    } finally {
      setLoading(false);
    }
  })

  useEffect(() => {
    fetchData();
  }, [])

  // ...
}
```

> React Query 를 사용하면 **데이터 로딩**을 훨씬 편하게 할 수 있고, **캐싱**도 기본적으로 제공함

## React Query 활용

### React Query 라이브러리 적용

#### react-query 라이브러리 설치

```bash
$ npm install react-query
```

#### QueryClientProvider 적용

> 캐시를 관리할 때 사용하는 QueryClient 인스턴스를 자식 컴포넌트에서 사용할 수 있게 해줌

**App.tsx**

```tsx
// ...
import {QueryClient, QueryClientProvider} from 'react-query';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
        <NavigationContainer>
          <RootStack />
      </NavigationContainer>
    </QueryClientProvider>
  );
}
// ...
```

### useQuery

> 데이터의 캐시 키와 Promise 를 반환하는 함수를 기반으로 데이터의 로딩/결과/오류 상태를 관리

**예시 코드**

```js
import {useQuery} from 'react-query'

function Sample() {
  const result = useQuery('articles', getArticles);
  const { data, error, isLoading } = result;
}
```

- useQuery의 첫 번째 인자에는 조회하고 싶은 **데이터의 캐시 키**를 넣음 (데이터 캐싱)
  - 한 번 데이터를 받아온 다음, 나중에 같은 요청을 해야 하는 상황에서 **데이터가 이미 존재한다면** 기존에 있던 데이터를 바로 보여줌 (설정에 따라 **데이터를 새로 요청**할 수 있음)
- 두 번째 인자에는 **Promise 를 반환하는 함수**를 넣음
  - 컴포넌트가 렌더링될 때 해당 함수를 호출하고, 이에 대한 상태가 관리됨

#### 반환값

> useQuery Hook을 사용하여 반환된 result 객체는 다음 값을 지니고 있음
> 
> https://react-query.tanstack.com/reference/useQuery

- **status** : API 의 요청 상태를 문자열로 나타냄
  
  - **'loading'** : 아직 데이터를 받아오지 않았고, 현재 데이터를 요청 중
  - **'error'** : 오류 발생
  - **'success'** : 데이터 요청 성공
  - **'idle'** : 비활성화된 상태 (따로 설정해 비활성화한 경우)

- **isLoading** : status === 'loading' 과 같음

- **isError** : status === 'error' 와 같음

- **isSuccess** : status === 'success' 와 같음

- **isIdle** : status === 'idle' 과 같음

- **error** : 오류가 발생했을 때 오류 정보를 지님

- **data** : 요청 성공한 데이터를 가리킴

- **isFetching** : 데이터가 요청 중일 때 true (데이터가 이미 존재하는 상태에서 재요청할 때 isLoading은 false이지만, isFetching은 true)

- **refetch** : 다시 요청을 시작하는 함수

> useQuery Hook 을 사용할 때는 **data, error, isLoading 을 많이 사용**하며, 이 값에 따라 **동적 렌더링**을 구현

```js
import {useQuery} from 'react-query'
import {Text, View} from 'react-native'

function Sample() {
  const result = useQuery('articles', getArticles);
  const { data, error, isLoading } = result;

  if (isLoading) return <Text>로딩 중..</Text>;
  if (error) return <Text>오류 발생</Text>;
  return <View>{/* 데이터 보여주기.. */}</View>;
}
```

#### 배열 타입의 캐시 키

> 요청 함수를 호출하는 상황에서 **파라미터가 필요**하다면 다음과 같이 구현

```js
import {useQuery} from 'react-query';

function Sample({id}) {
  const result = useQuery(['article', id], () => getArticle(id));
}
```

- 캐시 키는 **문자열**로만 이뤄질 수도 있고, 이와 같이 **배열 타입**으로 설정할 수도 있음
  
  - 배열 타입의 캐시 키를 사용할 때는 **원소에 객체**를 넣을 수도 있음 (순서는 상관없음)
    
    ```js
    useQuery(['articles', { start: 0, limit: 10 }], () => ...)
    // 순서 상관없이 동일
    useQuery(['articles', { limit: 10, start: 0 }], () => ...)
    ```

- 요청의 결과물이 **특정 변수**에 따라 달라진다면 꼭 캐시 키에 포함해야 함

#### useQuery의 options

> useQuery를 사용할 때 **세 번째 파라미터에 options 객체**를 넣어서 해당 **Hook의 작동 방식을 설정**할 수 있음

```js
function Sample() {
  const result = useQuery('articles', getArticles, {
    enabled: true,
    refetchOnMount: true,
  });
}
```

- **enabled** : boolean 타입의 값으로, 이 값이 false라면 컴포넌트가 마운트될 때 자동으로 요청하지 않음 (refetch 함수로만 요청이 시작됨)

- **retry** : boolean | number | (failureCount: number, error: TError) => boolean 타입의 값을 설정하며, 요청이 실패했을 때 재요청할지 설정할 수 있음
  
  - 이 값을 **true**로 하면 실패했을 때 성공할 때까지 계속 반복 요청함
  - 이 값을 **false**로 하면 실패했을 때 재요청하지 않음
  - 이 값을 **3**으로 하면 3번까지만 재요청함
  - 이 값을 **함수 타입**으로 설정하면 실패 횟수와 오류 타입에 따라 재요청할지 함수 내에서 결정할 수 있음

- **retryDelay** : number | (retryAttempt: number, error: TError) => number 타입의 값을 설정하며, 요청이 실패한 후 재요청할 때 지연 시간을 얼마나 가질지 설정할 수 있음. 시간 단위는 ms(밀리세컨드, 0.001초)
  
  - 이 값의 기본값은 (retryAttempt) => Math.min(1000 * 2 ** failuerCount, 30000)
    
    > 실패 횟수 n에 따라 2의 n제곱 초만큼 기다렸다가 재요청, 그리고 최대 30초까지 기다림

- **staleTime** : 데이터의 유효 시간을 ms 단위로 설정 (기본값은 0)

- **cacheTime** : 데이터의 캐시 시간을 ms 단위로 설정 (기본값은 5분)
  
  > 캐시 시간은 Hook을 사용하는 컴포넌트가 언마운트되고 나서 해당 데이터를 얼마나 유지할지 결정

- **refetchInterval** : false | number 타입의 값을 설정하며, **n초마다 데이터를 새로고침**하도록 설정할 수 있음. 시간 단위는 ms

- **refetchOnmount** : boolean | 'always' 타입의 값을 설정하며, **컴포넌트가 마운트될 때 재요청**하는 방식을 설정할 수 있음 (기본값은 true)
  
  - **true**일 때는 데이터가 유효하지 않을 때 재요청
  - **false**일 때는 컴포넌트가 다시 마운트되어도 재요청하지 않음
  - **'always'**일 때는 데이터의 유효 여부와 관계없이 무조건 재요청

- **onSuccess** : (data: Data) => void 타입의 함수를 설정. **데이터의 요청이 성공**하고 나서 **특정 함수를 호출**하고 싶을 때 사용

- **onError** : (error: Error) => void 타입의 함수를 설정. **데이터의 요청이 실패**하고 나서 **특정 함수를 호출**하고 싶을 때 사용

- **onSettled** : (data? Data, error?: Error) => void 타입의 함수를 설정. **데이터 요청의 성공 여부와 관계없이** 요청이 끝나면 **특정 함수를 호출**하도록 설정

- **initialData** : Data | () => Data 타입의 값을 설정. Hook에서 사용할 **데이터의 초기값**을 지정

#### staleTime과 cacheTime

- **staleTime** : stale 은 **'신선하지 않다'**라는 의미를 지니며, 해당 시간이 지나고나면 **유효하지 않은 데이터**가 됨
  
  > staleTime 옵션의 기본값은 0이기 때문에, **조회한 순간 데이터는 바로 유효하지 않게 됨**
  
  - 데이터가 유효하지 않다면 **재요청 기회가 주어졌을 때 데이터를 최신화**함
  - 재요청 기회가 주어지는 시점은 **똑같은 캐시 키를 사용**하는 컴포넌트가 마운트될 때

- **cacheTime** : 컴포넌트가 언마운트된 뒤 해당 **데이터를 얼마 동안 유지할지**에 대한 설정
  
  - 캐시에 데이터가 남아있다면 컴포넌트가 마운트될 때 isLoading 값이 true로 되지 않고 **이전에 불러온 데이터가 채워져 있음**
  - 이후 **staleTime**에 따라 데이터의 유효성을 판단하고 재요청 여부를 결정함

### useMutation

> 특정 함수에서 원하는 때에 직접 요청을 시작하여 데이터의 생성/수정/삭제를 구현

**예시 코드**

```js
import {useMutation} from 'react-query';

function Sample() {
  const mutation = useMutation(writeArticle, {
    onMutate: (variables) => {
      /* 요청 직전 처리, 여기서 반환하는 값은 하단 함수들의 context로 사용됨 */
    },
    onError: (error, variables, context) => {
      /* 오류 발생 시 처리 */
    },
    onSuccess: (data, variables, context) => {
      /* 성공 시 처리 */
    },
    onSettled: (data, error, variables, context) => {
      /* 성공 여부와 관계없이 작업이 끝나면 처리 */
    }
  });
  const {mutate, isLoading, isError} = mutation;
}
```

- 첫 번째 인자에 **Promise를 반환하는 함수**를 넣음
- 두 번째 인자에 이 작업이 처리되기 **전후로 실행할 함수를 넣은 옵션 객체**를 넣음 (생략 가능)

#### 반환값

- **mutate** : 요청을 시작하는 함수
  - 첫 번째 인자에는 **API 함수에서 사용할 인자**를 넣음
  - 두 번째 인자에는 **{onSuccess, onSettled, onError} 객체**를 넣음 (생략 가능)
- **mutateAsync** : mutate와 인자는 동일. 함수를 호출했을 때 **반환값이 Promise 타입**
- **status** : 요청의 상태를 문자열로 나타냄 (idle, loading, error, success)
- **isIdle, isLoading, isError, isSuccess** : status 값에 따라 boolean 타입의 값을 나타냄
- **error** : 오류가 발생했을 때 오류 정보를 지님
- **data** : 요청이 성공한 데이터를 가리킴
- **reset** : 상태를 모두 초기화하는 함수

### useQueryClient

#### 데이터 새로고침

> useQuery를 사용할 때 입력한 캐시 키로 기존 데이터를 만료시키고 새로 불러오도록 처리

**예시 코드**

```tsx
// ...
import {useMutation, useQueryClient} from 'react-query';
import {writeArticle} from '../api/articles';

function WriteScreen() {
  // ...
  const queryClient = useQueryClient();
  const {mutate: write} = useMutation(writeArticle, {
    onSuccess: () => {
      queryClient.invalidateQueries('articles');  // articles 캐시 키 만료시키기
      navigation.goBack();
    },
  });

  // ...
```

#### 캐시 데이터 직접 수정

> useMutation 요청을 성공했을 때 응답 결과를 바로 기존 캐시 데이터에 추가

**예시 코드 (게시글 생성)**

```tsx
// ...
import {Article} from '../api/types';


function WriteScreen() {
  // ...
  const queryClient = useQueryClient();
  const {mutate: write} = useMutation(writeArticle, {
    onSuccess: (article) => {
      // 캐시 데이터 조회 (undefined 인 경우 빈 배열)
      const articles = queryClient.getQueryData<Article[]>('articles') ?? [];
      // 캐시 데이터 업데이트
      queryClient.setQueryData('articles', articles.concat(article));
      navigation.goBack();
    },
  });

  // ...
```

- **getQueryData** : 캐시 키를 사용하여 캐시 데이터를 조회할 수 있음 (undefined 일 수도 있음)

- **setQueryData** : 캐시 데이터를 업데이트하는 메서드
  
  - 데이터를 두 번째 인자로 넣어도 되고, **업데이터 함수 형태의 값**을 인자로 넣을 수도 잇음
  
  ```tsx
  // getQueryData 는 생략 가능
  queryClient.setQueryData<Aritcle[]>('articles', (articles) => 
    (articles ?? []).concat(article)
  );
  ```
  
  > API 를 재요청하지 않고 데이터를 업데이트할 수 있음

- 게시글을 **수정하거나 삭제**하는 경우에는 더욱 복잡한 방법이 필요함

## 프로젝트 적용

### useQuery 적용

> 플로깅 상세 조회를 **useQuery** 로 구현

**api/types.ts**

> api 반환 데이터 타입 정의

```tsx
export interface Plogging {
  startedAt: string;
  endedAt: string;
  image: string;
  route: any;
  time: number;
  distance: number;
  calories: number;
  userSeq: number;
}
```

**api/plogging.ts**

> 플로깅 상세 조회 api 구현

```tsx
import Api from '../lib/customApi';  // 커스텀 API 활용
import {Plogging} from './types';

export async function getPloggingDetail(ploggingSeq: number) {
  const response = await Api.get<Plogging>(`/plogging/info/${ploggingSeq}`);
  return response.data;
}
```

**screens/Plogging/PloggingRecordScreen.tsx**

> 컴포넌트에서 useQuery 를 통해 api 요청 (route 의 params.id 정보로 해당 PloggingDetail 조회)

```tsx
// ...
import {useQuery} from 'react-query'
import {getPloggingDetail} from '../../api/plogging';

type PloggingRecordScreenRouteProp = RouteProp<RootStackParamList, 'PloggingRecord'>

function PloggingRecordScreen() {
  const route = useRoute<PloggingRecordScreenRouteProp>();
  const {data, isLoading} = useQuery(['ploggingDetail', route.params.id], () =>
    getPloggingDetail(route.params.id),
  );

  console.log({data, isLoading})

  // ...
```

- 컴포넌트가 렌더링되는 시점에 요청이 시작되어 isLoading 이 true 가 되고, 요청이 완료되면 false로 변함
  
  > - LOG {"data": undefined, "isLoading": true}
  > - LOG {"data": {"startedAt": "2022-04-01T17:07:33.673Z", "endedAt": "2022-04-01T18:00:30.673Z", ...}, "isLoading": false}

#### 경고 처리

- 다음과 같은 경고는 cacheTime 타이머가 돌고있기 때문에 나옴 (무시해도 됨)
  
  > Setting a timer for a long period of time, i.e. multiple minutes, is a performance and correctness issue on Android as it keeps the timer module awake, and timers can only be called when the app is in the foreground. See https://github.com/facebook/react-native/issues/12981 for more info.

- 경고가 나타나는 것이 거슬리는 경우 다음과 같이 설정해서 무시하도록 처리
  
  **index.js**
  
  ```js
  // ...
  import {AppRegistry, LogBox} from 'react-native';
  
  // ...
  
  LogBox.ignoreLogs(['Setting a timer']);
  ```

### useMutation 적용

> 플로깅 기록을 **useMutation** 로 구현

**api/plogging.ts**

```tsx
import Api from '../lib/customApi';
import {Plogging} from './types';

export async function savePlogging(ploggingData: Plogging) {
  const response = await Api.post<Plogging>('/plogging', ploggingData);
  return response.data;
}
```

**screens/Plogging/PloggingMapScreen.tsx**

```tsx
// ...
import {useMutation} from 'react-query';
import {savePlogging} from '../../api/plogging';

function PloggingMapScreen() {
  const [ploggingData, setPloggingData] = useState({
    time: 1000,
    distance: 500,
    // ...
  });
  const {mutate: save, isLoading} = useMutation(savePlogging, {
    onSuccess: (data) => {
      console.log(data);
    },
    onError: (error) => {
      console.error(error);
    },
  });

  // save에 데이터를 담아 api 요청을 시작
  const onSavePlogging = () => {
    save(ploggingData);
  };

  // ...
```

- mutate 의 경우 **save 라는 이름으로 변경**하여 구조분해함 (**useMutations 을 여러개 사용**하는 경우 활용)

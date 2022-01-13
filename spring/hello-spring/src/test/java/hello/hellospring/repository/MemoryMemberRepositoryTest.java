package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import java.util.List;

public class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    /*
    test 시 항목들이 순서대로 실행되는 것이 아니기 때문에
    하나의 test가 종료되면 repository를 초기화하여 상호 의존성 제거
     */
    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }


    @Test
    public void save() {
        Member member = new Member();
        member.setName("spring");

        repository.save(member);

        Member result = repository.findById(member.getId()).get();
        // Output
        // System.out.println("result = " + (result == member)); >> result = True

        // Assertions By jupiter
        // Assertions.assertEquals(member, result); >> Run
        // Assertions.assertEquals(member, result); >> Err

        // Assertions By assertj
        // Assertions.assertThat(member).isEqualTo(null); >> Err
        Assertions.assertThat(member).isEqualTo(result);
    }


    @Test
    public void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        Member result = repository.findByName("spring1").get();

        //Assertions.assertThat(result).isEqualTo(member2); >> Err
        Assertions.assertThat(result).isEqualTo(member1); // >> OK
    }


    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();

        // Assertions.assertThat(result.size()).isEqualTo(3); >> Err
        Assertions.assertThat(result.size()).isEqualTo(2);
    }
}

package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest {

    MemberService memberService;
    MemoryMemberRepository memberRepository;

    @BeforeEach
    public void beforeEach() {
        memberRepository = new MemoryMemberRepository();
         memberService = new MemberService(memberRepository);
    }

    @AfterEach
    public void afterEach() {
        memberRepository.clearStore();
    }

    @Test
    void 회원가입() {
        // given = 검증 데이터
        Member member = new Member();
        member.setName("spring");

        // when = 검증 기반
        Long saveId = memberService.join(member);

        // then = 검증 로직
        Member findMember = memberService.findOne(saveId).get();
        Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    @Test
    public void 중복_회원_예외() {
        // given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when
        memberService.join(member1);
        // assertThrows(NullPointerException.class, () -> memberService.join(member2)); >> Err
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));

        Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");

        /*
            memberService.join(member1);
            try {
                memberService.join(member2);
                fail("예외가 발생해야 합니다.");
            } catch (IllegalStateException e) {
                Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
            }
        */

        // then
    }

    @Test
    void findMembers() {
    }


    @Test
    void findOne() {
    }
}
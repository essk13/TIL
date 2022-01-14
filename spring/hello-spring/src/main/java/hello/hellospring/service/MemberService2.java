package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;

import java.util.List;
import java.util.Optional;


/**
 * Java Code Spring Bean
 */
public class MemberService2 {

    private final MemberRepository memberRepository;

    // (DI) 생성자 주입
    public MemberService2(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    /**
     * SignUp
     */
    public Long join(Member member) {
        // 중복 회원 X
        /*
         Optional<Member> result = memberRepository.findByName(member.getName());
         result.ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다");
                });
         */

        validateDuplicateMember(member);

        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        // Ctrl + Alt + Shift + T (Extract Method)
        memberRepository.findByName(member.getName())
                        .ifPresent(m -> {
                            throw new IllegalStateException("이미 존재하는 회원입니다.");
                        });
    }

    /**
     * All Members List
     */
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    /**
     * One Member Search
     */
    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}

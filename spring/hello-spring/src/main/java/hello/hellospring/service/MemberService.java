package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service // with Service, Repository [Component scan]
public class MemberService {

    private final MemberRepository memberRepository;

    @Autowired
    public MemberService(MemberRepository memberRepository) {
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

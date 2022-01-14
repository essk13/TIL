package hello.hellospring;

import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository2;
import hello.hellospring.service.MemberService;
import hello.hellospring.service.MemberService2;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Java Code Spring Bean
 */
@Configuration
public class SpringConfig {

    @Bean
    public MemberService2 memberService2() {
        return new MemberService2(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository2();
    }
}

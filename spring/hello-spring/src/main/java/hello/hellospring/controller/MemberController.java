package hello.hellospring.controller;

import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;


/**
 * Component Scan & Java Code Spring Bean 모두 적용
 */
@Controller // with Service, Repository [Component scan]
public class MemberController {

    private MemberService memberService;

    @Autowired
    public void setMemberService(MemberService memberService) {
        this.memberService = memberService;
    }


    /** Java Code를 통한 DI 이유
     *  정형화 되지 않거나, 상황에 따라 구현 클래스를 변경해야 하는 경우 편리
     */

    /*
        DI (Dependency Injection / 의존관계 주입)
        1. 필드 주입
        2. setter 주입
        3. 생성자 주입 (권장)
    */


    /*
        ## 생성자 주입 / 권장
        private MemberService memberService;

        @Autowired
        public MemberController(MemberService memberService) {
            this.memberService = memberService;
        }


        ## setter 주입 / 단점: Public 노출
        private MemberService memberService;

        @Autowired
        public void setMemberService(MemberService memberService) {
            this.memberService = memberService;
        }


        ## 필드 주입 / 비추천
        @Autowired private MemberService memberService;
    */
}

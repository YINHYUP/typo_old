
= Table.AddColumn(#"이름을 바꾼 열 수", "연월일", each 
    let
        yearPart = Text.Start(Text.From([#"연월(마감월)"], "ko-KR"), 2), // 연도 부분 (앞의 2자리)
        monthPart = Text.End(Text.From([#"연월(마감월)"], "ko-KR"), 2) // 월 부분 (뒤의 2자리)
    in
        Text.Combine({ "20" & yearPart & "년 ", monthPart & "월 01일" }, "")
)

dax
입고실적+예수량 = 
    VAR ld = MAX('예수량이력_예수량관리용'[일자])
    RETURN 
    CALCULATE(SUM('SomeTable'[미입고_1]), '예수량이력_예수량관리용'[일자] = ld) + 
    CALCULATE(SUM('OPO입고실적'[입고수량]))  // 입고수량* 수정
; Password for Submit: 16andcounting

(define (author)
    (println "AUTHOR: Kyle Galloway ckgalloway@crimson.ua.edu")
)

(define (exprTest # $expr target)
    (define result (catch (eval $expr #)))
    (if (error? result)
        (println $expr " is EXCEPTION: " (result'value)
            " (it should be " target ")")
        (println $expr " is " result
            " (it should be " target ")")
    )
)

; Task 1


; Task 2


; Task 3


; Task 4


; Task 5


; Task 6


; Task 7


; Task 8


; Task 9


; Task 10


; Tests
; (define (run1)
;
; )
; (define (run2)
;
; )
; (define (run3)
;
; )
; (define (run4)
;
; )
; (define (run5)
;
; )
; (define (run6)
;
; )
; (define (run7)
;
; )
; (define (run8)
;
; )
; (define (run9)
;
; )
; (define (run10)
;
; )

; Run tests
; (run1)
; (run2)
; (run3)
; (run4)
; (run5)
; (run6)
; (run7)
; (run8)
; (run9)
; (run10)
(println "assignment 1 loaded!")

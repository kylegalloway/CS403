(include "extras/exprTest.scm")
(include "extras/streamUtils.scm")


; Series = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/8 + 1/10 ...
; Need ones / ints (without 9 as digit)

(define (nine-digit? a)
    (cond
        ((= (% a 10) 9) #t)
        ((< a 10) #f)
        (else (nine-digit? (/ a 10)))
    )
)

(define ints-no-9s (sremove nine-digit? ints))
; (sdisplay ints-no-9s 900)
(define mystery (div-streams ones ints-no-9s))
(define mystery1 (psum mystery))
(define mystery2 (euler-transform mystery1))
(define mystery3 (smap scar (tableau euler-transform mystery2)))
(define mystery4 (smap scar (tableau euler-transform (smap scar (tableau euler-transform mystery3)))))

(define (run8)
    (sdisplay mystery 10)
    (sdisplay mystery1 10)
    (sdisplay mystery2 10)
    (sdisplay mystery3 10)
    ; (sdisplay mystery4 10)
    (print "Infinite Sum is 22.92067")
)


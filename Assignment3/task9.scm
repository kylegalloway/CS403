(include "exprTest.scm")
(include "streamUtils.scm")

(define (cube m) (* m m m))
(define (sum-cubed pair)
    (define x (car pair))
    (define y (cadr pair))

    (+ (cube x) (cube y))
)

(define (ramanujan-finder S)
    (define current (scar S))
    (define next (scadr S))
    (define possible-r (sum-cubed current))

    (cond
        ((== possible-r (sum-cubed next))
            (scons
                possible-r
                (ramanujan-finder (scddr S))
            )
        )
        (else
            (ramanujan-finder (scdr S))
        )
    )
)

(define (ramanujan)
  (ramanujan-finder (weighted-pairs ints ints sum-cubed))
)

(define (run9)
    (sdisplay (ramanujan) 6)
    (inspect (sref (ramanujan) 20))
)
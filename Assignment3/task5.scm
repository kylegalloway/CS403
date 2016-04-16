(include "exprTest.scm")

(define (mmutex n)
    (define number n)
    (define owners '())
    (define (check id)
        ; If id in owners
    )

    (define (p)
        (lock)
        (check (gettid))
        (unlock)
    )
    (define (v)
        (lock)
        (check (gettid))
        (unlock)
    )
    this
)

(define m (mmutex 3))
(exprTest (m'p) 'ACQUIRED)
(exprTest (m'v) 'RELEASED)